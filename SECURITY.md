# Política de Segurança

## Versões suportadas

| Versão | Suporte |
|---|---|
| 1.2 (atual) | ✅ |
| < 1.2 | ❌ |

## Como reportar uma vulnerabilidade

**Não abra uma Issue pública** para falhas de segurança.

Use o canal privado do GitHub: aba **Security → Report a vulnerability** neste repositório
(*Private vulnerability reporting*). Inclua:

- descrição da falha e impacto;
- passos para reproduzir;
- arquivo/URL afetado.

Prazo de resposta: até 5 dias úteis. Após a correção, o relato é creditado no CHANGELOG (se o autor quiser).

## Medidas adotadas neste repositório

- Ruleset na `main`: Pull Request obrigatório, CI obrigatório, bloqueio de *force push* e de exclusão.
- `CODEOWNERS`: o dono é solicitado como revisor em todo PR.
- Dependabot (alertas e atualizações de segurança) e `dependabot.yml`.
- *Secret scanning* com *push protection*.
- 2FA na conta do mantenedor.
- `.gitignore` bloqueando `.env`, bancos gerados e arquivos temporários.

Detalhes em [docs/seguranca-e-acessos.md](docs/seguranca-e-acessos.md).
