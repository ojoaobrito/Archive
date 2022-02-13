#include "shell.h"

void calc(char **args){

    float a = atof(args[1]); //primeiro operando
    float b = atof(args[3]); //segundo operando
    float resultado = 0;

    if(strcmp(args[2],"+")==0)        
        resultado=(a+b);

    else if(strcmp(args[2],"-")==0)        
        resultado=(a-b);

    else if(strcmp(args[2],"*")==0)        
        resultado=(a*b);

    else if(strcmp(args[2],"/")==0){

        if(b==0){
            
            printf("ERRO! DIVISÃO POR 0\n");
            return;
        }

        resultado=(a/b);
    }

    else if(strcmp(args[2],"^")==0)        
        resultado=pow(a,b);

    printf("O resultado é: %0.2f\n", resultado);
}