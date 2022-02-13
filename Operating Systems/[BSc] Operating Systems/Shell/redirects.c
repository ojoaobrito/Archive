#include "shell.h"

#define FILE_MODE (S_IRUSR|S_IWUSR)
#define FILE_MODE1 (O_WRONLY|O_APPEND)

int redirects(int numArgs, char **args){

    if(numArgs<3) return 0;

    if(strcmp(args[numArgs-2],"2>")==0){

        int fd=creat(args[numArgs-1],FILE_MODE);
        dup2(fd,STDERR_FILENO);
        close(fd);
        args[numArgs-1]=NULL;
        numArgs=(numArgs-2);
    }

    if(numArgs<3) return 0;

    if(strcmp(args[numArgs-2],">")==0){

        int fd=creat(args[numArgs-1],FILE_MODE);
        dup2(fd,STDOUT_FILENO);
        close(fd);
        args[numArgs-2]=NULL;
        numArgs=(numArgs-2);
    }

    else{
        
        if(strcmp(args[numArgs-2],">>")==0){
            
            int fd=open(args[numArgs-1],FILE_MODE1);
            
            if (fd<0){
                fprintf(stderr,"ERRO! IMPOSSÍVEL EFETUAR O REDIRECIONAMENTO\n");
                return 0;
            }

            dup2(fd,STDOUT_FILENO);
            close(fd);
            args[numArgs-2]=NULL;
            numArgs=(numArgs-2);
        }
    }

    if(numArgs>=3){

        if (strcmp(args[numArgs-2],"<")==0){

            int fd=open(args[numArgs-1],O_RDONLY);
            
            if(fd<0){
                
                fprintf(stderr, "ERRO! IMPOSSÍVEL EFETUAR O REDIRECIONAMENTO\n");
                return 0;
            }

            close(STDIN_FILENO);
            dup(fd);
            close(fd);
            args[numArgs-2]=NULL;
        }
    }

    execute(args,numArgs);
    return 0;
}