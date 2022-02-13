#include <stdio.h>

int tabuada(int n)

{
  int i; //contador
  int a;

 for(i=1; i<11; i++)
 {
 a=n*i;
 printf(" %d  x  %d  =  %d\n",n,i,a);
 }    
}

int main()

{
  int n;

 printf("Escolha um valor entre 1 e 10:\n");
 scanf("%d",&n);

 if(n<1)
 {
 printf("Sua besta! Eu disse \"entre 1 e 10\"!!");
 }
 else if(n>10)
 {
 printf("Sua besta! Eu disse \"entre 1 e 10\"!!");
 }
 
 printf("\n");
 printf("Tabuada do %d:\n",n);
 printf("\n");
 tabuada(n);
}
 
