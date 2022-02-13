#include <stdio.h>
#include <stdlib.h>

typedef struct AUTOMOVEL
{
    int BI;
    
    struct AUTOMOVEL *fd;
    struct AUTOMOVEL *fe;

} Automovel;

typedef struct FUNCIONARIO
{
    int BI;
    Automovel *automoveis;
    struct FUNCIONARIO *nseg;

} Funcionario;

// REMOVER FUNCIONÁRIO DA LISTA
// ---------------------------------------------------------------------------------
void apagaArvore(Automovel *A){ // função auxiliar, apaga uma árvore binária

    if(A==NULL)
        return(NULL);
    
    if(A->fe!=NULL)
        apagaArvore(A->fe);

    if(A->fd!=NULL)
        apagaArvore(A->fd);

    free(A);
}

Funcionario* removeFuncionario(Funcionario *L, int BI){

    Funcionario *aux = L, *aux2 = L;

    if(L==NULL || L->BI==BI){ // caso em que a lista está vazia ou só tem 1 elemento

        free(L);
        return(NULL);
    }

    aux2 = L->nseg;

    while(aux2!=NULL){

        if(aux2->BI == BI){

            apagaArvore(aux2->automoveis);
            aux->nseg = aux2->nseg;
            free(aux2);
        }

        aux2 = aux2->nseg;
        aux = aux->nseg;
    }

    return(L);
}
// ---------------------------------------------------------------------------------