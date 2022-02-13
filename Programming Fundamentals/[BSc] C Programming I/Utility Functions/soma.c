#include <stdio.h>
#define DIM 5

void lerArray(int X[DIM])
{

  int i; //variável de apoio
  int a; //variável com o array

  for (i=0; i<DIM; i++)

  {

   scanf("%d",&a);
   X[i]=a;

  }

}

int somaElementosArray(int X[DIM])
{

  int i; //variável de apoio
  int soma=0; //variável soma

  for (i=0; i<DIM; i++)
  
  {

   soma=soma+X[i];
   
  } 
 
  return soma;

}

int main()

{

  int soma;
  int a[DIM];

  printf("\n");
  printf("Introduza os elementos do Array:\n");
  lerArray(a);
  soma=somaElementosArray(a);
  printf("O valor da soma é: %d\n",soma);
  printf("\n"); 
}
