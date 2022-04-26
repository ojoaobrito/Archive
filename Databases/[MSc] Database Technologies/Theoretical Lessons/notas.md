# Tipos de índices (usando BTREEs):
## **Simples**:
Útil quando pretendemos fazer queries que usam apenas 1 campo

***exemplo:*** **CREATE INDEX** idx_tabela_campo **ON** tabela **USING BTREE** (campo);

## **Composto**:
Útil quando pretendemos fazer queries que usam mais que 1 campo

***exemplo:*** **CREATE INDEX** idx_tabela_campo1_campo2 **ON** tabela **USING BTREE** (campo1,campo2);

## **Parcial**:
Útil quando pretendemos fazer queries que têm condições sobre os campos (em vez de termos a informação toda, temos apenas aquela que respeita as condições)

***exemplo:*** **CREATE INDEX** idx_tabela_campo **ON** tabela **USING BTREE** (campo) **WHERE** campo>1000 **AND** campo<2000;

# Tipos de índices (usando hashing):
Usados fundamentalmente para pesquisas por igualdade

***exemplo:*** **SELECT * FROM** pessoa **WHERE** idade=19;

**CREATE INDEX** idx_pessoa_idade **ON** pessoa **USING HASH** (idade);

**Tabela "pessoa"**
|num|  nome  | idade |
| - |:------:| -----:|
| 1 | Pedro  |   20  |
| 2 | Joana  |   19  |
| 3 | Carlos |   17  |

# Para o relatório (comparação de construção de índices)

| tipo  |  tempo inicial | tempo final | espaço ocupado | indice |
| ----- |:--------------:|:-----------:|:--------------:|:------:|
| BTREE |     3 min.     |   333 ms.   |     54 KB.     | 20 KB. |
| HASH  |     1 min.     |  **52 ms.** |    100 KB.     | 52 KB. |