#include <stdio.h>
#define DIM 3

void lerArray(int A[DIM])

{
  int a;
  int i; //contador

 for(i=0; i<DIM; i++)
 {
 scanf("%d",&a);
 A[i]=a;
 }
}

void copia(int A[DIM],int B[DIM])

{
  int i; //contador

 for(i=0; i<DIM; i++)
 {
 B[i]=A[i];
 }
}

int escreverArray(int B[DIM])

{
  int i;

 for(i=0; i<DIM; i++)
 {
 printf(" %d ",B[i]);
 }
 printf("\n");
}

int main()

{
  int A[DIM];
  int B[DIM];
  int i; //contador
 
 printf("Escreva uma sequência com %d números inteiros (Seq. A):\n",DIM);
 lerArray(A);
 copia(A,B);
 printf("Seq. B:\n");
 escreverArray(B);
}
