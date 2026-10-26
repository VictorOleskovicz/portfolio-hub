"""
Verifica se os links internos do site (index.html) e dos arquivos Markdown
apontam para arquivos/pastas que existem no repositório.

Uso: python scripts/check_links.py   (sai com código 1 se houver link quebrado)
"""
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
PADROES = {
    ".html": re.compile(r'(?:href|src)="([^"]+)"'),
    ".md": re.compile(r"\]\(([^)\s]+)\)"),
}
IGNORAR = ("http://", "https://", "mailto:", "#", "tel:")


def links_quebrados() -> list[str]:
    erros = []
    for arquivo in sorted(RAIZ.rglob("*")):
        if ".git" in arquivo.parts or arquivo.suffix not in PADROES:
            continue
        texto = arquivo.read_text(encoding="utf-8")
        for alvo in PADROES[arquivo.suffix].findall(texto):
            if alvo.startswith(IGNORAR):
                continue
            caminho = (arquivo.parent / alvo.split("#")[0]).resolve()
            if not caminho.exists():
                erros.append(f"{arquivo.relative_to(RAIZ)} -> {alvo}")
    return erros


if __name__ == "__main__":
    erros = links_quebrados()
    for e in erros:
        print(f"LINK QUEBRADO: {e}")
    print(f"{len(erros)} link(s) quebrado(s).")
    sys.exit(1 if erros else 0)
