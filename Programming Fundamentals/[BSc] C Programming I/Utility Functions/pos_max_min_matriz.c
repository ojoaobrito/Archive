#include <stdio.h>
#define L 3
#define C 3

void lerMatriz(float p[L][C])

{
  int i; //contador
  int b; //contador

 for(i=0; i<L; i++)
 {
  for(b=0; b<C; b++)
  {
  scanf("%f",&p[i][b]);
  }
 }
}

void escreverMatriz(float p[L][C])

{
  int i; //contador
  int b; //contador

 for(i=0; i<L; i++)
 {
  for(b=0; b<C; b++)
  {
  printf("%f\t",p[i][b]);
  }
  printf("\n");
 }
}

void posicaoMaximo(float p[L][C], int a[2])

{
  int i; //contador
  int b; //contador
  float max;
  
  max=p[0][0];
  a[0]=1;
  a[1]=1;

  for(i=0; i<L; i++)
  {
   for(b=0; b<C; b++)
   {
    if(p[i][b]>max)
    {
    max=p[i][b];
    a[0]=i+1;
    a[1]=b+1;
    }
    else
    {
    max=max;
    a[0]=a[0];
    a[1]=a[1];
    }
   }
  }
} 

void posicaoMinimo(float p[L][C], int c[2])

{
  int i; //contador
  int b; //contador
  float min;
  
  min=p[0][0];
  c[0]=1;
  c[1]=1;

  for(i=0; i<L; i++)
  {
   for(b=0; b<C; b++)
   {
    if(p[i][b]<min)
    {
    min=p[i][b];
    c[0]=i+1;
    c[1]=b+1;
    }
    else
    {
    min=min;
    c[0]=c[0];
    c[1]=c[1];
    }
   }
  }
} 


int main()

{
  float p[L][C];
  int a[2];
  int c[2];

 printf("Escreva uma matriz com %d linhas e %d colunas:\n",L,C);
 lerMatriz(p);
 printf("\n");
 printf("Ou seja:\n");
 printf("\n");
 escreverMatriz(p);
 printf("\n");
 posicaoMaximo(p,a);
 posicaoMinimo(p,c);
 printf("O máximo está na %dª coluna da %dª linha e o mínimo está na %dªcoluna da %dª linha.\n",a[1],a[0],c[1],c[0]);
}
 
