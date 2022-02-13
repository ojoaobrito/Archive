#include "cs.h"

int main(){

	char *s=NULL, *user=NULL, *limpar=(char*)malloc(25*sizeof(char)), *tempo=(char*)malloc(40*sizeof(char));
	char s1, s2, **info=NULL;
	int fd, fd1, k=0, pass, pass2, i;
	size_t buffer=40;

	//FIFO's de passagem de comandos
	fd = open("fifo1", O_WRONLY);
	fd1 = open("fifo2", O_RDONLY);

	//FIFO's de passagem de informação e pedidos de autenticação
	pass = open("fifo_pass", O_WRONLY);
	pass2 = open("fifo_pass2", O_RDONLY);

	while(1){

		printf("\n");

		if(k==0){ //autenticação

			printf("Enter username and password > ");
			getline(&user,&buffer,stdin);
			user[strlen(user)-1]='\0';
			write(pass, user, strlen(user));

			if(read(pass2, &s2, 1)!=0){

				if(s2=='F'){

					printf("Authentication denied!\n\n");
					break;
				}

				else{

					printf("OK, you're authorized for 5 minutes!");
					k=1;
					continue;
				}
			}
		}

		else{ //inserção de comandos

			printf("\nEnter prompt > ");
			getline(&s,&buffer,stdin);

			if(s[0]=='e' && s[1]=='x' && s[2]=='i' && s[3]=='t'){ //terminar execução

				write(fd,"exit", 4);
				printf("\n\n");
			    break;
			}

			else if(s[0]=='s' && s[1]=='h' && s[2]=='o' && s[3]=='w'){ //pedir ao servidor o conteúdo de um ficheiro

				write(fd, s, 25);

				read(fd1, &s1, 1);

		    	if(s1=='`'){

		    		printf("You ran out of time, please authenticate again!\n");
		    		user=NULL;
		    		buffer=40;
					k=0;
					continue;
		    	}

				printf("\n--- File Content ---\n\n");

				while(1){

			    	if(s1==EOF){
			    
			       		printf("\n\n");   
			       		break;
			    	}

			    	printf("%c",s1);
			    	read(fd1, &s1, 1);
				}

				//read(fd1, limpar, 25);
			}

			else if(s[0]=='i' && s[1]=='n' && s[2]=='f' && s[3]=='o'){ //pedir ao servidor informação relativa a um ficheiro

				write(fd, s, 25);

				limpar=(char*)realloc(limpar, 80*sizeof(char));

				read(fd1, limpar, 80);

				if(limpar[0]=='`'){

					printf("You ran out of time, please authenticate again!\n");
					user=NULL;
		    		buffer=40;
					k=0;
					continue;						
				}

				printf("\n--- File Information ---\n\n");
		    	printf("%s\n",limpar);
				
				//read(fd1, limpar, 25);
			}

			else if(s[0]=='l' && s[1]=='o' && s[2]=='g'){ //pedir ao servidor a informação guardada (log)

				write(fd, s, 25);
				read(fd1, &s1, 1);

				if(s1=='`'){

					printf("You ran out of time, please authenticate again!\n");
					user=NULL;
		    		buffer=40;
					k=0;
					continue;
				}

				if(s1=='?'){

					printf("Sorry, but you're not authorized to access this information!\n");
				}

				else{

					printf("\n--- Logged Information ---\n\n");

					while(1){

				    	if(s1==EOF){
				     
				       		break;
				    	}

				    	printf("%c",s1);

				    	read(fd1, &s1, 1);
					}
				}
			}
		}
	}
}