#include <stdio.h>
#define L 3
#define C 2

void lerMatriz(float p[L][C])

{
  int i; //contador
  int k; //contador
  int a;

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


void escreverMatriz(float p[L][C])

{
  int i; //contador
  int k; //contador

 for(i=0; i<L; i++)
 {
    for(k=0; k<C; k++)
    {
    printf(" %f \t",p[i][k]);
    }
 printf("\n");
 }
}
     

float maximo(float p[L][C])

{
  float max;
  int i; //contador
  int k; //contador

 max=p[0][0];

 for(i=0; i<L; i++)
 {
    for(k=0; k<C; k++)
    {
     if(p[i][k]>max)
     {
     max=p[i][k];
     } 
    }
 }
 return max;
}


float minimo(float p[L][C])

{
  float min;
  int i; //contador
  int k; //contador

 min=p[0][0];

 for(i=0; i<L; i++)
 {
    for(k=0; k<C; k++)
    {
     if(p[i][k]<min)
     {
     min=p[i][k];
     } 
    }
 }
 return min;
}

int main()

{
  float p[L][C];
 
 printf("\n");
 printf("Escreva os elementos das linhas de uma matriz:\n");
 printf("\n");
 lerMatriz(p);
 printf("\n");
 printf("Ou seja:\n");
 printf("\n");
 escreverMatriz(p);
 printf("\n");
 maximo(p);
 minimo(p);
 printf("O máximo é %f e o mínimo é %f.\n",maximo(p),minimo(p));
 printf("\n");
}

 
