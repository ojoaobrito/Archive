#include <stdio.h>

void palindroma(int x, int b, int a, int y, int i){

	if((a%(10*i))>=(b*i)){

		printf("ERROR\n"); //não é um inteiro na base considerada
		return;
	}

	else if(x==0){

		if(y==a){

			printf("YES\n"); //é um palindroma na base considerada
			return;
		}

		printf("NO\n"); //é um inteiro na base considerada, mas não é um palindroma
		return;
	}

	//construir o número invertido
	y=(y*10)+(x%10); 
	x=(x/10);
	i=(i*10);

	palindroma(x,b,a,y,i);
}

int main(int argc, char *argv[]){

	int b=0, x=0, y=0, i=1; //base dada, número dado, número invertido e variável auxiliar

	scanf("%d",&b);
	scanf("%d",&x);
	
	palindroma(x,b,x,y,i);

	return(0);
}