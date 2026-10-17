# ETL Vendas — Pipeline em Python + SQLite

> Projeto pessoal: um pipeline ETL completo, simples de rodar, que aplica os mesmos conceitos que uso em migrações de dados no trabalho.

## O que ele faz

```
data/vendas.csv  ──►  EXTRAIR  ──►  TRANSFORMAR  ──►  CARREGAR  ──►  data/vendas.db
                     (csv)        (validação,       (SQLite +
                                   padronização)     view analítica)
```

1. **Extract:** lê o CSV de vendas.
2. **Transform:**
   - converte datas `dd/mm/aaaa` para ISO (`aaaa-mm-dd`);
   - converte preços com vírgula decimal (`4500,00` → `4500.00`);
   - padroniza textos (produto em *Title Case*, UF em maiúsculas);
   - calcula `valor_total`;
   - **rejeita** registros inválidos (data inexistente, quantidade ≤ 0) e registra o motivo no log.
3. **Load:** grava a tabela `fato_vendas` (carga idempotente com `INSERT OR REPLACE`) e cria a view `vw_faturamento_uf`.

## Como executar

Requisito: Python 3.10+ (só biblioteca padrão, sem dependências).

```bash
cd pessoais/etl-vendas
python src/pipeline.py
```

Saída esperada:

```
[INFO] Extração: 8 linhas lidas de vendas.csv
[INFO] Transformação: 6 válidas, 2 rejeitadas
[WARNING] Rejeitada id=5: day is out of range for month
[WARNING] Rejeitada id=6: quantidade/preço inválido
[INFO] Carga: 6 registros na tabela fato_vendas

Faturamento por UF:
  DF: R$ 12,646.00
  SP: R$ 4,500.00
  RS: R$ 3,601.50
  GO: R$ 899.00
```

## Estrutura

```
etl-vendas/
├── data/vendas.csv     # Dados de entrada (fictícios)
├── sql/schema.sql      # DDL da tabela fato e da view
└── src/pipeline.py     # Pipeline ETL
```

## Conceitos aplicados

- Separação das etapas E, T e L em funções testáveis
- Qualidade de dados: validação e tratamento de rejeitados
- Carga idempotente (rodar duas vezes não duplica dados)
- Restrições no banco (`CHECK`, `NOT NULL`) como segunda camada de validação

## Próximos passos

- [ ] Testes automatizados com `pytest`
- [ ] Carga incremental (delta) por data
- [ ] Orquestração com Airflow
