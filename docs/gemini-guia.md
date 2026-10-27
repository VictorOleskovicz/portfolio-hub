# Uso do Google Gemini como guia da implantação

Usei o Gemini da minha conta institucional do UniCEUB como guia, em duas consultas.
Conversa: "Plano de Implantação PortfolioHUB", 26/10/2026.

## Consulta 1: plano de implantação

**Prompt (resumo):** montar um plano de implantação em fases (planejamento, integração com GitHub, gestão de usuários e segurança, compartilhamento e controle de acesso, finalização e testes, revisão), com entregáveis e critério de pronto.

**O que o Gemini recomendou e o que foi aplicado:**

| Recomendação do Gemini | Aplicado? |
|---|---|
| Publicar pelo GitHub Pages a partir da `main`, pasta raiz | Sim, já estava publicado |
| Branch protection na `main`, exigir PR e bloquear *force push* | Sim, ruleset `protecao-main` |
| Metatags Open Graph para pré-visualização ao compartilhar o link | Sim, no `index.html` |
| Varredura de links quebrados e teste de responsividade | Links: sim, `scripts/check_links.py` no CI. Responsividade: testada na largura de celular (375 px), sem rolagem horizontal |
| Atualizar README, About do repositório e CHANGELOG | README e CHANGELOG sim (v1.2); o About já descrevia o projeto |
| Domínio personalizado | Não, pois não tenho domínio próprio |

## Consulta 2: políticas de segurança e gestão de usuários

**Prompt (resumo):** políticas recomendadas (OWASP/GitHub) para um repositório público pessoal: 2FA, ruleset, CODEOWNERS, SECURITY.md, Dependabot, secret scanning, private vulnerability reporting, permissões de colaboradores e `.gitignore`.

| Recomendação do Gemini | Onde está |
|---|---|
| 2FA na conta | Passkey configurada; 2FA por app pendente |
| Ruleset: PR obrigatório, *status checks*, bloquear *force push* | Settings → Rules |
| `CODEOWNERS` com `* @VictorOleskovicz` | `.github/CODEOWNERS` |
| `SECURITY.md` com canal de reporte | `SECURITY.md` |
| Dependabot (alertas + atualizações) | Settings → Advanced Security + `.github/dependabot.yml` |
| Secret scanning + push protection | Settings → Advanced Security |
| Private vulnerability reporting | Settings → Advanced Security |
| Menor privilégio para colaboradores | [seguranca-e-acessos.md](seguranca-e-acessos.md) |
| `.gitignore` com `.env`, `venv/`, `*.log` | `.gitignore` |

> Como o Gemini pode errar, conferi cada recomendação na documentação do GitHub antes de aplicar.
