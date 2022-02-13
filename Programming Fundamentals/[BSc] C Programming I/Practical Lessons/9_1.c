#include <stdio.h>
#include <stdlib.h>

int main()

{
  FILE *f, *d;
  char a;
  char s[30];

  puts("Que ficheiro pretende abrir?");
  gets(s);

  f = fopen(s, "r");
  
  if(f==NULL)
  {
  printf("ERRO NA ABERTURA DO FICHEIRO \"%s\".\n",s);
  exit(1);
  }
  else
  {
  printf("Sucesso na abertura do ficheiro \"%s\".\n",s);
  }  
  
  d = fopen("nada.txt", "w");

  if(d==NULL)
  {
  printf("ERRO!!\n");
  exit(2);
  }
 
    do {
    a=fgetc(f);
    fputc(a, d);
       }
    while(a != EOF);

  printf("O conteúdo de \"%s\" foi copiado com sucesso para \"nada.txt\".\n",s); 
  fcloseall();
  return 0;

}
