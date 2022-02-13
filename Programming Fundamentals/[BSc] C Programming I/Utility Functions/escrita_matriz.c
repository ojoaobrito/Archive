#include <stdio.h>
#define L 3
#define C 2

void lerMatriz(float p[L][C])

{
  int i; //contador
  int k; //contador
  int a;

 printf("Escreva os elementos das linhas de uma matriz:\n");
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


void escreverMatriz(float p[L][C])

{
  int i; //contador
  int k; //contador

 for(i=0; i<L; i++)
 {
     for(k=0; k<C; k++)
     {
     printf(" %f\t",p[i][k]);
     }
     printf("\n");
 }
}

int main()

{
   float p[L][C];
 
 printf("\n"); 
 lerMatriz(p);
 printf("\n");
 printf("A matriz é:\n");
 printf("\n");
 escreverMatriz(p);
 printf("\n");
}  

