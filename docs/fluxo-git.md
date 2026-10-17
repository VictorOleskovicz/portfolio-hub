# Fluxo de trabalho com Git

## Ciclo básico

```
Working Directory ──git add──► Staging Area ──git commit──► Repositório local ──git push──► GitHub
                                                                   ◄──git pull──
```

## Branches

| Branch | Uso |
|---|---|
| `main` | Versão estável, publicada no GitHub Pages |
| `feature/<nome>` | Nova funcionalidade ou novo projeto |
| `fix/<nome>` | Correção |

Fluxo: criar a branch → commits → Pull Request → revisão → merge na `main`.

## Padrão de commits (Conventional Commits)

| Prefixo | Quando usar | Exemplo |
|---|---|---|
| `feat:` | Nova funcionalidade | `feat: adiciona projeto ETL de vendas` |
| `fix:` | Correção | `fix: corrige link do LinkedIn` |
| `docs:` | Documentação | `docs: detalha README do MaskSafe` |
| `style:` | Visual/formatação | `style: ajusta cores do site` |
| `chore:` | Manutenção | `chore: adiciona .gitignore` |

## Versionamento

Uso [SemVer](https://semver.org/lang/pt-BR/) com tags anotadas:

```bash
git tag -a v1.0 -m "Versão 1.0"
git push origin --tags
```

## Colaboração

- Toda mudança na `main` passa por Pull Request.
- Issues registram tarefas e bugs.
- Para contribuir em repositórios de terceiros: **fork → branch → PR**.
