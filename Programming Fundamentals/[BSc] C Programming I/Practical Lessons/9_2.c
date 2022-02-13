#include <stdio.h>
#include <stdlib.h>

void main()

{
  FILE *f;
  char s[30];
  int i; //contador
  char b;
  char a;
  int n; //número de linhas


  printf("Quantas linhas quer copiar?\n");
  scanf("%d",&n);

  puts("Escreva o nome do ficheiro:");
  scanf("%s",s);

  f=fopen(s,"r");
 
  if(f==NULL)
  {
  printf("ERRO NA ABERTURA DO FICHEIRO.\n");
  exit(1);
  }
  else
  {
  printf("SUCESSO NA ABERTURA DO FICHEIRO.\n");
  }

  printf("Aqui estão a(s) última(s) %d linha(s) do documento:\n",n);

   while((b=fgetc(f)) != EOF)
   {
    if(b=="\n")
    {
    i=i+1;
    }
    else
    {
    i=i;
    }
   }

  while(i != )
  {
  a=fgetc(f);

  fcloseall();
}
    
    
