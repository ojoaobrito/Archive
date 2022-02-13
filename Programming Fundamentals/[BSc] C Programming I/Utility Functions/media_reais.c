#include <stdio.h>
#define DIM 5

void lerArray(float X[DIM])

{
  int i; //contador
  float a;

 for(i=0; i<DIM; i++)
 {
 scanf("%f",&a);
 X[i]=a;
 }
}

float media(float X[DIM])

{
  int i; //contador
  float media;  
  float soma=0; 
 
 for(i=0; i<DIM; i++)
 {
 soma=soma+X[i];
 }
 media=(soma/DIM);
 printf("A média é: %f\n",media);
}

int main()

{
  float X[DIM];
 
 printf("Escreva %d reais:\n",DIM); 
 lerArray(X);
 media(X);
}
