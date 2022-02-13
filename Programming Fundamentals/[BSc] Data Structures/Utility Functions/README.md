# README
**1.** Usar o ficheiro ***teste.c*** para testar as funções desejadas; \
**2.** Acrescentar, no ficheiro ***teste.c***, o excerto seguinte:

```c
#include "nome_da_funcao.h"
```
**NOTA:** se existirem estruturas definidas no ficheiro escolhido, colocar: 

```c
extern struct nome_da_estrutura;
```
**3.** Na função ***main()***, chamar as funções que se querem testar.

**NOTA:** se existirem **2 ficheiros que usem as mesmas estruturas**, testar **um de cada vez** (senão, existe conflito de definições e o programa não compila).