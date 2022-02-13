#include "shell.h"

void pipe1 (char **args, int numArgs, int indice){
    int pidNovoFilho, fd[2];
    args[indice] = NULL;
    pipe(fd);
    pidNovoFilho = fork();

    if (pidNovoFilho == 0){
        numArgs = indice;
        dup2 (fd[1], STDOUT_FILENO);
        close(fd[0]);
    }
    else{
        args = args + indice + 1;
        numArgs = numArgs - indice - 1;
        dup2(fd[0], STDIN_FILENO);
        close(fd[1]);

    }
    execvp(*args, args);

}


//faltam as funções built in
//depois de executar, está a sair do ciclo