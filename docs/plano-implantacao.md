# Plano de implantação do PortfolioHUB

Plano montado com o **Google Gemini** como guia (ver [gemini-guia.md](gemini-guia.md)) e executado em 17/10 e 26/10/2026.

| Fase | Atividades | Entregável | Critério de pronto | Status |
|---|---|---|---|---|
| 1. Planejamento | Definir estrutura (`academicos/`, `pessoais/`, `docs/`), projetos e padrão de commits; usar o Gemini para montar o plano | Este plano + estrutura do repositório | Estrutura criada e plano versionado | ✅ |
| 2. Configuração inicial e integração com GitHub | Criar o repositório `portfolio-hub`, publicar `index.html` no GitHub Pages (branch `main`, pasta raiz), integrar os projetos ao site | Site no ar: https://victoroleskovicz.github.io/portfolio-hub/ | URL pública abrindo o site com todos os projetos | ✅ |
| 3. Gestão de usuários e segurança | Passkey/2FA, ruleset na `main`, `CODEOWNERS`, `SECURITY.md`, Dependabot, secret scanning + push protection, private vulnerability reporting, `.gitignore` de segredos | Políticas aplicadas e documentadas em [seguranca-e-acessos.md](seguranca-e-acessos.md) | Push direto na `main` bloqueado; alertas de segurança ativos | ✅ (2FA por app pendente) |
| 4. Compartilhamento e controle de acesso | Repositório público, papéis de colaborador por menor privilégio, `CONTRIBUTING.md`, template de PR, metatags Open Graph para compartilhar o link | Fluxo fork/branch → PR → revisão → merge documentado | Mudança integrada por PR com CI verde | ✅ |
| 5. Finalização e testes | CI no GitHub Actions: testes unitários do pipeline, execução ponta a ponta e verificação de links; teste do site em produção | `.github/workflows/ci.yml` | CI verde na `main` e site sem links quebrados | ✅ |
| 6. Revisão e apresentação | CHANGELOG/tag `v1.2`, README atualizado, vídeo de 5 min no YouTube | Release `v1.2` + vídeo | Documentação atualizada e vídeo publicado | ✅ / vídeo pendente |

## Linha do tempo

- **17/10/2026** — v1.0 e v1.1: estrutura, projetos, site no GitHub Pages, fluxo Git, roteiro do vídeo.
- **26/10/2026** — v1.2: plano de implantação guiado pelo Gemini, segurança, gestão de acessos, CI e testes.
