#include <stdio.h>
#include <stdlib.h>

typedef struct{

	int PID; //ID de processo
	int chegada; //instante de chegada
	int prioridade; //prioridade
	int duracao; //duração ("burst-time")
	int tempo; //tempo de circulação

}Processo;

int ProcessoAEscolher(int instante, Processo *processos, int *espera, int num, int *etot, float *tempo){

	int i=0, k=0, id=(num+1), prioridade=101;

	for(i=0; i<num; i++){ //verificar os processos que acabaram de chegar

		if(processos[i].PID!=-1 && processos[i].duracao==0){ //se o processo acabar, vamos marcá-lo como finalizado

			*tempo=(*tempo+(processos[i].tempo));
			processos[i].PID=-1;
			k++;
		}

		else if(processos[i].PID!=-1 && (processos[i].chegada)==instante){ //colocá-los na lista de espera 

			(*etot)++;
			espera[(*etot)-1]=(processos[i].PID);
		}

		else if(processos[i].PID==-1)
			k++;
	}

	if(k==num) //não há mais processos para correr
		return(-1);

	for(i=0; i<(*etot); i++){ //escolher o processo, com maior prioridade, da lista de espera

		if(processos[espera[i]-1].PID!=-1 && (processos[espera[i]-1].prioridade)<prioridade){

			id=(processos[espera[i]-1].PID);
			prioridade=(processos[espera[i]-1].prioridade);
		}

		else if(processos[espera[i]-1].PID!=-1 && (processos[espera[i]-1].prioridade)==prioridade){

			id=((processos[espera[i]-1].PID)<id)?(processos[espera[i]-1].PID):id;
		}
	}

	return(id);
}

int main(){

	int i=0, num=0, *espera=NULL, etot=0, atual=0, j=0;
	float tempo=0;
	Processo *processos=NULL;

	scanf(" %d",&num); //número de processos

	processos=(Processo*)malloc(num*sizeof(Processo));
	espera=(int*)malloc(num*sizeof(int));

	for(i=0; i<num; i++){

		(processos[i].PID)=(i+1);
		scanf(" %d %d %d",&(processos[i].chegada),&(processos[i].prioridade),&(processos[i].duracao));
	}

	i=0; //instante

	while(1){

		atual=ProcessoAEscolher(i,processos,espera,num,&etot,&tempo);
		i++;

		if(atual==(num+1)) //não há processos a correr
			printf("%d-IDLE\n",(i-1));

		else if(atual==-1) //todos os processos foram executados
			break;

		else{ //existe algum processo a correr

			printf("%d-P%d\n",(i-1),atual);
			(processos[atual-1].duracao)--;

			for(j=0; j<num; j++){ //incrementar o tempo de circulação de todos os processos em espera (ou a correr)

				if(processos[j].PID!=-1 && (processos[j].chegada)<=(i-1)){

					(processos[j].tempo)++;
				}
			}
		}
	}

	printf("TMC=%.1f\n",tempo/num);

	free(processos);
	free(espera);
	return(0);
}