# Segurança, gestão de usuários e controle de acesso

## 1. Conta

- Login com **passkey** configurada na conta `@VictorOleskovicz` (dono e único admin).
- **2FA por aplicativo autenticador: pendente** — próxima ação, recomendada pelo Gemini (Settings → Password and authentication → Enable 2FA).

## 2. Ruleset da branch `main` (`protecao-main`)

| Regra | Motivo |
|---|---|
| Restrict deletions | Ninguém apaga a branch publicada |
| Block force pushes | Histórico não pode ser reescrito |
| Require a pull request before merging | Nenhum commit direto: toda mudança passa por PR (o `CODEOWNERS` é chamado como revisor automaticamente; com mantenedor único, o número de aprovações fica em 0 — ao entrar um colaborador com Write, passa a 1) |
| Require status checks to pass (`Testes do pipeline ETL`, `Links do site e da documentação`) | Nada quebrado chega ao site |

## 3. Papéis de colaboradores (menor privilégio)

| Papel no GitHub | Quem recebe | Pode |
|---|---|---|
| Read | Professor / avaliador (repo é público, nem precisa de convite) | Ver código, abrir issues |
| Triage | Colega que ajuda a organizar issues | Rotular, fechar issues |
| Write | Colega de grupo que contribui com código | Criar branches e PRs (merge na `main` ainda exige PR + CI + aprovação) |
| Maintain | — (não usado) | Gerenciar o repo sem acesso a configurações sensíveis |
| Admin | Somente o dono | Tudo |

**Como convidar:** Settings → Collaborators → *Add people* → escolher o papel. Acesso é revisto ao fim de cada projeto.

## 4. Segurança do código (Settings → Advanced Security)

- **Dependabot alerts** e **security updates** ativos; `dependabot.yml` monitora GitHub Actions e o pipeline Python.
- **Secret scanning** + **push protection**: um push com token/senha é bloqueado.
- **Private vulnerability reporting**: canal sigiloso descrito no [SECURITY.md](../SECURITY.md).
- **CI com `permissions: contents: read`**: o workflow roda com o mínimo de permissão.

## 5. O que não é versionado

`.env`, `venv/`, `*.log`, chaves (`*.pem`, `*.key`) e os bancos gerados pelo pipeline (`*.db`) — ver `.gitignore`.

## 6. Fluxo de colaboração

```
branch feature/* ──commits──► Pull Request ──CI + revisão CODEOWNERS──► merge na main ──► GitHub Pages
```
