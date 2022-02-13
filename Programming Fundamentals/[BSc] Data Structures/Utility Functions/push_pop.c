#include <stdio.h>
#include <stdlib.h>

typedef struct QUEUE{
	
	char ID;
	struct QUEUE *nseg;

}Queue;

Queue* pop(Queue **Q){

	Queue *aux = *Q;

	*Q = (*Q)->nseg;
	aux -> nseg = NULL;

	return(aux);
}

Queue* push(Queue *Q, Queue *nv){

	Queue *aux = Q;

	if(Q==NULL)
		return(nv);

	while(Q->nseg!=NULL)
		Q = Q->nseg;

	Q->nseg = nv;

	return(aux);
}

Queue* funcaoEstranha(Queue *F){

	Queue *aux = NULL;
	Queue *nv = NULL;

	while(F!=NULL){

		aux=pop(&F);

		if((aux->ID=='a') || (aux->ID=='e') || (aux->ID=='i'))
			nv = push(nv,aux);

		else
			nv = push(aux,nv);
	}

	return(nv);
}

int main(){

	Queue *Q = NULL;

	Q = (Queue*)malloc(sizeof(Queue));
	Q->ID = 'a';
	Q->nseg = (Queue*)malloc(sizeof(Queue));
	Q->nseg->ID = 'b';
	Q->nseg->nseg = (Queue*)malloc(sizeof(Queue));
	Q->nseg->nseg->ID = 'i';
	Q->nseg->nseg->nseg = (Queue*)malloc(sizeof(Queue));
	Q->nseg->nseg->nseg->ID = 'e';
	Q->nseg->nseg->nseg->nseg = (Queue*)malloc(sizeof(Queue));
	Q->nseg->nseg->nseg->nseg->ID = 'o';
	Q->nseg->nseg->nseg->nseg->nseg = (Queue*)malloc(sizeof(Queue));
	Q->nseg->nseg->nseg->nseg->nseg->ID = 'u';
	Q->nseg->nseg->nseg->nseg->nseg->nseg = NULL;

	Q = funcaoEstranha(Q);

	printf("Q: ");

	while(Q!=NULL){

		printf("%c -> ",Q->ID);
		Q = Q -> nseg;

		if((Q->nseg)==NULL){

			printf("%c\n",Q->ID);
			break;
		}
	}

	return(0);
}