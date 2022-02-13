#include <stdio.h>
#include <stdlib.h>

typedef struct{

	int memoria_pedida; //quantidade de memória pedida pelo processo

} Processo;

typedef struct{

	int tamanho; //tamanho do bloco de memória

} Bloco_memoria;

char* melhorAlgoritmo(int *reset, Processo *processos, int num_processos, Bloco_memoria *blocos, int num_blocos){

	int i=0, j=0, contador_first=0, max_best=4194305, ID_best=0, contador_best=0, max_worst=0, ID_worst=0, contador_worst=0;

	for(i=0; i<num_processos; i++){ //first fit

		for(j=0; j<num_blocos; j++){

			if((blocos[j].tamanho)>=(processos[i].memoria_pedida)){

				contador_first++;
				blocos[j].tamanho=((blocos[j].tamanho)-(processos[i].memoria_pedida));
				break;
			}
		}
	}

	for(i=0; i<num_blocos; i++) //fazer "reset" aos blocos de memória
		blocos[i].tamanho=reset[i];

	for(i=0; i<num_processos; i++){ //best fit

		for(j=0; j<num_blocos; j++){

			if(((blocos[j].tamanho)>=(processos[i].memoria_pedida)) && (blocos[j].tamanho)<=max_best){

				max_best=(blocos[j].tamanho);
				ID_best=j;
			}
		}

		if(max_best!=4194305){

			blocos[ID_best].tamanho=((blocos[ID_best].tamanho)-(processos[i].memoria_pedida));
			contador_best++;
			max_best=4194305;
		}
	}

	for(i=0; i<num_blocos; i++) //fazer "reset" aos blocos de memória
		blocos[i].tamanho=reset[i];

	for(i=0; i<num_processos; i++){ //worst fit

		for(j=0; j<num_blocos; j++){

			if(((blocos[j].tamanho)>=(processos[i].memoria_pedida)) && (blocos[j].tamanho)>=max_worst){

				max_worst=(blocos[j].tamanho);
				ID_worst=j;
			}
		}

		if(max_worst!=0){

			blocos[ID_worst].tamanho=((blocos[ID_worst].tamanho)-(processos[i].memoria_pedida));
			contador_worst++;
			max_worst=0;
		}
	}

	printf("FIRST - %d BEST - %d WORST - %d\n",contador_first,contador_best,contador_worst);

	if((contador_first==contador_worst) && (contador_first==contador_best) && (contador_best==contador_worst))
		return("First");

	else if(contador_first>=((contador_best>contador_worst)?contador_best:contador_worst))
		return("First");

	else if(contador_best>=contador_worst)
		return("Best");

	else
		return("Worst");
}

int main(int argc, char **argv){

	int i=0, num_processos=0, num_blocos=0, *reset=(int*)malloc(num_blocos*sizeof(int));
	Processo *processos=NULL;
	Bloco_memoria *blocos=NULL;

	scanf(" %d",&num_processos);
	processos=(Processo*)malloc(num_processos*sizeof(Processo));

	for(i=0; i<num_processos; i++) //informação dos processos
		scanf(" %d",&(processos[i].memoria_pedida));

	scanf(" %d",&num_blocos);
	blocos=(Bloco_memoria*)malloc(num_blocos*sizeof(Bloco_memoria));

	for(i=0; i<num_blocos; i++){ //informação dos blocos de memória

		scanf(" %d",&(blocos[i].tamanho));
		reset[i]=(blocos[i].tamanho);
	}

	printf("%s\n",melhorAlgoritmo(reset,processos,num_processos,blocos,num_blocos));
	return(0);
}