"""Testes unitários do pipeline ETL de vendas (unittest, sem dependências)."""
import sqlite3
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))
import pipeline  # noqa: E402


def linha(**kw):
    base = {"id_venda": "1", "data_venda": "10/10/2026", "produto": " notebook ",
            "uf": "df", "quantidade": "2", "preco_unitario": "100,50"}
    base.update(kw)
    return base


class TestTransformar(unittest.TestCase):
    def test_linha_valida_e_normalizada(self):
        validas, rejeitadas = pipeline.transformar([linha()])
        self.assertEqual(rejeitadas, [])
        self.assertEqual(validas[0], (1, "2026-10-10", "Notebook", "DF", 2, 100.5, 201.0))

    def test_rejeita_data_invalida(self):
        _, rejeitadas = pipeline.transformar([linha(data_venda="31/02/2026")])
        self.assertEqual(len(rejeitadas), 1)

    def test_rejeita_quantidade_zero(self):
        _, rejeitadas = pipeline.transformar([linha(quantidade="0")])
        self.assertIn("inválido", rejeitadas[0]["motivo"])


class TestCarga(unittest.TestCase):
    def test_carga_e_view(self):
        validas, _ = pipeline.transformar([linha(), linha(id_venda="2", uf="sp")])
        with tempfile.TemporaryDirectory() as tmp:
            banco = Path(tmp) / "teste.db"
            pipeline.carregar(validas, banco)
            with sqlite3.connect(banco) as con:
                total = con.execute("SELECT COUNT(*) FROM fato_vendas").fetchone()[0]
                ufs = {uf for uf, _ in con.execute("SELECT * FROM vw_faturamento_uf")}
        self.assertEqual(total, 2)
        self.assertEqual(ufs, {"DF", "SP"})


if __name__ == "__main__":
    unittest.main()
