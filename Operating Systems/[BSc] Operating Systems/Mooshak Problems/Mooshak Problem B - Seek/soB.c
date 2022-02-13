#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h> //biblioteca com as funções open(), creat(), ...
#include <sys/stat.h> //" " " "
#include <fcntl.h> //biblioteca com as flags e permissões
#include <unistd.h> //biblioteca com as funções close(), read(), write(), ... 

int main(int argc, char *argv[]){

	int fd, stot=0, i, numero=0; //file descriptor, ou seja, um identificador de um ficheiro
	char carater, *s=NULL, aux[1];
	const char newline='\n';

	fd=open(argv[1],O_RDONLY); //abrir ficheiro para leitura

	if(fd==-1)
		return(0);

	while(1){

		scanf(" %c %d",&carater,&numero); //o espaço inicial ignora as tabulações e espaços em branco anteriores

		if(carater=='l'){ //apagar o conteúdo da string

			free(s);
			s=NULL;
			stot=0;
		}

		if(carater=='s' && numero==0){ //parar as instruções

			write(STDOUT_FILENO,s,(stot)); //imprimir a string final no ecrã
			write(STDOUT_FILENO,&newline,1); //imprimir o "\n"
			free(s);
			close(fd);
			return(0);
		}

		else if(carater=='r'){

			for(i=0; i<numero; i++){

				if(read(fd,aux,1)==0)
					break;

				s=(char*)realloc(s,(++stot)*sizeof(char));
				s[stot-1]=(*aux);
			}
		}

		else{

			if(carater=='+' || carater=='i'){

				if(carater=='i')
					lseek(fd,0,SEEK_SET);

				lseek(fd,numero,SEEK_CUR);
			}

			else{

				if(carater=='f')
					lseek(fd,0,SEEK_END);

				lseek(fd,-numero,SEEK_CUR);
			}
		}
	}
}