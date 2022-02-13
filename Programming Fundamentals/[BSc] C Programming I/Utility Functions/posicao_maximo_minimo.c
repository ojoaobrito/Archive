#include <stdio.h>
#define DIM 5

void lerArray(int X[DIM])

{

 int i; //contador
 int a; //valores escritos

 for(i=0; i<DIM; i++)
 {
 scanf("%d",&a);
 X[i]=a;
 }
}

int posicaoMaximo(int X[DIM])

{

 int max; //máximo
 int i; //contador
 int pos; //posição


 max=X[0];
 pos=1;

 for(i=1; i<DIM; i++)
 {
 if(X[i]>max)
 {
 max=X[i];
 pos=i+1;
 }
 }
 return pos;
}


int posicaoMinimo(int X[DIM])

{

 int min; //minimo
 int i; //contador
 int posi; //posição

 min=X[0];
 posi=1;

 for(i=1; i<DIM; i++)
 {
 if(X[i]<min)
 {
 min=X[i];
 posi=i+1;
 }
 }
 return posi;
}


int main()

{

 int X[DIM];

 printf("\n");
 printf("Escreva %d valores inteiros:\n",DIM);
 lerArray(X);
 posicaoMaximo(X);
 posicaoMinimo(X);
 printf("\n");
 printf("O máximo ocupa a %dº posição e o mínimo ocupa a %dº posição.\n",posicaoMaximo(X),posicaoMinimo(X));
 printf("\n");
}
