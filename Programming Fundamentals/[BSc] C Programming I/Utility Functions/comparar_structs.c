#include <stdio.h>
#include <stdlib.h>
#define MAX 20

typedef struct
 {
 char nome[MAX];
 char apelido[MAX];
 char residencia[MAX];
 int telefone;
 } ESTUDANTE;


void equalEntry(ESTUDANTE r1, ESTUDANTE r2)

{
  int i,controlo=1; 
    
 for(i=0; i<MAX; i++)
 {
  if(r1.nome[i]==r2.nome[i])
  {
  continue;
  }
  else
  {
  printf("Os registos são diferentes.\n");
  controlo=0;
  break;
  }
 }
 
 if(controlo==1)
 {
     for(i=0; i<MAX; i++)
     {
      if(r1.apelido[i]==r2.apelido[i])
      {
      continue;
      }
      else
      {
      printf("Os registos são diferentes.\n");
      controlo=0;
      break;
      }
     }
 }

 if(controlo==1)
 {
     for(i=0; i<MAX; i++)
     { 
      if(r1.residencia[i]==r2.residencia[i])
      {
      continue;
      }
      else
      {
      printf("Os registos são diferentes.\n");
      controlo=0;
      break;
      }
     }
 }

 if(controlo==1)
 {      
  if(r1.telefone==r2.telefone)	
   {
   printf("Os registos são iguais.\n");
   }
 }
}


void comesFirst(ESTUDANTE r1, ESTUDANTE r2)

{
  int i; //contador
    
 for(i=0; i<MAX; i++)
 {
  if(r1.nome[i]<r2.nome[i])
  {
  printf("O registo 1 precede o registo 2.\n");
  break;
  }
  else if(r1.nome[i]>r2.nome[i])
  {
  printf("O registo 1 sucede o registo 2.\n");
  break;
  }
  else if(r1.nome[i]==r2.nome[i])
  {
  printf("Os nomes são iguais.\n");
  break;
  }
 }
}


void main()

{
  ESTUDANTE r1;
  ESTUDANTE r2;
  
 printf("Escreva, respetivamente, o nome, apelido, a residência e o telefone do 1º registo:\n");
 scanf("%s %s %s %d",r1.nome,r1.apelido,r1.residencia,&r1.telefone);

 printf("Escreva, respetivamente, o nome, apelido, a residência e o telefone do 2º registo:\n");
 scanf("%s %s %s %d",r2.nome,r2.apelido,r2.residencia,&r2.telefone);

 equalEntry(r1,r2);
 comesFirst(r1,r2);
}

 
