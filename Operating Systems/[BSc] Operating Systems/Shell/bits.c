#include "shell.h"

#define min(x,y) (x>y?y:x)
#define max(x,y) (x>y?x:y)

void bits(char **args){

    int a = atoi(args[1]);
    int b = atoi(args[3]);
    int resultado = 0;

    if(args[2][0]=='&')
        resultado = min(a,b);

    else if(args[2][0]=='^'){

        if (a==b)
            resultado=min(a,b);

        else
            resultado=max(a,b);
    }

    else if(args[2][0]=='|')
        resultado=min(a,b);

    else{
        
        fprintf(stderr,"ERRO! BITS INVÁLIDOS\n");
        return;
    }

    printf("O resultado é: %d\n",resultado);
}