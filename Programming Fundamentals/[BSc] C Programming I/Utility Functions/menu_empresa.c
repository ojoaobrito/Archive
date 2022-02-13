#include <stdio.h>
#include <stdlib.h>
#define MAX 1000

typedef struct {
	int dia, mes, ano;
} DATA;

typedef struct {
	int ID;
	char nome[30];
	char apelido[30];
	DATA datanascimento;
	float salario;
} EMPLOYEE;


void novoFUNCIONARIO(int i, EMPLOYEE E[MAX])

{
  printf("Qual o dia, o mês e o ano de nascimento do funcionário?\n");
  printf("\n");
  printf("DIA - ");
  scanf("%d",&E[i].datanascimento.dia);
  printf("MÊS - ");
  scanf("%d",&E[i].datanascimento.mes);
  printf("ANO - ");
  scanf("%d",&E[i].datanascimento.ano);
  printf("\n");
  printf("Qual é o ID do funcionário?\n");
  scanf("%d",&E[i].ID);
  printf("\n");
  printf("Qual é o nome e apelido?\n");
  scanf("%s %s",E[i].nome, E[i].apelido);
  printf("\n");
  printf("Qual é o salário do funcionário?\n");
  scanf("%f",&E[i].salario);
}


int salarioFUNCIONARIO(int i, EMPLOYEE E[MAX])

{
  int Id;

  printf("Qual o funcionário que gostaria de editar?\n");
  printf("ID - ");
  scanf("%d",&Id);
  
   for(i=0; i<MAX; i++)
   {
   	  if(Id==E[i].ID)
   	  {
   	  printf("Qual é o salário atualizado? (atual: %0.1f€)\n",E[i].salario);
   	  scanf("%f",&E[i].salario);
   	  }
   	  else
   	  {
   	  continue;
   	  }
   }
  return 0;
}


int listarFUNCIONARIO(int i, EMPLOYEE E[MAX])

{

  for(i=0; i<MAX; i++)
  {
     if(E[i].salario>=1000 && E[i].salario<=2000)
     {
     printf("%d/%d/%d, ID-%d, %0.1f€, %s %s.\n",E[i].datanascimento.dia, E[i].datanascimento.mes, E[i].datanascimento.ano, E[i].ID, E[i].salario, E[i].nome, E[i].apelido);
     }
  }
}


int main()

{
  int i;
  int controlo=0;
  EMPLOYEE E[MAX];

  while(1){

  printf("\n");
  printf(">> Base de Dados de uma empresa <<\n");
  printf("\n");
  printf("1. Inserir novo FUNCIONARIO.\n");
  printf("2. Atualizar salário de um FUNCIONARIO através do ID.\n");
  printf("3. Listar FUNCIONARIOs com salários na gama [1000,2000].\n");
  printf("4. EXIT\n");
  printf("\n");
  scanf("%d",&controlo);
  printf("\n");

  switch(controlo){
          
          case 1: printf("--Novo Funcionário--\n");
                  printf("\n");
                  novoFUNCIONARIO(i,E);
                  i++;
                  printf("\n");
                  printf("\n");
                  break;

          case 2: printf("--Atualizar Salário--\n");
                  printf("\n");
                  salarioFUNCIONARIO(i,E);
                  printf("\n");
                  printf("\n");
                  break;

          case 3: printf("--Lista de Funcionários--\n");
                  printf("\n");
                  listarFUNCIONARIO(i,E);
                  printf("\n");
                  printf("\n");
                  break;

          case 4: printf("Adeus. Volte sempre!\n");
                  printf("\n");
                  exit(1);
                  printf("\n");
                  break;

          default: printf("ERRO!!! ESCREVA UM NÚMERO ENTRE 1 E 4, POR FAVOR:\n");
                   printf("\n");
                   break;
  }
 }

  return 0;
}