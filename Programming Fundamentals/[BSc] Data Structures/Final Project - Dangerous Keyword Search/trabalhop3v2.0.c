#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

typedef struct NODO_AB{ //elementos da árvore

	char a; //carater do nó, proveniente da mensagem dos terroristas
	long int *b; //vetor com as posições, na mensagem dos terroristas, do carater do nó
	long int size; //tamanho do vetor com as posições
	struct NODO_AB *fe; //filho esquerdo do nó
	struct NODO_AB *fd; //filho direito do nó

}Nodo_AB;

typedef struct CONTENT{ //keywords que casa mensagem tem

	char *p; //vetor com a keyword
	long int espacamento; //espaçamento com que essa keyword ocorre
	long int coluna; //coluna da primeira letra dessa keyword
	struct CONTENT *nseg; //nó seguinte

}Content;

typedef struct ORDEM{ //mensagens ordenadas

	int ID; //ID da mensagem
	int total; //total de keywords diferentes dessa mensagem
	Content *c; //lista com as keywords dessa mensagem
	struct ORDEM *nseg; //nó seguinte
	struct ORDEM *nant; //nó anterior

}Ordem;


void clearTree(Nodo_AB **A){ //função auxiliar (apaga uma árvore)

	if((*A)->fd!=NULL){

		clearTree(&((*A)->fd));
	}

	else if((*A)->fe!=NULL){

		clearTree(&((*A)->fe));
	}

	free(*A);

	return;
}


void clearList(Ordem **o){ //função auxiliar (apaga uma lista)

	Ordem *aux=(*o); //variável auxiliar

	while(aux!=NULL){

		aux=(aux->nseg);
		free(*o);
		(*o)=aux;
	}
}


Ordem* removeNode(Ordem *A, Ordem *r){ //função auxiliar (remove uma mensagem de uma lista de mensagens)

	if(A->nseg==NULL){

		free(A);
		return(NULL);
	}

	if(A==r){

		r=(A->nseg);
		r->nant=NULL;
		free(A);
		return(r);
	}

	if(r->nseg==NULL){

		r->nant->nseg=NULL;
		free(r);
		return(A);
	}

	r->nant->nseg=(r->nseg);
	r->nseg->nant=(r->nant);
	free(r);

	return(A);
}


Ordem* findMax(Ordem *A){ //função auxiliar (encontra a mensagem com mais keywords numa lista de mensagens)

	Ordem *max=A; //variável auxiliar

	if(A==NULL){

		return(A);
	}

	A=(A->nseg);

	while(A!=NULL){

		if((A->total)>(max->total)){

			max=A;
		}

		A=(A->nseg);
	}

	return(max);
}


Ordem* sortMessages(Ordem *o){ //função auxiliar (ordena as mensagens pelo total de keywords)

	Ordem* aux=NULL, *n=NULL, *temp=NULL; //variáveis auxiliares

	temp=findMax(o);

	n=(Ordem*)malloc(sizeof(Ordem));
	n->ID=(temp->ID);
	n->total=(temp->total);
	n->c=(temp->c);
	n->nseg=NULL;
	n->nant=NULL;

	aux=n;

	o=removeNode(o,temp);

	while(o!=NULL){

		temp=findMax(o);

		n->nseg=(Ordem*)malloc(sizeof(Ordem));
		n->nseg->ID=(temp->ID);
		n->nseg->total=(temp->total);
		n->nseg->c=(temp->c);
		n->nseg->nseg=NULL;
		n->nseg->nant=n;
		n=(n->nseg);

		o=removeNode(o,temp);
	}

	n=aux;

	return(n);
}


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


Ordem* results(Nodo_AB *A, Ordem *o, char *v, int n){ //função final

	Content *c=NULL;
	int b=0, m=2, d=1, k=0, f=0, p=0; //variáveis auxiliares
	long int j=0, i=0, espacamento=0, *aux=NULL, **aux2=NULL, *aux3=NULL, *tamanho=NULL; //variáveis principais (espaçamento, próximo carater,...)

	if(o!=NULL){

		while((o->nseg)!=NULL){

			o=(o->nseg);
		}

		o->nseg=(Ordem*)malloc(sizeof(Ordem));
		o->nseg->ID=n;
		o->nseg->total=0;
		o->nseg->c=NULL;
		o->nseg->nseg=NULL;
		o->nseg->nant=o;
		o=(o->nseg);
	}

	else{

		o=(Ordem*)malloc(sizeof(Ordem));
		o->ID=n;
		o->total=0;
		o->c=NULL;
		o->nseg=NULL;
		o->nant=NULL;
	}

	do{
		if(v[i]!='\n'){

			tamanho=(long int*)realloc(tamanho,(i+1)*sizeof(long int));
			tamanho[i]=((findNode(A,v[i]))->size);
		}

		i++;

	}while(v[i]!=EOF);

	i=-1;

	do{

		i++;

	}while(v[i+1]!='\n');

	aux=(long int*)malloc((i+1)*sizeof(long int));
	aux2=(long int**)malloc((i+1)*sizeof(long int*));
	d=(i+1);

	for(j=0; j<d; j++){

		aux2[j]=(long int*)findPosition(A,v[j]);
	}

	aux3=(long int*)malloc(d*sizeof(long int));

	for(i=0; i<d; i++){

		aux3[i]=0;
		aux[i]=0;
	}

	i=0;

	while(1){

		if(f==0 && p==0){

			if((aux2[1][aux3[1]]-aux2[0][aux3[0]])>0){

				espacamento=((aux2[1][aux3[1]])-(aux2[0][aux3[0]]));

				while(m<d){

					if((aux2[m][aux3[m]]-aux2[m-1][aux3[m-1]])<espacamento){

						aux3[m]++;

						if(aux3[m]>=tamanho[k+m]){

							f=1;
							p=0;
							m=2;
							break;
						}
					}

					else if((aux2[m][aux3[m]]-aux2[m-1][aux3[m-1]])>espacamento){

						aux3[1]++;

						if(aux3[1]>=tamanho[k+1]){

							f=1;
							p=0;
						}

						m=2;
						break;
					}

					else if((aux2[m][aux3[m]]-aux2[m-1][aux3[m-1]])==espacamento){

						m++;

						if(m==d){

							if(o->c!=NULL){

								while((o->c->nseg)!=NULL){

									o->c=(o->c->nseg);
								}

								o->c->nseg=(Content*)malloc(sizeof(Content));
								o->c->nseg->p=NULL;
								o->c->nseg->espacamento=0;
								o->c->nseg->coluna=0;
								o->c->nseg->nseg=NULL;
								o->c=(o->c->nseg);
							}

							else{

								o->c=(Content*)malloc(sizeof(Content));
								c=(o->c);
								o->c->p=NULL;
								o->c->espacamento=0;
								o->c->coluna=0;
								o->c->nseg=NULL;
							}

							o->c->p=(char*)malloc((d+1)*sizeof(char));

							while(v[b]!='\n' && v[b]!=EOF && v[b+1]!=EOF){

								o->c->p[b-k]=v[b];
								b++;
							}

							o->c->espacamento=espacamento;
							o->c->coluna=aux2[0][aux3[0]];
							(o->total)++;

							if(v[b]==EOF){

								p=1;
								f=0;
								m=2;
								break;
							}

							o->c->p[b-k]=(char)'\n';

							b=k;

							f=0;
							p=1;
							m=2;
							break;
						}

					}

				}
			}

			else{

				aux3[1]++;

				if(aux3[1]>=tamanho[k+1]){

					f=1;
					p=0;
					m=2;
				}
			}

		}

		else{

			if(f==1){

				aux3[0]++;

				if(aux3[0]>=tamanho[k]){

					p=1;
					f=0;
					m=2;
				}

				else{

					for(j=1; j<d; j++){

						while((aux2[j][aux[j]])<(aux2[0][aux3[0]])){

							aux[j]++;

							if(aux[j]>=tamanho[k+j]){

								p=1;
								f=0;
								m=2;
								break;
							}
						}

						if(p==1){

							break;
						}

						aux3[j]=aux[j];
					}

					if(p==0){

						f=0;
						m=2;
					}
				}
			}

			else if(p==1){ //próxima keyword

				while(v[i]!='\n' && v[i]!=EOF && v[i+1]!=EOF){

					i++;
				}

				if(v[i]==EOF || v[i+1]==EOF){

					free(tamanho);
					free(aux);
					free(aux2);
					free(aux3);

					printf(" TOTAL: %d\n",o->total);

					o->c=c;

					while((o->nant)!=NULL){

						o=(o->nant);
					}

					return(o);
				}

				i++;

				espacamento=0;
				k=i;
				b=i;

				do{
					i++;

				}while(v[i+1]!='\n');

				d=((i-b)+1);
				aux2=(long int**)realloc(aux2,d*sizeof(long int*));

				for(j=0; j<d; j++){

					aux2[j]=(long int*)findPosition(A,v[j+b]);

				}

				aux3=(long int*)realloc(aux3,d*sizeof(long int));
				aux=(long int*)realloc(aux,d*sizeof(long int));

				for(j=0; j<d; j++){

					aux3[j]=0;
					aux[j]=0;
				}

				f=0;
				p=0;
				m=2;
			}

		}

	}
}


Nodo_AB* makeTree(){ //função que constrói a árvore para pesquisa dos carateres

	//optou-se por construir a árvore deste modo para poupar tempo e garantir a árvore otimizada
	//se a árvore fosse construída pela máquina poderia não ficar tão boa e, claro, seria mais trabalho a realizar
	//assim é só alocar memória, e, neste problema, é uma solução que encaixa bem, afinal de contas são só 26 nós

	Nodo_AB *n, *A=NULL; //variável auxiliar e raiz da árvore

	n=(Nodo_AB*)malloc(sizeof(Nodo_AB));
	n->size=0;
	n->a='m';
	n->b=(long int*)malloc(sizeof(long int));

	A=n; //raiz

	n=(Nodo_AB*)malloc(sizeof(Nodo_AB));
	n->size=0;
	n->a='f';
	n->b=(long int*)malloc(sizeof(long int));
	A->fe=n;

	n=(Nodo_AB*)malloc(sizeof(Nodo_AB));
	n->size=0;
	n->a='t';
	n->b=(long int*)malloc(sizeof(long int));
	A->fd=n;

	//lado esquerdo da árvore

	//parte do c

	n=(Nodo_AB*)malloc(sizeof(Nodo_AB));
	n->size=0;
	n->a='c';
	n->b=(long int*)malloc(sizeof(long int));
	A->fe->fe=n; //c

	n=(Nodo_AB*)malloc(sizeof(Nodo_AB));
	n->size=0;
	n->a='d';
	n->b=(long int*)malloc(sizeof(long int));
	A->fe->fe->fd=n; //d

	n=(Nodo_AB*)malloc(sizeof(Nodo_AB));
	n->size=0;
	n->a='e';
	n->b=(long int*)malloc(sizeof(long int));
	A->fe->fe->fd->fd=n; //e

	A->fe->fe->fd->fe=NULL;

	n=(Nodo_AB*)malloc(sizeof(Nodo_AB));
	n->size=0;
	n->a='b';
	n->b=(long int*)malloc(sizeof(long int));
	A->fe->fe->fe=n; //b

	n=(Nodo_AB*)malloc(sizeof(Nodo_AB));
	n->size=0;
	n->a='a';
	n->b=(long int*)malloc(sizeof(long int));
	A->fe->fe->fe->fe=n; //a

	A->fe->fe->fe->fd=NULL;

	//parte do i

	n=(Nodo_AB*)malloc(sizeof(Nodo_AB));
	n->size=0;
	n->a='i';
	n->b=(long int*)malloc(sizeof(long int));
	A->fe->fd=n; //i

	n=(Nodo_AB*)malloc(sizeof(Nodo_AB));
	n->size=0;
	n->a='k';
	n->b=(long int*)malloc(sizeof(long int));
	A->fe->fd->fd=n; //k

	n=(Nodo_AB*)malloc(sizeof(Nodo_AB));
	n->size=0;
	n->a='l';
	n->b=(long int*)malloc(sizeof(long int));
	A->fe->fd->fd->fd=n; //l

	n=(Nodo_AB*)malloc(sizeof(Nodo_AB));
	n->size=0;
	n->a='j';
	n->b=(long int*)malloc(sizeof(long int));
	A->fe->fd->fd->fe=n; //j

	n=(Nodo_AB*)malloc(sizeof(Nodo_AB));
	n->size=0;
	n->a='h';
	n->b=(long int*)malloc(sizeof(long int));
	A->fe->fd->fe=n; //h

	n=(Nodo_AB*)malloc(sizeof(Nodo_AB));
	n->size=0;
	n->a='g';
	n->b=(long int*)malloc(sizeof(long int));
	A->fe->fd->fe->fe=n; //g

	A->fe->fd->fe->fd=NULL;

	//lado direito da árvore

	//parte do p

	n=(Nodo_AB*)malloc(sizeof(Nodo_AB));
	n->size=0;
	n->a='p';
	n->b=(long int*)malloc(sizeof(long int));
	A->fd->fe=n; //p

	n=(Nodo_AB*)malloc(sizeof(Nodo_AB));
	n->size=0;
	n->a='r';
	n->b=(long int*)malloc(sizeof(long int));
	A->fd->fe->fd=n; //r

	n=(Nodo_AB*)malloc(sizeof(Nodo_AB));
	n->size=0;
	n->a='s';
	n->b=(long int*)malloc(sizeof(long int));
	A->fd->fe->fd->fd=n; //s

	n=(Nodo_AB*)malloc(sizeof(Nodo_AB));
	n->size=0;
	n->a='q';
	n->b=(long int*)malloc(sizeof(long int));
	A->fd->fe->fd->fe=n; //q

	n=(Nodo_AB*)malloc(sizeof(Nodo_AB));
	n->size=0;
	n->a='o';
	n->b=(long int*)malloc(sizeof(long int));
	A->fd->fe->fe=n; //o

	n=(Nodo_AB*)malloc(sizeof(Nodo_AB));
	n->size=0;
	n->a='n';
	n->b=(long int*)malloc(sizeof(long int));
	A->fd->fe->fe->fe=n; //n

	A->fd->fe->fe->fd=NULL;

	//parte do w

	n=(Nodo_AB*)malloc(sizeof(Nodo_AB));
	n->size=0;
	n->a='w';
	n->b=(long int*)malloc(sizeof(long int));
	A->fd->fd=n; //w

	n=(Nodo_AB*)malloc(sizeof(Nodo_AB));
	n->size=0;
	n->a='y';
	n->b=(long int*)malloc(sizeof(long int));
	A->fd->fd->fd=n; //y

	n=(Nodo_AB*)malloc(sizeof(Nodo_AB));
	n->size=0;
	n->a='z';
	n->b=(long int*)malloc(sizeof(long int));
	A->fd->fd->fd->fd=n; //z

	n=(Nodo_AB*)malloc(sizeof(Nodo_AB));
	n->size=0;
	n->a='x';
	n->b=(long int*)malloc(sizeof(long int));
	A->fd->fd->fd->fe=n; //x

	n=(Nodo_AB*)malloc(sizeof(Nodo_AB));
	n->size=0;
	n->a='v';
	n->b=(long int*)malloc(sizeof(long int));
	A->fd->fd->fe=n; //v

	n=(Nodo_AB*)malloc(sizeof(Nodo_AB));
	n->size=0;
	n->a='u';
	n->b=(long int*)malloc(sizeof(long int));
	A->fd->fd->fe->fe=n; //u

	A->fd->fd->fe->fd=NULL;

	return(A);
}


void readMessages(int top, int modo, char *p){ //função que abre as mensagens e chama as demais funções

	FILE *f=NULL, *g=NULL; //apontadores para o ficheiro das mensagens e das keywords
	Nodo_AB *A=NULL, *nv=NULL; //raiz da árvore e variável auxiliar
	Ordem *o=NULL; //lista com os resultados da procura, mensagem a mensagem
	int j=0, comp=0, contador=1; //ID das mensagens e tamanho do vetor das keywords
	long int pos=1; //variável auxiliar
	char *v=NULL, e, a; //vetor com os carateres das keywords e carateres lidos
	
	f=fopen("msgs.bin","r");

	if(f==NULL){

		printf("\n");
		printf("A abertura do ficheiro das mensagens falhou...\n");
		printf("\n");
		exit(0);
	}

	if(modo==2){

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
	}

	A=makeTree();

	while(e!=EOF){

		e=fgetc(f);

		if(e=='\n'){

			j++;
			pos=1;

			printf("MENSAGEM ATUAL (%d/100)",j);

			if(modo==2){

				o=results(A,o,v,j);
			}

			else{

				o=results(A,o,p,j);

			}

			while(o->nant!=NULL){ //retroceder até ao início da lista de resultados

				o=o->nant;
			}

			while(o->nseg!=NULL){ //ver se já obtivemos a quantidade de mensagens que o utilizador pediu

				if(o->nseg->total>0){

					contador++;
					o=o->nseg;
				}

				else{

					o=o->nseg;
				}

			}

			A=cleanTree(A); //limpar a árvore

			if(contador==top){ //resultados finais obtidos, execução terminada

				break;
			}

			contador=1; //reset ao contador

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

	comp=0;

	while(o->nant!=NULL){ //retroceder até ao início da lista de resultados

		o=o->nant;
	}

	o=sortMessages(o); //ordenar a lista de resultados por quantidade de palavras em cada mensagem

	printf("\n");
	printf("-------------< TOP MENSAGENS >-------------\n\n\n");

	for(j=0; j<top; j++){

		printf("   %dº) MENSAGEM %d\n",(j+1),o->ID);
		printf("___________________\n\n");

		while(o!=NULL && (o->c)!=NULL){

			printf("\"");

			while((o->c->p[comp])!='\n'){

				printf("%c",o->c->p[comp]);
				comp++;
			}

			printf("\" (espaçamento %ld / coluna %ld)\n",o->c->espacamento,o->c->coluna);

			o->c=(o->c->nseg);
			comp=0;
		}

		o=(o->nseg);

		printf("\n\n");
	}

	fclose(f);

	if(modo==2){

		fclose(g);
	}

	free(v);
	free(p);
	clearTree(&A);
	A=NULL;
	clearList(&o);
	o=NULL;
}


int main(){ //função main

	clock_t t; //variável para calcular o tempo de execução
	double tempo; //variável para calcular o tempo de execução
	int controlo=0, k=0, top=0, modo=0, i=0; //variável de controlo
	char s[20], *p=NULL;

	while(1){

		printf("\n");
		printf("---------------------< CAÇA AO TERRORISTA 2.0 >---------------------\n");
		printf("\n");
		printf("1: Apanhar os terroristas\n");
		printf("2: Sair e deixá-los escapar\n");
		printf("\n");

		printf("> ");
		scanf("%d",&controlo);

		switch(controlo){

			case 1: while(k==0){

					printf("\n");
					printf("____________________________________________________________________\n");
					printf("\n");
					printf("-------------------< QUE PROCURA QUER REALIZAR? >-------------------\n");
					printf("\n");
					printf("1: Procurar por uma \"keyword\" definida por si\n");
					printf("2: Mensagens ordenadas por nº de \"keywords\" diferentes (usando o ficheiro \"keywords.txt\")\n");
					printf("\n");
					printf("3: VOLTAR\n");
					printf("\n");

					printf("> ");
					scanf("%d",&controlo);

						if(controlo==1 || controlo==2){

							while(k==0){

								if(controlo==1){

									modo=1;

									printf("\n");
									printf("Introduza a \"keyword\": ");
									scanf("%s",s);
									p=(char*)malloc((strlen(s)+2)*sizeof(char));

									do{
										p[i]=s[i];
										i++;

									}while(s[i]!='\0');

									p[i]='\n';
									p[i+1]=EOF;
									i=0;
								}

								else{

									modo=2;
								}

									printf("\n");
									printf("____________________________________________________________________\n");
									printf("\n");
									printf("-----------------< QUANTOS RESULTADOS QUER OBTER? >-----------------\n");
									printf("\n");
									printf("1: TOP 5\n");
									printf("2: TOP 10\n");
									printf("3: DÁ-ME TUDO!\n");
									printf("\n");
									printf("4: VOLTAR\n");
									printf("\n");

									printf("> ");
									scanf("%d",&controlo);

									if(controlo==1 || controlo==2 || controlo==3){

										printf("\n");
										printf("____________________________________________________________________\n");
										printf("\n");
										printf("LOADING...\n\n");

										top=controlo;

										if(top==1){top=5;}
										else if(top==2){top=10;}
										else{top=100;}

										t=clock();
										readMessages(top,modo,p);
										t=clock()-t;
										printf("\n");
										tempo=((double)t)/CLOCKS_PER_SEC;
										printf("\n");
										printf("A execução demorou %.1lf segundos.\n",tempo);
										printf("\n\n\n");
										printf("____________________________________________________________________\n");
										k=1;
									}

									else if(controlo==4){

										k=1;
									}

									else{

										printf("\n");
										printf("ESCOLHA CORRETAMENTE UMA DAS OPÇÕES, POR FAVOR.\n");
										printf("\n");
									}
								}

								k=1;
								break;

							}

						else if(controlo==3){

							k=1;
							break;
						}

						else{

							printf("\n");
					 		printf("ESCOLHA CORRETAMENTE UMA DAS OPÇÕES, POR FAVOR.\n");
							printf("\n");
							break;
						}
					}

					k=0;
					break;

			case 2: printf("\n");
					printf("____________________________________________________________________\n");
					printf("\n");
					printf("Os terroristas fugiram, mais uma cidade afetada... Por sua culpa :(\n");
					printf("\n");
			     	exit(0);

			default: printf("\n");
					 printf("ESCOLHA CORRETAMENTE UMA DAS OPÇÕES, POR FAVOR.\n");
				     printf("\n");
					 break;

		}

	}

	return(0);
}
