#include <stdio.h>
#include <string.h> 

int main()

{
   char a[100];
   int comprimento;
 
   printf("\n");
   printf("Escreva a string para calcular o seu comprimento:\n");
   gets(a);
 
   comprimento = strlen(a);
 
   printf("O comprimento da string é %d.\n",comprimento);
   printf("\n");
 
   return 0;
}
