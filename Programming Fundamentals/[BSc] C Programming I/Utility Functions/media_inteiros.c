#include <stdio.h>

int lerArray(int n)

{
  int a;
  int i; //contador
  int X[n]; 

 for(i=0; i<n; i++)
 {
 scanf("%d",&a);
 X[i]=a;
 }
}

float media(int n)

{
  float soma=0;
  int i; //contador
  float media=0;
  int X[n];

 for(i=0; i<n; i++)
 {
 soma=soma+X[i];
 }
 media=(soma)/n;
}

int main()

{
  int n; //nº de números escritos
 
 printf("Quantos números vai escrever?\n");
 scanf("%d",&n);
 printf("Escreva-os então...\n");
 lerArray(n);
 media(n);
 printf("A média é: %f\n",media(n));
}


