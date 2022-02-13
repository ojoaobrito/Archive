#include <stdio.h>
#include <math.h>

int main()

{

  float n; //número inserido
  int i; //parte inteira do número
  float fr; //parte fracionária do número

  printf("\n");
  printf("Escreva um número real:\n");
  scanf("%f",&n);
  i=trunc(n);
  fr=n-i;
  printf("A parte inteira é \"%d\" e a parte fracionária é \"%f\".\n",i,fr);
  printf("\n");

}
