#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <string.h>
#include <unistd.h>
#include <pthread.h>
#include <ctype.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <math.h>
#include <pthread.h>
#include <dirent.h>

typedef struct{
    char msg[100];
    int tempo;
}aviso_t;

typedef struct{
    char fonte[100];
    char destino[100];
}copiar_t;

int sols(int nrArgs, char **argv);

void aviso(char*mesg, int tempo);

void* avisowrapper(void *args);

int parse(char *buf, char **args);

void execute(char **args, int waitAux);

int builtin (char **args, int nrArgs);

void socp(int in, int out);

void calc(char **args);

void bits(char **args);

int isJPG(int fd);

int redirects(int numargs, char *args[]);

void pipe1 (char **args, int numArgs, int indice);

/* constantes que podem tornar uteis*/

#define BG 0
#define FG 1
