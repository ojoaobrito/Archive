#include "cs.h"

int flag=1;

void aviso(char *mesg, int tempo){ //avisar o cliente do período de autenticação expirado

    while(tempo>0){

        sleep (1);
        tempo--;
    }
    
    flag=0;
}

void* avisoAux(void *args){ //função auxiliar

    aviso_t *ptr = (aviso_t *) args;
    aviso(ptr->msg, ptr->tempo);
    free(ptr);
    return NULL;
}

int compareInput(char *fname, char *v){ //compara strings (sem contar qualquer tipo de lixo)

    int i;

    for(i=0; i<25; i++){

        if(v[i]=='\0'){

            return(1);
        }

        else if(fname[i]!=v[i]){

            return(0);
        }
    }

    return(0);
}

char* criaRelatorio(char *fname){ //gera informações de ficheiros

    int fd;
    struct stat fprop;
    mode_t *permissoes=NULL;
    char *r=(char*)malloc(80*sizeof(char));

    fd=open(fname, O_RDONLY);

    if(fstat(fd, &fprop)!=0){ //criar uma estrutura com propriedades do ficheiro ("fprop")

        free(r);
        close(fd);
        return(0);      
    }

    permissoes=(mode_t*)malloc(9*sizeof(mode_t));
    permissoes[0]=S_IRUSR;
    permissoes[1]=S_IWUSR;
    permissoes[2]=S_IXUSR;
    permissoes[3]=S_IRGRP;
    permissoes[4]=S_IWGRP;
    permissoes[5]=S_IXGRP;
    permissoes[6]=S_IROTH;
    permissoes[7]=S_IWOTH;
    permissoes[8]=S_IXOTH;

    strcpy(r,"User permissions: ");

    if(fprop.st_mode & permissoes[0]){

        strcat(r, "S_IRUSR");
    }    

    else if(fprop.st_mode & permissoes[1]){

        strcat(r, " | S_IWUSR");
    }

    else if(fprop.st_mode & permissoes[2]){

        strcat(r, " | S_IXUSR");
    }

    strcat(r, "\nGroup permissions: ");

    if(fprop.st_mode & permissoes[3]){

        strcat(r, "S_IRGRP");
    }    

    else if(fprop.st_mode & permissoes[4]){

        strcat(r, " | S_IWGRP");
    }

    else if(fprop.st_mode & permissoes[5]){

        strcat(r, " | S_IXGRP");
    }

    strcat(r, "\nOther permissions: ");

    if(fprop.st_mode & permissoes[6]){

        strcat(r, "S_IROTH");
    }    

    else if(fprop.st_mode & permissoes[7]){

        strcat(r, " | S_IWOTH");
    }

    else if(fprop.st_mode & permissoes[8]){

        strcat(r, " | S_IXOTH");
    }

    return(r);
}

int main(){

    char *fname=(char*)malloc(25*sizeof(char)), c=EOF, *v=NULL, *r=NULL, user[50]="", user2[50]="", temp[50]="", file[50]="";
    char fcontent;
    int fd, fd1, fd2, i, tot=0, pass, pass2, aux=0, log2;
    FILE *log;

    mkfifo("fifo1", 0600);
    mkfifo("fifo2", 0600);

    mkfifo("fifo_pass", 0600);
    mkfifo("fifo_pass2", 0600);

    fd = open("fifo1", O_RDONLY);
    fd1 = open("fifo2", O_WRONLY);
    pass = open("fifo_pass", O_RDONLY);
    pass2 = open("fifo_pass2", O_WRONLY);

    log=fopen("log.txt", "a");

    if(log==NULL)
        return(0);
    
    while(1){

        if(read(pass,fname,25)!=0){ //autenticação

            fd2 = open("utilizadores.txt", O_RDONLY);

            if(fd2<0){

                write(pass2, "F", 1);
                break;
            }

            while(read(fd2, &fcontent, 1)!=0){

                if(fcontent!='\n' && fcontent!=EOF){

                    v=(char*)realloc(v,(++tot)*sizeof(char));
                    v[tot-1]=fcontent;
                }

                else{

                    v=(char*)realloc(v,(++tot)*sizeof(char));
                    v[tot-1]='\0';                   

                    aux=compareInput(fname,v);

                    if(aux==1){

                        strcpy(temp, "Successful Authentication by ");
                        strcat(user, fname);
                        strcat(user2, fname);
                        strcat(temp, user2);

                        fputs(temp, log);
                        fputs("\n", log);

                        pthread_t th;
                        aviso_t *ptr = (aviso_t *) malloc(sizeof(aviso_t));
                        ptr->tempo=10;
                        pthread_create(&th, NULL, avisoAux, (void *)ptr);

                        write(pass2, "S", 1);

                        close(pass);
                        close(pass2);
                        break;
                    }

                    else{

                        free(v);
                        v=NULL;
                        tot=0;
                    }
                }
            }

            if(aux==0 && strcmp(fname, "")!=0){

                strcpy(temp,"Failed Authentication by ");
                strcat(user, fname);
                strcat(user2, fname);
                strcat(temp, user2);

                fputs(temp, log);
                fputs("\n", log);

                write(pass2, "F", 1);
                fclose(log);
                close(fd);
                close(fd1);
                close(pass);
                close(pass2);
                close(fd2);
                return(0);
            }
        }

        if(read(fd,fname,25)!=0){ //avaliar o pedido de informação

            if(strcmp(fname, "exit")==0 && strlen(fname)==4){ //terminar execução

                close(fd);
                close(fd1);
                return(0);
            }

            else if(fname[0]=='s' && fname[1]=='h' && fname[2]=='o' && fname[3]=='w'){ //devolver o conteúdo do ficheiro

                if(flag==0){

                    write(fd1, "`", 1);
                    continue;
                }

                fname[((int)strlen(fname))-1]='\0';

                strcpy(temp,"File content (\"");
                strcat(temp,&fname[5]);
                strcat(temp,"\") by ");
                strcat(temp,user2);

                fputs(temp, log);
                fputs("\n", log);

                fd2 = open(&fname[5], O_RDONLY);

                while(read(fd2, &fcontent, 1)!=0){
                
                    if(fd<0)
                        write(fd1, "ERRO! IMPOSSÍVEL APRESENTAR O CONTEÚDO DO FICHEIRO", 52);
                
                    else
                        write(fd1, &fcontent, 1);
                }

                write(fd1, &c , 1);
            }

            else if(fname[0]=='i' && fname[1]=='n' && fname[2]=='f' && fname[3]=='o'){ //devolver informações do ficheiro

                if(flag==0){

                    write(fd1, "`", 1);
                    continue;
                }

                fname[((int)strlen(fname))-1]='\0';

                strcpy(temp,"File information (\"");
                strcat(temp,&fname[5]);
                strcat(temp,"\") by ");
                strcat(temp,user2);

                fputs(temp, log);
                fputs("\n", log);

                fd2 = open(&fname[5], O_RDONLY);

                r = criaRelatorio(&fname[5]);

                write(fd1, r, strlen(r));
            }

            else if(fname[0]=='l' && fname[1]=='o' && fname[2]=='g'){ //aceder à informação guardada

                if(flag==0){

                    write(fd1, "`", 1);
                    continue;
                }

                if(user2[0]=='a' && user2[1]=='d' && user2[2]=='m' && user2[3]=='i' && user2[4]=='n'){ //só acessível a "admins"

                    log2 = open("log.txt", O_RDONLY);

                    while(read(log2, &fcontent, 1)!=0){
                
                        if(log2<0)
                            write(fd1, "ERRO! IMPOSSÍVEL APRESENTAR O CONTEÚDO DO FICHEIRO", 52);
                    
                        else
                            write(fd1, &fcontent, 1);
                    }

                    write(fd1, &c , 1);
                }

                else{

                    write(fd1, "?" , 1);
                }
            }

        }

    }

    fclose(log);
    close(fd);
    close(fd1);
    close(pass);
    close(pass2);
    close(fd2);
}