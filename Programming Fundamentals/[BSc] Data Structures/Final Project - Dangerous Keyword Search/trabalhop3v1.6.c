#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <limits.h>

typedef struct NODO_AB{

	char a; //carater do nó, proveniente da mensagem dos terroristas
	long int *b; //vetor com as posições, na mensagem dos terroristas, do carater do nó
	long int size; //tamanho do vetor com as posições
	struct NODO_AB *fe; //filho esquerdo do nó
	struct NODO_AB *fd; //filho direito do nó

}Nodo_AB;


Nodo_AB* cleanTree(Nodo_AB *A){ //função auxiliar (limpa a árvore e prepara-a para as próximas mensagens)

	if(A==NULL){

		return(NULL);
	}

	A->size=0;
	free(A->b);
	A->b=NULL;
	A->fe=cleanTree(A->fe);
	A->fd=cleanTree(A->fd);

	return(A);
}


int countNodes(Nodo_AB *A){ //função auxiliar (conta os nós da árvore)

	if(A==NULL){

		return(0);
	}

	return(1+countNodes(A->fd)+countNodes(A->fe));
}


Nodo_AB* findNode(Nodo_AB *A, char c){ //função auxiliar (procura nós com o carater c na árvore)

	if(A==NULL){

		return(NULL);
	}

	if((A->a)==c){

		return(A);
	}

	if((int)(A->a)<(int)c){

		return(findNode(A->fd,c));
	}

	return(findNode(A->fe,c));
}


long int* findPosition(Nodo_AB *A, char c){ //função auxiliar (procura nós com o carater c na árvore)

	if(A==NULL){

		return(NULL);
	}

	if((A->a)==c){

		return(A->b);
	}

	if((int)(A->a)<(int)c){

		return(findPosition(A->fd,c));
	}

	return(findPosition(A->fe,c));
}


void results(Nodo_AB *A, char *v, int n){ //função final

	int b=0, c=0, m=1, d=1, e=0; //variáveis auxiliares
	long int j=0, i=1, espacamento=0, k=0, *aux=NULL, **aux2=NULL, a=0, f=0, teste=0, *tamanho=NULL; //variáveis principais (espaçamento, próximo carater,...)

	do{
		if(v[i]!='\n'){

			tamanho=(long int*)realloc(tamanho,(i)*sizeof(long int));
			tamanho[i-1]=((findNode(A,v[i]))->size);
		}

		i++;

	}while(v[i]!=EOF);

	i=-1;

	do{

		i++;
	
	}while(v[i+1]!='\n');

	aux2=(long int**)malloc((i+1)*sizeof(long int*));

	for(j=0; j<(i+1); j++){

		aux2[j]=(long int*)findPosition(A,v[j]);
	}

	i=0;

	f=(findNode(A,v[c])->size);

		for(j=0; j<f; j++){ //percorrer todas as ocorrências numa mensagem da primeira letra de cada keyword

			teste++;

			if(d==1){

				aux=findPosition(A,v[c]);
				f=(findNode(A,v[c])->size);
				d=0;
			}

			if(v[i+1]!='\n' && v[i+1]!=EOF){

				if(a<tamanho[i]){

					k=(aux2[e+1][a]);

					if(espacamento==0){ //caso inicial

						if((k-aux[j])>0){

							espacamento=(k-aux[j]);
							i++;
							e++;
							j--;
							a=0;
						}

						else{

							a++;
							j--;
						}
					}						

					else if((k-(aux[j]+((i-c)*espacamento)))==espacamento){ //caso ideal

						i++;
						e++;
						j--;
						a=0;
					}

					else if((k-(aux[j]+((i-c)*espacamento)))<espacamento){ //caso em que o espaçamento é curto, mas pode haver uma ocorrência à frente que satisfaça o espaçamento definido

						j--;
						a++;
					}

					else{ //caso em que o espaçamento é demasiado grande

						i=c;
						e=0;
						a++;
						j--;
						espacamento=0;			
					}

				}

				else{ //sempre que não há mais letras para uma dada palavra

					if(j==(f-1)){ //próxima keyword

						do{
							i++;

						}while(v[i-1]!='\n');

						b=i;
						c=i;
						j=-1;
						a=0;
						espacamento=0;
						d=1;
						e=0;

						free(aux2);

						i=b;

						do{

							i++;
	
						}while(v[i+1]!='\n');

						aux2=(long int**)malloc(((i-b)+1)*sizeof(long int*));

						for(j=0; j<((i-b)+1); j++){

						aux2[j]=(long int*)findPosition(A,v[j+b]);

						}

						j=-1;
						i=b;

						if(v[i]==EOF){

							printf("\n");
							printf("O ciclo \"for\" foi executado %ld vezes.",teste);
							return;
						}

						f=(findNode(A,v[c])->size);
					}

					else{ //reset das variáveis auxiliares

						a=0;
						i=c;
						e=0;
						b=c;
						espacamento=0;
						continue;
					}
				}

			}

			else{ //imprimir no ecrã os resultados

				if(v[i+1]=='\n'){

					if(m==1){

					printf("\n");
					printf("\n");
					printf(". MENSAGEM %d .\n",n);
					printf("---------------\n");
					}

					printf("\"");

					do{
						printf("%c",v[b]);
						b++;

					}while(v[b]!='\n');

					printf("\" aparece com espaçamento %ld (coluna %ld).\n",espacamento,aux[j]);

					m=0;

					if(j==(f-1)){ //próxima keyword

						do{
							i++;

						}while(v[i-1]!='\n');

						b=i;
						c=i;
						j=-1;
						a=0;
						espacamento=0;
						d=1;
						e=0;

						free(aux2);

						i=b;

						do{

							i++;
	
						}while(v[i+1]!='\n');

						aux2=(long int**)malloc(((i-b)+1)*sizeof(long int*));

						for(j=0; j<((i-b)+1); j++){

						aux2[j]=(long int*)findPosition(A,v[j+b]);

						}

						j=-1;
						i=b;

						if(v[i]==EOF){
							
							printf("\n");
							printf("O ciclo \"for\" foi executado %ld vezes.",teste);
							return;
						}

						f=(findNode(A,v[c])->size);
					}

					else{ //reset das variáveis auxiliares

						a=0;
						i=c;
						e=0;
						b=c;
						espacamento=0;
						continue;
					}

				}
			}

		}

	free(tamanho);
	free(aux2);
}


Nodo_AB* makeTree(){ //função que constrói a árvore para pesquisa dos carateres

	Nodo_AB *n, *A=NULL; //variável auxiliar e raiz da árvore

	n=(Nodo_AB*)malloc(sizeof(Nodo_AB));
	n->size=0;
	n->a='m';

	A=n; //raiz

	n=(Nodo_AB*)malloc(sizeof(Nodo_AB));
	n->size=0;
	n->a='f';
	A->fe=n;

	n=(Nodo_AB*)malloc(sizeof(Nodo_AB));
	n->size=0;
	n->a='t';
	A->fd=n;

	//lado esquerdo da árvore

	//parte do c

	n=(Nodo_AB*)malloc(sizeof(Nodo_AB));
	n->size=0;
	n->a='c';
	A->fe->fe=n; //c
	
	n=(Nodo_AB*)malloc(sizeof(Nodo_AB));
	n->size=0;
	n->a='d';
	A->fe->fe->fd=n; //d

	n=(Nodo_AB*)malloc(sizeof(Nodo_AB));
	n->size=0;
	n->a='e';
	A->fe->fe->fd->fd=n; //e

	A->fe->fe->fd->fe=NULL;

	n=(Nodo_AB*)malloc(sizeof(Nodo_AB));
	n->size=0;
	n->a='b';
	A->fe->fe->fe=n; //b

	n=(Nodo_AB*)malloc(sizeof(Nodo_AB));
	n->size=0;
	n->a='a';
	A->fe->fe->fe->fe=n; //a

	A->fe->fe->fe->fd=NULL;

	//parte do i

	n=(Nodo_AB*)malloc(sizeof(Nodo_AB));
	n->size=0;
	n->a='i';
	A->fe->fd=n; //i

	n=(Nodo_AB*)malloc(sizeof(Nodo_AB));
	n->size=0;
	n->a='k';
	A->fe->fd->fd=n; //k

	n=(Nodo_AB*)malloc(sizeof(Nodo_AB));
	n->size=0;
	n->a='l';
	A->fe->fd->fd->fd=n; //l

	n=(Nodo_AB*)malloc(sizeof(Nodo_AB));
	n->size=0;
	n->a='j';
	A->fe->fd->fd->fe=n; //j

	n=(Nodo_AB*)malloc(sizeof(Nodo_AB));
	n->size=0;
	n->a='h';
	A->fe->fd->fe=n; //h

	n=(Nodo_AB*)malloc(sizeof(Nodo_AB));
	n->size=0;
	n->a='g';
	A->fe->fd->fe->fe=n; //g

	A->fe->fd->fe->fd=NULL;

	//lado direito da árvore

	//parte do p

	n=(Nodo_AB*)malloc(sizeof(Nodo_AB));
	n->size=0;
	n->a='p';
	A->fd->fe=n; //p

	n=(Nodo_AB*)malloc(sizeof(Nodo_AB));
	n->size=0;
	n->a='r';
	A->fd->fe->fd=n; //r

	n=(Nodo_AB*)malloc(sizeof(Nodo_AB));
	n->size=0;
	n->a='s';
	A->fd->fe->fd->fd=n; //s

	n=(Nodo_AB*)malloc(sizeof(Nodo_AB));
	n->size=0;
	n->a='q';
	A->fd->fe->fd->fe=n; //q

	n=(Nodo_AB*)malloc(sizeof(Nodo_AB));
	n->size=0;
	n->a='o';
	A->fd->fe->fe=n; //o

	n=(Nodo_AB*)malloc(sizeof(Nodo_AB));
	n->size=0;
	n->a='n';
	A->fd->fe->fe->fe=n; //n

	A->fd->fe->fe->fd=NULL;

	//parte do w

	n=(Nodo_AB*)malloc(sizeof(Nodo_AB));
	n->size=0;
	n->a='w';
	A->fd->fd=n; //w

	n=(Nodo_AB*)malloc(sizeof(Nodo_AB));
	n->size=0;
	n->a='y';
	A->fd->fd->fd=n; //y

	n=(Nodo_AB*)malloc(sizeof(Nodo_AB));
	n->size=0;
	n->a='z';
	A->fd->fd->fd->fd=n; //z

	n=(Nodo_AB*)malloc(sizeof(Nodo_AB));
	n->size=0;
	n->a='x';
	A->fd->fd->fd->fe=n; //x

	n=(Nodo_AB*)malloc(sizeof(Nodo_AB));
	n->size=0;
	n->a='v';
	A->fd->fd->fe=n; //v

	n=(Nodo_AB*)malloc(sizeof(Nodo_AB));
	n->size=0;
	n->a='u';
	A->fd->fd->fe->fe=n; //u

	A->fd->fd->fe->fd=NULL;

	return(A);
}


void readMessages(){ //função que abre as mensagens e chama as demais funções

	FILE *f=NULL, *g=NULL; //apontadores para o ficheiro das mensagens e das keywords
	Nodo_AB *A=NULL, *nv=NULL; //raiz da árvore e variável auxiliar
	clock_t t; //variável para calcular o tempo de execução
	double tempo; //variável para calcular o tempo de execução
	int j=0, comp=0; //ID das mensagens e tamanho do vetor das keywords
	long int pos=1; //variável auxiliar
	char *v=NULL, e, a; //vetor com os carateres das keywords e carateres lidos 

	f=fopen("msgs.bin","r");

	if(f==NULL){

		printf("\n");
		printf("A abertura do ficheiro das mensagens falhou...\n");
		printf("\n");
		exit(0);
	}

	g=fopen("keywords.txt","r");

	if(g==NULL){

		printf("\n");
		printf("Ocorreu um erro inesperado...\n");
		printf("\n");
		exit(0);
	}	

	while(a!=EOF){

		a=fgetc(g);
		v=(char*)realloc(v,(++comp)*sizeof(char));
		v[comp-1]=a;
	}

	A=makeTree();

	printf("\n");
	printf("(Árvore construída)\n");

	while(e!=EOF){

		e=fgetc(f);

		if(e=='\n'){

			j++;
			pos=1;

			t=clock();

			results(A,v,j);

			A=cleanTree(A);

			t=clock()-t;
			printf("\n");
			tempo=((double)t)/CLOCKS_PER_SEC;
			printf("A mensagem %d demorou %.1lf segundos.\n",j,tempo);
		}

		else{

			nv=findNode(A,e);

			if(nv!=NULL){

				(nv->size)++;
				(nv->b)=(long int*)realloc((nv->b),(nv->size)*sizeof(long int));
				(nv->b)[(nv->size)-1]=pos;
				pos++;
			}

			else{

				pos++;

			}
		}
	}

	fclose(f);
	fclose(g);
	free(v);
	v=NULL;

}


void main(){ //função main

	clock_t t; //variável para calcular o tempo de execução
	double tempo; //variável para calcular o tempo de execução
	int controlo=0; //variável de controlo
	
	while(1){

		printf("\n");
		printf("___________CAÇA AO TERRORISTA v1.6___________\n");
		printf("\n");
		printf("1: Apanhar os terroristas\n");
		printf("2: Sair e deixá-los escapar\n");
		printf("\n");
	
		printf("> ");
		scanf("%d",&controlo);

		switch(controlo){

			case 1: printf("\n");
					printf("--------------------------------------------\n");
					printf("\n");
					printf("A carregar os resultados...\n");
					t=clock();
					readMessages();
					t=clock()-t;
					printf("\n");
					tempo=((double)t)/CLOCKS_PER_SEC;
					printf("\n");
					printf("A execução demorou %.1lf segundos.\n",tempo);
					printf("\n");
					printf("--------------------------------------------\n");
					break;

			case 2: printf("\n");
					printf("--------------------------------------------\n");
					printf("\n");
					printf("Os terroristas fugiram... Adeus :(\n");
					printf("\n");
					exit(0);
	
			default: printf("\n");
					 printf("ESCOLHA CORRETAMENTE UMA DAS OPÇÕES, POR FAVOR.\n");
					 printf("\n");
					 break;	

		}

	}

}