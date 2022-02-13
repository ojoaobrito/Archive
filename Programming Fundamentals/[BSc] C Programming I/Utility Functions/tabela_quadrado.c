#include <stdio.h>

int quadrado(int n)

{
  int i=1; //variável de apoio
  int a;
  int c; //contador
  int b; //contador
 
 for(b=1; b<n+1; b++)
 {
  for(c=i; c<n+i; c++)
  {
  a=c;
  printf("%d \t",a);
  }
  i=i+1;
  printf(" \n"); 
 }
} 

int main()

{
  int n;

 printf("\n");
 printf("Escreva um número superior a 2:\n");
 scanf("%d",&n);

 if(n<=2)
 {
 while(n<=2)
 {
 printf("Eu pedi um número maior que 2...\n");
 scanf("%d",&n);
 }
 }
 printf("\n");
 printf("Aqui está:\n");
 printf("\n");
 quadrado(n);
 printf("\n");
}

