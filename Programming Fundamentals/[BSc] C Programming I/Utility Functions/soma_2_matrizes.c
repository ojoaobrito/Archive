#include <stdio.h>
#define L 3
#define C 3

void lerMatriz(float matriz[L][C])

{
  int i; //contador
  int d; //contador

 for(i=0; i<L; i++)
 {
  for(d=0; d<C; d++)
  {
  scanf("%f",&matriz[i][d]);
  }
 }
}

void somaMatrizes(float a[L][C], float b[L][C], float c[L][C])

{
  int i; //contador
  int d; //contador

 for(i=0; i<L; i++)
 {
  for(d=0; d<C; d++)
  {
  c[i][d]=a[i][d]+b[i][d];
  printf("%f\t",c[i][d]);
  }
 printf("\n");
 }
}

int main()

{
  float a[L][C];
  float b[L][C];
  float c[L][C];
 
 printf("Escreva duas matrizes por favor:\n");
 printf("Matriz A:\n");
 lerMatriz(a);
 printf("\n");
 printf("Matriz B:\n");
 lerMatriz(b);
 printf("\n");
 printf("Aqui está a soma destas 2 matrizes:\n");
 printf("\n");
 somaMatrizes(a,b,c);
 printf("\n");
}
