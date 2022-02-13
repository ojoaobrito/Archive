#include <stdio.h>
int par(int r)
 
{
   
  if(r==0)
  {
  printf("Par\n");
  }
  else
  {
  printf("Ímpar\n");
  }
} 
  
int main()

{  

  int i; //número introduzido
  int r; //resto das divisões
  
  printf("Escreva um valor inteiro:\n");
  scanf("%d",&i);
  r=i%2;
  par(r);
}
  
  
