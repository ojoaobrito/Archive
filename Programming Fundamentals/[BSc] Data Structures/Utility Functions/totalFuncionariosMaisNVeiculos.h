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

// CALCULAR O TOTAL DE FUNCIONÁRIOS QUE VERIFICARAM MAIS DE "N" VEÍCULOS
// ---------------------------------------------------------------------
int contaNos(Automovel *A){

    if(A==NULL)
        return(0);
    
    return(1+contaNos(A->fe)+contaNos(A->fd));
}

int totalFuncionariosMaisNVeiculos(Funcionario *F, int n){

    int total = 0;

    while(F!=NULL){

        if(contaNos(F->automoveis)>n)
            total++;
        
        F = F->nseg;
    }

    return(total);
}
// ---------------------------------------------------------------------
