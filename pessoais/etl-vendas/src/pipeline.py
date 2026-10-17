"""
Pipeline ETL de vendas: CSV -> validação/transformação -> SQLite.

Uso:
    python src/pipeline.py
"""
import csv
import logging
import sqlite3
from datetime import datetime
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
ARQ_ENTRADA = BASE / "data" / "vendas.csv"
ARQ_SCHEMA = BASE / "sql" / "schema.sql"
ARQ_BANCO = BASE / "data" / "vendas.db"

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
log = logging.getLogger("etl")


def extrair(caminho: Path) -> list[dict]:
    with caminho.open(encoding="utf-8") as f:
        linhas = list(csv.DictReader(f))
    log.info("Extração: %d linhas lidas de %s", len(linhas), caminho.name)
    return linhas


def transformar(linhas: list[dict]) -> tuple[list[tuple], list[dict]]:
    validas, rejeitadas = [], []
    for linha in linhas:
        try:
            data = datetime.strptime(linha["data_venda"].strip(), "%d/%m/%Y").date()
            qtd = int(linha["quantidade"])
            preco = float(linha["preco_unitario"].replace(",", "."))
            if qtd <= 0 or preco < 0:
                raise ValueError("quantidade/preço inválido")
            validas.append((
                int(linha["id_venda"]),
                data.isoformat(),
                linha["produto"].strip().title(),
                linha["uf"].strip().upper(),
                qtd,
                round(preco, 2),
                round(qtd * preco, 2),
            ))
        except (ValueError, KeyError) as erro:
            rejeitadas.append({**linha, "motivo": str(erro)})
    log.info("Transformação: %d válidas, %d rejeitadas", len(validas), len(rejeitadas))
    return validas, rejeitadas


def carregar(registros: list[tuple], banco: Path) -> None:
    with sqlite3.connect(banco) as con:
        con.executescript(ARQ_SCHEMA.read_text(encoding="utf-8"))
        con.executemany(
            "INSERT OR REPLACE INTO fato_vendas VALUES (?, ?, ?, ?, ?, ?, ?)", registros
        )
        total = con.execute("SELECT COUNT(*) FROM fato_vendas").fetchone()[0]
    log.info("Carga: %d registros na tabela fato_vendas", total)


def relatorio(banco: Path) -> None:
    with sqlite3.connect(banco) as con:
        print("\nFaturamento por UF:")
        for uf, valor in con.execute("SELECT * FROM vw_faturamento_uf"):
            print(f"  {uf}: R$ {valor:,.2f}")


def main() -> None:
    linhas = extrair(ARQ_ENTRADA)
    validas, rejeitadas = transformar(linhas)
    for r in rejeitadas:
        log.warning("Rejeitada id=%s: %s", r.get("id_venda"), r["motivo"])
    carregar(validas, ARQ_BANCO)
    relatorio(ARQ_BANCO)


if __name__ == "__main__":
    main()
