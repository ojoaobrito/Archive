#include <stdio.h>
#include <math.h>

int main()

{
  
  float a; //coeficiente a
  float b; //coeficiente b
  float c; //coeficiente c
  float x1; //uma das soluções
  float x2; //a outra solução
  float y; //binómio discriminante

  printf("\n");
  printf("Introduza os valores de a, b e c:\n");
  scanf("%f %f %f",&a,&b,&c);
  y=((b*b)-(4.0*a*c));
  
  if(a>0 && b==0 && c>0)
  {
   printf("Erro!!! Verifique os valores introduzidos.\n");
  }
  else if(a<0 && b==0 && c<0)
  {
   printf("Erro!!! Verifique os valores introduzidos.\n");
  }
  else if(y<0)
  {
   printf("Erro!!! Verifique os valores introduzidos.\n");
  }
  else
  {
  x1=((-b)+sqrt(y))/(2*a);
  x2=((-b)-sqrt(y))/(2*a);
  }
  printf("X1=%f e X2=%f\n",x1,x2);
  printf("\n");
}
