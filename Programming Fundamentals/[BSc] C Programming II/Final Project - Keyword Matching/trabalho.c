#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct{

	int ID[8]; //ID de cada ficheiro
	int assinatura[2048]; //assinatura de cada ficheiro
	int distancia; //distancia de Hamming para a sequência introduzida
	int coluna; //coluna na qual se encontra a sequência pedida (para o utilizador saber exatamente onde está a mesma)
	int linha; //linha  na qual se encontra a sequência pedida (para o utilizador saber exatamente onde está a mesma)

} DADO;


void resultados(DADO *z, int a, long int tot){

	int i,j; //contador
	int k=0; //variável auxiliar

	printf("\n");
	printf("O(s) conteúdo(s) mais parecido(s) são(é):\n");
	printf("\n");

	for(i=0; i<2049; i++){

		for(j=0; j<tot; j++){

			if(z[j].distancia==i){

				if(k<a){
			
				printf("ID: %c%c%c%c%c%c%c%c (l. %d), com Distância %d e na Coluna %d.\n",z[j].ID[0],z[j].ID[1],z[j].ID[2],z[j].ID[3],z[j].ID[4],z[j].ID[5],z[j].ID[6],z[j].ID[7],z[j].linha,z[j].distancia,z[j].coluna);
				printf("\n");
				k++;
				}
			}

		}

	}

	printf("______________________________________________________________\n");

}


void distancia(DADO *z, long int tot, int c, char *b){

	int i, j; //contadores
	int min=c; //variável auxiliar
	int k=0; //variável auxiliar


	for(i=0; i<(2048-c); i++){

		for(j=0; j<c; j++){

			if((i+j)<=2047 && b[j]!=z[tot-1].assinatura[i+j]){

				z[tot-1].distancia=(z[tot-1].distancia + 1);
			}

			else{

				continue;
			}

		}

		if(z[tot-1].distancia==0){

			z[tot-1].coluna=(14+i);
			return;
		}

		
		else if(z[tot-1].distancia<=min){

			min=z[tot-1].distancia;
			z[tot-1].distancia=0;
			k=i;
		}

	}

	z[tot-1].distancia=min;
	z[tot-1].coluna=(14+k);
	
}

void pesquisar(){

	FILE *f; //ficheiro "DANGER_DB_LARGE.txt"
	DADO *z=NULL; //apontador para o vetor com as caraterísticas de cada ficheiro
	long int tot=0; //tamanho do vetor com as caraterísticas de cada ficheiro
	int a; //nº de resultados a procurar
	int c; //comprimento da sequência introduzida
	int i; //contador
	int j=1; //variável auxiliar
	int k=0; //contador
	int e=0; //carateres da base de dados
	char b[2048]; //sequência introduzida

	printf("\n");
	printf("______________________________________________________________\n");
	printf("\n");
	printf("\n");
	printf(">> Pesquisa de Sequência <<\n");
	printf("\n");

	f=fopen("DANGER_DB_LARGE.txt", "r");

	if(f==NULL){

		printf("\n");
		printf("ERRO NA ABERTURA DA BASE DE DADOS!!\n");
		printf("\n");
		exit(1);
	}

	printf("\n");
	printf("Quantos resultados pretende?\n");
	printf("> ");
	scanf("%d",&a);

	while(a==0 || a<0){

		printf("\n");
		printf("Introduza um valor válido:\n");
		printf("> ");
		scanf("%d",&a);

		if(a>0){

			break;
		}

	}


	printf("\n");
	printf("Introduza a sequência a procurar (seq. de \"1\" e \"0\"):\n");
	printf("> ");
	scanf("%s",b);
	c=strlen(b);

	printf("\n");

	 z=(DADO*)realloc(z,(++tot)*sizeof(DADO));

	 while(e!=EOF){

		e=fgetc(f);

		if(k<8){

			z[tot-1].ID[k]=e;
				
		}

		else if(k==8 && e=='\t'){

			continue;
		}

		else if(k>=9 && e!='\n'){

			z[tot-1].assinatura[k-9]=e;
		}

		else if(e=='\n'){

			z[tot-1].linha=j;
			j++;
			k=(-1);
			z=(DADO*)realloc(z,(++tot)*sizeof(DADO));
		}

		k++;

	}

	fclose(f);

	for(i=1; i<=tot; i++){

		distancia(z,i,c,b);
	}

	resultados(z,a,tot);
	
	free(z);

}



void main(){

	int controlo=0; //variável de controlo

	while(1){

		printf("\n");
		printf("----- MENU -----\n");
		printf("\n");
		printf("1: Leitura e Pesquisa de Ficheiro\n");
		printf("2: EXIT\n");
		printf("\n");

		printf("> ");
		scanf("%d",&controlo);

		switch(controlo){


			case 1:	pesquisar();
					printf("\n");
					continue;

			case 2: printf("\n");
					printf("ADEUS, VOLTE SEMPRE!!\n");
					printf("\n");
					exit(1);
					break;

			default: printf("\n");
					 printf("\n");
					 printf("ESCOLHA CORRETAMENTE UMA OPÇÃO!!\n");
					 printf("\n");
					 continue;
		}

	}

}
