# Uso do Google Gemini como guia da implantação

O Gemini (conta institucional UniCEUB, Google Workspace for Education) foi usado como guia em duas consultas.
Conversa: "Plano de Implantação PortfolioHUB", 26/10/2026.

## Consulta 1 — Plano de implantação

**Prompt (resumo):** montar um plano de implantação em fases (planejamento, integração com GitHub, gestão de usuários e segurança, compartilhamento e controle de acesso, finalização e testes, revisão), com entregáveis e critério de pronto.

**O que o Gemini recomendou e o que foi aplicado:**

| Recomendação do Gemini | Aplicado? |
|---|---|
| Publicar pelo GitHub Pages a partir da `main`, pasta raiz | ✅ já publicado |
| Branch protection na `main`, exigir PR e bloquear *force push* | ✅ ruleset `protecao-main` |
| Metatags Open Graph para pré-visualização ao compartilhar o link | ✅ `index.html` |
| Varredura de links quebrados e teste de responsividade | ✅ `scripts/check_links.py` no CI |
| Atualizar README, About do repositório e CHANGELOG | ✅ v1.2 |
| Domínio personalizado | ⏭️ não aplicado (sem domínio próprio) |

## Consulta 2 — Políticas de segurança e gestão de usuários

**Prompt (resumo):** políticas recomendadas (OWASP/GitHub) para um repositório público pessoal: 2FA, ruleset, CODEOWNERS, SECURITY.md, Dependabot, secret scanning, private vulnerability reporting, permissões de colaboradores e `.gitignore`.

| Recomendação do Gemini | Onde está |
|---|---|
| 2FA na conta | Configuração da conta |
| Ruleset: PR obrigatório, *status checks*, bloquear *force push* | Settings → Rules |
| `CODEOWNERS` com `* @VictorOleskovicz` | `.github/CODEOWNERS` |
| `SECURITY.md` com canal de reporte | `SECURITY.md` |
| Dependabot (alertas + atualizações) | Settings → Advanced Security + `.github/dependabot.yml` |
| Secret scanning + push protection | Settings → Advanced Security |
| Private vulnerability reporting | Settings → Advanced Security |
| Menor privilégio para colaboradores | [seguranca-e-acessos.md](seguranca-e-acessos.md) |
| `.gitignore` com `.env`, `venv/`, `*.log` | `.gitignore` |

> O Gemini pode errar: cada recomendação foi conferida na documentação do GitHub antes de ser aplicada.
