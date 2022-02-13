#include <stdio.h>
#define L 2
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

void escreverMatriz(float a[L][C])

{
  int i; //contador
  int d; //contador

 for(i=0; i<L; i++)
 {
  for(d=0; d<C; d++)
  {
  printf("%f\t",a[i][d]);
  }
  printf("\n");
 }
}

void trocarMatriz(float a[L][C], float b[L][C])

{
  int i; //contador
  int d; //contador

 for(i=0; i<C; i++)
 {
  for(d=0; d<L; d++)
  {
  b[i][d]=a[d][i];
  printf("%f\t",b[i][d]);
  }
 printf("\n");
 }
}

int main()

{
  float a[L][C];
  float b[L][C];

 printf("Escreva uma matriz:\n");
 lerMatriz(a);
 printf("\n");
 printf("Ou seja:\n");
 printf("\n");
 escreverMatriz(a);
 printf("\n");
 printf("Esta é a matriz transporta da anterior:\n");
 printf("\n");
 trocarMatriz(a,b);
}

