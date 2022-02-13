#include <stdio.h>
#define DIM 5

void lerArray(float A[DIM])

{

 float a;
 int i; //contador

 for(i=0; i<DIM; i++)
 {
 scanf("%f",&a);
 A[i]=a;
 }
}

void LerArray(float B[DIM])

{

 float b;
 int i; //contador

 for(i=0; i<DIM; i++)
 {
 scanf("%f",&b);
 B[i]=b;
 }
}

void soma(float A[DIM], float B[DIM], float C[DIM])

{

 int i; //contador
 
 for(i=0; i<DIM; i++)
 {
 C[i]=A[i]+B[i];
 }
}

int main ()

{

 float A[DIM]; 
 float B[DIM];
 float C[DIM];
 int i; //contador

 printf("Escreva uma sequência de %d números (Seq. A):\n",DIM);
 lerArray(A);
 printf("Escreva a segunda sequência de %d números (Seq. B):\n",DIM);
 LerArray(B);
 printf("A nova sequência (Seq. C) é:\n");
 
 for(i=0; i<DIM; i++)
 {
 soma(A,B,C);
 printf("  %f  ",C[i]);
 } 
 printf("\n");
}

