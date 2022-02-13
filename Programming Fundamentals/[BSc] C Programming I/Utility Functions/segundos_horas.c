#include <stdio.h>

int main()

{
  
  int hh; //horas
  int mm; //minutos
  int ss; //segundos
  int r; //resto das divisões

  printf("\n");
  printf("Escreva o tempo em segundos:\n");
  scanf("%d",&ss);
  hh=(ss/3600);
  r=(ss%3600);
  mm=(r/60);
  r=(r%60);
  ss=r;
  printf("\n");
  printf("O valor equivale a %d hora(s), %d minuto(s) e %d segundo(s).\n",hh, mm, ss);
  printf("\n");

}
