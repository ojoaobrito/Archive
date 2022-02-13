#include <stdio.h>

typedef struct
 {
 float a; //parte real
 float b; //parte imaginária
 } COMPLEXO;

COMPLEXO soma(COMPLEXO n1, COMPLEXO n2);

void main()

{
 COMPLEXO n1;
 COMPLEXO n2;
 COMPLEXO res;

  printf("\n");
  printf("Escreva a parte real e a parte imaginária do primeiro nº complexo, respetivamente:\n");
  scanf("%f %f",&n1.a, &n1.b);

  printf("Escreva a parte real e a parte imaginária do segundo nº complexo, respetivamente:\n");
  scanf("%f %f",&n2.a, &n2.b);

  res = soma(n1,n2);
  printf("O número resultante é:\n");
  printf("%.1f + %.1fi",res.a, res.b);
  printf("\n");
  printf("\n");
}

COMPLEXO soma(COMPLEXO n1, COMPLEXO n2)

{
 COMPLEXO res; //resultado

 res.a = n1.a + n2.a;
 res.b = n1.b + n2.b;

 return res;
}
