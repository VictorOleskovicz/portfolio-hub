# PortfolioHUB — Victor Oleskovicz

> Repositório central do meu portfólio: projetos acadêmicos e pessoais, versionados com Git e publicados com GitHub Pages.

[![GitHub Pages](https://img.shields.io/badge/site-GitHub%20Pages-222?logo=github)](https://victoroleskovicz.github.io/portfolio-hub/)
[![Versão](https://img.shields.io/badge/versão-1.2-blue)](CHANGELOG.md)
[![CI](https://github.com/VictorOleskovicz/portfolio-hub/actions/workflows/ci.yml/badge.svg)](https://github.com/VictorOleskovicz/portfolio-hub/actions/workflows/ci.yml)
[![Licença](https://img.shields.io/badge/licença-MIT-green)](LICENSE)

**Site:** https://victoroleskovicz.github.io/portfolio-hub/
**LinkedIn:** https://www.linkedin.com/in/victoroleskovicz

---

## Sobre mim

Sou engenheiro de dados júnior na First Decision e estou no 8º semestre de Ciência da Computação no UniCEUB, em Brasília. No trabalho, atuo em migrações de dados SAP de grande porte: pipelines ETL com SAP Data Services, planejamento de cutover e cargas delta.

## Estrutura do repositório

```
portfolio-hub/
├── index.html               # Página do GitHub Pages
├── assets/                  # CSS do site
├── academicos/              # Projetos da graduação
│   ├── masksafe/            # Mascaramento de dados sensíveis (PI III)
│   ├── treinu-pi-iv/        # Treinu — Projeto Integrador IV
│   └── sqli-lab/            # Laboratório de SQL Injection (Segurança de Dados)
├── pessoais/                # Projetos pessoais
│   └── etl-vendas/          # Pipeline ETL em Python + SQLite
├── docs/                    # Plano de implantação, Gemini, segurança, fluxo Git
├── scripts/                 # Verificação de links (usada no CI)
├── .github/                 # CI, CODEOWNERS, Dependabot, template de PR
├── SECURITY.md              # Política de segurança
├── CONTRIBUTING.md          # Como contribuir
├── apresentacao/            # Roteiro do vídeo de apresentação
├── CHANGELOG.md             # Histórico de versões
└── LICENSE
```

## Projetos

| Projeto | Tipo | Tecnologias | Descrição |
|---|---|---|---|
| [MaskSafe](academicos/masksafe/) | Acadêmico | Backend, banco de dados | Sistema para mascarar dados sensíveis (LGPD) |
| [Treinu](academicos/treinu-pi-iv/) | Acadêmico | GitHub Projects, Scrum | Projeto Integrador IV, organizado em sprints |
| [SQLi Lab](academicos/sqli-lab/) | Acadêmico | SQL, OWASP | Laboratório de SQL Injection (OWASP A03/A08) |
| [ETL Vendas](pessoais/etl-vendas/) | Pessoal | Python, SQLite, SQL | Pipeline extract → transform → load com validações |

## Versionamento

O repositório segue [versionamento semântico](https://semver.org/lang/pt-BR/) e usa tags Git (`v1.0`, `v1.1`, ...). O histórico está no [CHANGELOG](CHANGELOG.md), e o fluxo de trabalho está em [docs/fluxo-git.md](docs/fluxo-git.md).

## Implantação, segurança e colaboração

- [Plano de implantação](docs/plano-implantacao.md) — 6 fases, montado com o Google Gemini ([como o Gemini foi usado](docs/gemini-guia.md))
- [Segurança e controle de acesso](docs/seguranca-e-acessos.md) — ruleset na `main`, papéis de colaboradores, Dependabot, secret scanning
- [Política de segurança](SECURITY.md) e [como contribuir](CONTRIBUTING.md)
- **CI:** todo PR roda os testes do pipeline ETL e a verificação de links antes do merge

## Contato

- GitHub: [@VictorOleskovicz](https://github.com/VictorOleskovicz)
- LinkedIn: [victoroleskovicz](https://www.linkedin.com/in/victoroleskovicz)
