#include <stdio.h>
#define L 3 
#define C 2

void lerMatriz(float p[L][C])

{
  int i; //contador
  int k; //contador
  int a;

 printf("Escreva os elementos das linhas da matriz:\n");
 printf("\n");

 for(i=0; i<L; i++)
 {
 a=i+1;
 printf("Linha %d:\n",a);
     for(k=0; k<C; k++)
     {
     scanf("%f",&p[i][k]);
     }
 }
}

float somaElementosMatriz(float p[L][C])

{
  int i; //contador
  int k; //contador
  float soma=0;

 for(i=0; i<L; i++)
 {
     for(k=0; k<C; k++)
     {
     soma=soma+p[i][k];
     }
 }
 printf("%f\n",soma);
}
      
int main()

{
  float p[L][C];
 
 printf("\n");
 lerMatriz(p);
 printf("\n");
 printf("Aqui está a soma dos elementos desta matriz:\n");
 somaElementosMatriz(p);
 printf("\n");
}

