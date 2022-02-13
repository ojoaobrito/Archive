#include <stdio.h>
#include <stdlib.h>

typedef struct NODO
{
    int destino, custo;
    struct NODO *nseg;

} Nodo;

// ESCOLHER O NÓ (CIDADE) DO GRAFO QUE TEM MAIS VIZINHOS NUM RAIO DE "N" QUILÓMETROS
// ------------------------------------------------------------------------------------------------------------------------------------------
int contaCidades(Nodo *L, int custo){ // função auxiliar, conta o número de cidades vizinhas que uma cidade tem (num raio de "N" quilómetros)

    int contador = 0;

    while(L!=NULL){

        if(L->custo<custo)
            contador++;
    }

    return(contador);
}

void encontraSede(Nodo **G, int tv, int N){

    int i=0, aux = 0, id_cidade = 0;
    Nodo *ideal = NULL;

    for(i=0; i<tv; i++){

        aux = contaCidades(G[i],N);

        if(ideal==NULL || aux > (ideal->custo)){ // cidade melhor que a atual "ideal"
        
            ideal = G[i];
            id_cidade = i + 1;
        }
    }

    printf("Melhor %d\n",id_cidade);
}
// ------------------------------------------------------------------------------------------------------------------------------------------
