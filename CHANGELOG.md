# Changelog

Formato baseado em [Keep a Changelog](https://keepachangelog.com/pt-BR/1.1.0/) e [SemVer](https://semver.org/lang/pt-BR/).

## [1.2] — 2026-10-26
### Adicionado
- Plano de implantação guiado pelo Google Gemini (`docs/plano-implantacao.md`, `docs/gemini-guia.md`)
- Segurança: `SECURITY.md`, `.github/CODEOWNERS`, `.github/dependabot.yml`, documentação em `docs/seguranca-e-acessos.md`
- Colaboração: `CONTRIBUTING.md` e template de Pull Request
- CI no GitHub Actions: testes unitários do pipeline ETL, execução ponta a ponta e verificação de links
- Metatags Open Graph no site

### Alterado
- `.gitignore` passa a bloquear `.env`, chaves e logs
- Ruleset na `main`: PR e CI obrigatórios, sem *force push*

## [1.1] — 2026-10-17
### Adicionado
- Projeto pessoal **ETL Vendas** (Python + SQLite)
- Documentação do fluxo Git em `docs/fluxo-git.md`
- Roteiro da apresentação em `apresentacao/`

### Alterado
- Site: nova seção de projetos com cards e links

## [1.0] — 2026-10-17
### Adicionado
- Estrutura inicial do repositório (`academicos/`, `pessoais/`, `docs/`)
- READMEs dos projetos MaskSafe, Treinu e SQLi Lab
- Página inicial no GitHub Pages (`index.html`)
