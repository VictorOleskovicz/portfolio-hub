# Como contribuir

1. Faça um **fork** (ou crie uma branch, se for colaborador): `feature/<nome>` ou `fix/<nome>`.
2. Faça commits pequenos seguindo o [padrão de commits](docs/fluxo-git.md#padrão-de-commits-conventional-commits).
3. Rode os testes localmente:
   ```bash
   python -m unittest discover -s pessoais/etl-vendas/tests -v
   python scripts/check_links.py
   ```
4. Abra um **Pull Request** para a `main` preenchendo o template.
5. O PR só é integrado quando o **CI passa** (regra da `main`); o code owner revisa antes do merge.

Nunca envie senhas, tokens ou arquivos `.env`. Falhas de segurança: veja [SECURITY.md](SECURITY.md).
