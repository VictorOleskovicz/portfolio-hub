CREATE TABLE IF NOT EXISTS fato_vendas (
    id_venda       INTEGER PRIMARY KEY,
    data_venda     DATE    NOT NULL,
    produto        TEXT    NOT NULL,
    uf             CHAR(2) NOT NULL,
    quantidade     INTEGER NOT NULL CHECK (quantidade > 0),
    preco_unitario REAL    NOT NULL CHECK (preco_unitario >= 0),
    valor_total    REAL    NOT NULL
);

CREATE VIEW IF NOT EXISTS vw_faturamento_uf AS
SELECT uf, ROUND(SUM(valor_total), 2) AS faturamento
FROM fato_vendas
GROUP BY uf
ORDER BY faturamento DESC;
