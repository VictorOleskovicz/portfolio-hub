# SQLi Lab — Laboratório de SQL Injection

> Disciplina de Segurança de Dados — Ciência da Computação, UniCEUB (projeto em grupo)

⚠️ **Uso exclusivamente educacional, em ambiente controlado.**

## Objetivo

Demonstrar, em um ambiente de laboratório, como uma aplicação vulnerável a **SQL Injection** pode ser explorada e como corrigir a falha. O projeto se relaciona com duas categorias do **OWASP Top 10**:

- **A03 — Injection**
- **A08 — Software and Data Integrity Failures**

## Cenários demonstrados

1. **Extração de dados.** Uma entrada não tratada permite ler registros que o usuário não deveria acessar.
2. **Destruição de dados.** A mesma falha permite alterar ou apagar dados, o que compromete a integridade.

## Como prevenir

| Vulnerável | Seguro |
|---|---|
| Concatenar a entrada do usuário na query | **Consultas parametrizadas** (prepared statements) |
| Usuário do banco com permissão total | **Princípio do menor privilégio** |
| Sem validação de entrada | **Validação e sanitização** no backend |
| Erros SQL exibidos ao usuário | Mensagens genéricas + log interno |

Exemplo de correção (Python):

```python
# Vulnerável
cursor.execute(f"SELECT * FROM usuarios WHERE login = '{login}'")

# Seguro
cursor.execute("SELECT * FROM usuarios WHERE login = ?", (login,))
```

## Minha contribuição

Apresentação do **Bloco 3** da demonstração do grupo.

## Aprendizados

- Como funciona um ataque de injeção na prática
- Por que a parametrização resolve a causa raiz do problema
