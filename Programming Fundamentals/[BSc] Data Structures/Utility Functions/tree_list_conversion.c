#include <stdio.h>
#include <stdlib.h>

typedef struct NODO{ // estrutura que representa cada nó na lista

    int ID;
    struct NODO *nseg;

} Nodo;

typedef struct NODOAB{ // estrutura que representa cada nó na árvore

    int ID;
    struct NODOAB *fe;
    struct NODOAB *fd;

} NodoAB;

NodoAB* arvore_2_lista(NodoAB *A){

    if(A==NULL)
        return NULL;

    NodoAB *temp = (arvore_2_lista(A->fe));

    if(temp!=NULL){

        while(temp->fd!=NULL){ // ir para o último elemento
            temp = temp->fd;
        }

        temp->fd = A;
        temp->fd->fd = (arvore_2_lista(A->fd));

        // pôr tudo a NULL
        temp->fe = NULL;
        temp->fd->fe = NULL;
    }
    else
        temp = A;
        temp->fe = NULL;
        temp->fd = (arvore_2_lista(A->fd));

    return(temp);
}

Nodo* antepassado_aux(Nodo *A, Nodo *atual, Nodo *a, Nodo *b){

    Nodo *temp = NULL;

    if(A==NULL)
        return(NULL);


    if(a->ID<atual->ID)
        temp = antepassado(A,A->fe,a,b);

    else if(atual->ID==a->ID)
            return(getPai(A,a));

    else
        temp = antepassado(A,atual->fd,a,b);

    return(temp);
}

int maisFilhosAtivos(NodoAB *A){

    if(A==NULL || (A->fe==NULL && A->fd==NULL))
        return(0);

    if(A->fe!=NULL && A->fd==NULL)
        return(-1);

    if(A->fe==NULL && A->fd!=NULL)
        return(1);
}

int igualEstrutura(NodoAB *A1, NodoAB *A2){

    if(A1==NULL && A2!=NULL || A1!=NULL && A2==NULL) // caso em que diferem
        return(0);

    if(A1==A2 || A1->fe==NULL && A2->fe==NULL && A1->fd==NULL && A2->fd==NULL) // caso em que são iguais
        return(1);

    if(A1->fe!=NULL && A2->fe==NULL || A1->fe==NULL && A2->fe!=NULL || A1->fd!=NULL && A2->fd==NULL || A1->fd==NULL && A2->fd!=NULL) // casos em que diferem
        return(0);

    return((igualEstrutura(A1->fe, A2->fe)==igualEstrutura(A1->fd, A2->fd))?1:0);
}

int conta_nos(Nodo *L){

    if(L==NULL)
        return(0);

    return(1 + conta_nos(L->nseg));
}

void imprime_lista(Nodo *L){

    while(L!=NULL){

        printf("%d ",L->ID);
        L = L->nseg;
    }
}

void imprime_lista_arvore(NodoAB *L){

    while(L!=NULL){

        printf("%d ",L->ID);
        L = L->fd;
    }
}

void imprime_arvore(NodoAB *A){

    if(A==NULL)
        return;

    printf("Filhos do %d: ", A->ID);
    if((A->fe)!=NULL)
        printf("%d ", A->fe->ID);
    if((A->fd)!=NULL)
        printf("%d ", A->fd->ID);
    printf("\n");

    imprime_arvore(A->fe);
    imprime_arvore(A->fd);
}

Nodo** adiciona_a_lista(Nodo **L, NodoAB *novo){

    // converter o nó que entrou (que é do tipo NodoAB) num nó de tipo Nodo (usados nas listas)
    Nodo *novo_lista = (Nodo*) malloc(sizeof(Nodo));
    novo_lista->ID = novo->ID;
    novo_lista->nseg = NULL;

    Nodo *aux = *L;

    if(aux==NULL){ // não há nada na lista ainda

        *L = novo_lista;
        return(L);
    }

    while((aux->nseg)!=NULL) // chegar ao último elemento da lista
        aux = aux->nseg;
        
    aux->nseg = novo_lista; // inserir o novo elemento na lista (na última posição)
    return(L);
}

void tree_to_list(NodoAB *A, Nodo **L){ // função que transforma a árvore dada por A numa lista

    if((A->fe)!=NULL)
        tree_to_list(A->fe,L); // vamos para a esquerda

    L = adiciona_a_lista(L,A); // guardar o nó atual

    if(A->fd!=NULL)
        tree_to_list(A->fd,L); // vamos para a direita
}

void list_to_tree(NodoAB **A, Nodo *L, int tamanho){ // função que transforma a árvore dada por A numa lista

    int aux = 1;
    Nodo *L_aux = L;

    if(tamanho==0) // não há nada a fazer
        return;

    if(tamanho!=1){ // se o tamanho for 1, o elemento já está escolhido

        while(aux<(tamanho/2)){ // obter o elemento do meio

            L = L->nseg;
            aux++;
        }
    }

    (*A) = (NodoAB*) malloc(sizeof(NodoAB));
    (*A)->ID = L->ID;

    // continuar para a esquerda e a direita
    list_to_tree(&((*A)->fe),L_aux,aux-1);
    list_to_tree(&((*A)->fd),L->nseg,tamanho-aux);
}

int main(int argc, char **argv){
    
    NodoAB *A = NULL, *B = NULL, *C = NULL, *D = NULL; // raiz da nossa árvore
    Nodo *L = NULL; // cabeça da nossa lista

    // a árvore de teste será assim:
    //                         __
    //                         10
    //             |                        |
    //             4                        14
    //      |             |           |            |
    //      2             5           13           18
    //  |       |                                        | 
    //  1       3                                        19

    // construir a árvore de teste
    A = (NodoAB*) malloc(sizeof(NodoAB));
    A->ID = 10;

    // filhos da raiz
    A->fe = (NodoAB*) malloc(sizeof(NodoAB));
    A->fe->ID = 4;

    A->fd = (NodoAB*) malloc(sizeof(NodoAB));
    A->fd->ID = 14;

    // LADO ESQUERDO DA ÁRVORE
    // ----------------------------------------------
    // filhos do nó 4
    A->fe->fe = (NodoAB*) malloc(sizeof(NodoAB));
    A->fe->fe->ID = 2;

    A->fe->fd = (NodoAB*) malloc(sizeof(NodoAB));
    A->fe->fd->ID = 5;

    // filhos do nó 2
    A->fe->fe->fe = (NodoAB*) malloc(sizeof(NodoAB));
    A->fe->fe->fe->ID = 1;

    A->fe->fe->fd = (NodoAB*) malloc(sizeof(NodoAB));
    A->fe->fe->fd->ID = 3;

    // filhos do nó 5
    A->fe->fd->fe = NULL;
    A->fe->fd->fd = NULL;

    // filhos do nó 1
    A->fe->fe->fe->fe = NULL;
    A->fe->fe->fe->fd = NULL;

    // filhos do nó 3
    A->fe->fe->fd->fe = NULL;
    A->fe->fe->fd->fd = NULL;
    // ----------------------------------------------

    // LADO DIREITO DA ÁRVORE
    // ----------------------------------------------
    // filhos do nó 14
    A->fd->fe = (NodoAB*) malloc(sizeof(NodoAB));
    A->fd->fe->ID = 13;

    A->fd->fd = (NodoAB*) malloc(sizeof(NodoAB));
    A->fd->fd->ID = 18;

    // filhos do nó 13
    A->fd->fe->fe = NULL;
    A->fd->fe->fd = NULL;

    // filhos do nó 18
    A->fd->fd->fd = (NodoAB*) malloc(sizeof(NodoAB));
    A->fd->fd->fd->ID = 19;

    A->fd->fd->fe = NULL;

    // filhos do nó 19
    A->fd->fd->fd->fe = NULL;
    A->fd->fd->fd->fe = NULL;
    // ----------------------------------------------

    // construir a árvore de teste
    C = (NodoAB*) malloc(sizeof(NodoAB));
    C->ID = 10;

    // filhos da raiz
    C->fe = (NodoAB*) malloc(sizeof(NodoAB));
    C->fe->ID = 4;

    C->fd = (NodoAB*) malloc(sizeof(NodoAB));
    C->fd->ID = 14;

    // LADO ESQUERDO DA ÁRVORE
    // ----------------------------------------------
    // filhos do nó 4
    C->fe->fe = (NodoAB*) malloc(sizeof(NodoAB));
    C->fe->fe->ID = 2;

    C->fe->fd = (NodoAB*) malloc(sizeof(NodoAB));
    C->fe->fd->ID = 5;

    // filhos do nó 2
    C->fe->fe->fe = (NodoAB*) malloc(sizeof(NodoAB));
    C->fe->fe->fe->ID = 1;

    C->fe->fe->fd = (NodoAB*) malloc(sizeof(NodoAB));
    C->fe->fe->fd->ID = 3;

    // filhos do nó 5
    C->fe->fd->fe = NULL;
    C->fe->fd->fd = NULL;

    // filhos do nó 1
    C->fe->fe->fe->fe = NULL;
    C->fe->fe->fe->fd = NULL;

    // filhos do nó 3
    C->fe->fe->fd->fe = NULL;
    C->fe->fe->fd->fd = NULL;
    // ----------------------------------------------

    // LADO DIREITO DA ÁRVORE
    // ----------------------------------------------
    // filhos do nó 14
    C->fd->fe = (NodoAB*) malloc(sizeof(NodoAB));
    C->fd->fe->ID = 13;

    C->fd->fd = (NodoAB*) malloc(sizeof(NodoAB));
    C->fd->fd->ID = 18;

    // filhos do nó 13
    C->fd->fe->fe = NULL;
    C->fd->fe->fd = NULL;

    // filhos do nó 18
    C->fd->fd->fd = (NodoAB*) malloc(sizeof(NodoAB));
    C->fd->fd->fd->ID = 19;

    C->fd->fd->fe = NULL;

    // filhos do nó 19
    C->fd->fd->fd->fe = NULL;
    C->fd->fd->fd->fe = NULL;
    // ----------------------------------------------
    
    //printf("Árvore A em forma de lista:\n");
    //tree_to_list(A,&L);
    //imprime_lista(L);
    //printf("\n\n");
    //printf("Lista L em forma de árvore:\n");
    //list_to_tree(&B,L,conta_nos(L));
    //imprime_arvore(C);
    //printf("%d\n",igualEstrutura(A,C));

    D = arvore_2_lista(A);
    imprime_lista_arvore(D);

    return(0);
}