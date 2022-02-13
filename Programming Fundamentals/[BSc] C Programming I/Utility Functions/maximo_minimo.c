#include <stdio.h>
#define DIM 5

int lerArray(int X[DIM])

{

 int i; //contador
 int a; //variável do Array
  
 for(i=0; i<DIM; i++)
 
 {
  scanf("%d",&a);
  X[i]=a;
 }
  
  return a;
}
 
int maximo(int X[DIM])

{

 int max; //máximo
 int i; //contador

 max=X[0];

 for(i=0; i<DIM; i++)
 {
 if (X[i]>max)
 {
 max=X[i];
 }
}
 
 return max;

}

int minimo(int X[DIM])

{

 int min; //mínimo
 int i; //contador

 min=X[0];

 for(i=0; i<DIM; i++)
 {
 if(X[i]<min)
 {
 min=X[i];
 }
}

 return min; 

}
  
int main()

{

  int X[DIM]; //array
  int max; //maximo
  int min; //minimo
 
  printf("\n");
  printf("Escreva %d valores:\n",DIM);
  lerArray(X);
  maximo(X);
  minimo(X);

  printf("O valor máximo é %d e o valor mínimo é %d.\n",maximo(X),minimo(X));
  printf("\n");
}

