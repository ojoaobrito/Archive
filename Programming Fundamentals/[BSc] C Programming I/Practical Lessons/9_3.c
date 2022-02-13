#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()

{
 FILE *f;
 char s[30];
 char c[20];
 char b;
 char a[20];
 int i;
 int valor;


 printf("Qual é o ficheiro em que pretende procurar?\n");
 gets(s);

 printf("Que palavra que encontrar?\n");
 gets(c);

 f = fopen(s,"r");

 if(f==NULL)
 {
 printf("ERRO NA ABERTURA DO FICHEIRO, TENTE NOVAMENTE.\n");
 exit(1);
 }

 else
 {
 printf("SUCESSO NA ABERTURA DO FICHEIRO\n");
 }

 while(b!=EOF){
b=getc(f);

     if(strcmp(b,' ')!=0)
  {
  a[i]=b;
  i=i+1;
  }
  else{
    for(i=0; i<20; i++)
    {
    valor=((a[i]==c[20])?1:0);
    }
  }
}

return(0);
}
