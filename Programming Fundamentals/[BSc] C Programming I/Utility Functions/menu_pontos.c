#include <stdio.h>
#include <math.h>

typedef struct
{
  float x;
  float y;
  float z;
} PONTO;

PONTO distancia()

{
  float distancia;
  float r1, r2, r3;
  PONTO p1,p2;
 
 printf("---DISTÂNCIA ENTRE 2 PONTOS---\n");
 printf("Escreva as coordenadas do 1º ponto:\n");
 printf("Coordenada x: ");
 scanf("%f",&p1.x);  
 printf("Coordenada y: ");
 scanf("%f",&p1.y); 
 printf("Coordenada z: ");
 scanf("%f",&p1.z); 
 
 printf("Escreva as coordenadas do 2º ponto:\n");
 printf("Coordenada x: ");
 scanf("%f",&p2.x);  
 printf("Coordenada y: ");
 scanf("%f",&p2.y); 
 printf("Coordenada z: ");
 scanf("%f",&p2.z); 

 r1 = ((p2.x)-(p1.x));
 r2 = ((p2.y)-(p1.y));
 r3 = ((p2.z)-(p1.z)); 

 distancia = sqrt((pow(r1,2))+(pow(r2,2))+(pow(r3,2)));

 printf("\n");
 printf("A distância é: %f.\n",distancia);

}


PONTO pmedio()

{
  PONTO p1,p2;

 printf("---PONTO MÉDIO---\n");
 printf("Escreva as coordenadas do 1º ponto:\n");
 scanf("%f %f %f",&p1.x, &p1.y, &p1.z);

 printf("Escreva as coordenadas do 2º ponto:\n");
 scanf("%f %f %f",&p2.x, &p2.y, &p2.z);

 PONTO medio = {(p1.x+p2.x)/2,(p1.y+p2.y)/2,(p1.z+p2.z)/2};
 
 printf("\n");
 printf("O ponto médio é: {%f,%f,%f}.\n",medio.x,medio.y,medio.z);
}


int main()

{
  int controlo=0;
 
 printf("\n");
 while(1)
 {
 printf(">>>GEOMETRIA<<<\n");
 printf("\n");
 printf("1. Distância entre dois pontos em R3.\n");
 printf("2. Ponto médio entre dois pontos em R3.\n");
 printf("3. Baricentro de N pontos em R3.\n");
 printf("4. EXIT\n");
 printf("\n");
 printf("ESCOLHA UMA DAS OPÇÕES ACIMA:\n");
 scanf("%d",&controlo);
 printf("\n");
 printf("\n");

 switch (controlo)
 {
    case 1: distancia();
            printf("\n");
            printf("\n");	
            break;

    case 2: pmedio();
            printf("\n");
            printf("\n");
            break;

    case 3: printf("Não sei o que é isso. Desculpa.\n");
            printf("\n");
            printf("\n");
            break;  

    case 4: printf("ADEUS, VOLTE SEMPRE!\n");
            printf("\n");
            return 0;

   default: printf("Digite um número entre 1 e 4...\n");
            printf("\n");
 }
 }
}
