#include <stdio.h>

typedef struct
 {
 int hh;
 int mm;
 double secs;
 } TIME;

 TIME convertTime(double secs)
 { 
  int hh;
  int mm;
  int r;  

  hh=int(secs/3600);
  r=(secs%3600);
  mm=int(r/60);
  secs=(r%60);
  
  TIME = {}
 






void main()

{
  double secs; 

 printf("Escreva o tempo em segundos (ex: \"33.236 segundos\"):\n");
 scanf("%lf",&secs);
 convertTime(secs);

