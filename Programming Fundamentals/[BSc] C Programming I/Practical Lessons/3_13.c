#include <stdio.h>

int main()

{

  float a; //concentração A
  float A;
  float b; //concentração B
  float B;
  float c; //concentração C
  float C;
  float p; //produto

  printf("\n");
  printf(" A     B     C\n");
  printf("0.1   0.5   0.6   Produto 1\n");
  printf("0.1   0.3   0.7   Produto 2\n");
  printf("0.2   0.5   0.7   Produto 3\n");
  printf("0.2   0.3   0.1   Produto 4\n");
  printf("0.2   0.5   0.6   Produto 5\n");
  printf("\n");
  printf("Escreva o valor das concentrações A, B e C:\n");
  scanf("%f %f %f",&a,&b,&c);
  printf("\n");
  A=(int)(a*10);
  B=(int)(b*10);
  C=(int)(c*10);
  
  if(A==1 && B==5 && C==6)
  {
   printf("Produto 1.\n");
  }
  else if(A==1 && B==3 && C==7)
  {
   printf("Produto 2.\n");
  }
  else if(A==2 && B==5 && C==7) 
  {
   printf("Produto 3.\n");
  }
  else if(A==2 && B==3 && C==1)
  {
   printf("Produto 4.\n");
  }
  else if(A==2 && B==5 && C==6)
  {
   printf("Produto 5.\n");
  }
  else
  {
   printf("Produto Desconhecido!!!\n");
  }
  printf("\n");
}










