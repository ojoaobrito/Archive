#include "shell.h"

#define FLAG S_IRUSR

char prompt[100];

int ultimo(char **args, int numargs){

    if (args[numargs-1][0]=='&'){
        
        args[numargs-1]=NULL;
        return(BG);
    }

    return(FG);
}

int containsPipe(int numArgs, char **args){ //ver se o input contém pipes

    int indice=0;
    
    for(indice=0; indice<numArgs; indice++){

        if (args[indice][0]=='|')
            return(indice);
    }

    return(-1);
}

int main(int argc, char **argv){

    int numArgs=0; //número de argumentos
    int comp=0; //comprimento do comando
    int indice=(-1); //para a função "containsPipe"
    char buf[1024]; // um comando
    char *args[64]; // máximo de 64 argumentos

    if(strlen(prompt)==0)
        strcpy (prompt,"SOSHELL: Introduza um comando> ");

    while (1){

        printf("%s",prompt);
        
        if(fgets(buf,1023,stdin)==NULL){ //se der NULL, houve algum erro
            
            printf("\n");
	        exit(0);
        }

        comp=strlen(buf);
        
        if(comp==1) 
            continue;  // string is only a barra n

        if(buf[comp-1]=='\n') 
            buf[comp-1]='\0';
    
        numArgs=parse(buf,args); //particionar o input em vários argumentos

        if(ultimo(args,numArgs)==0){
            
            if(builtin(args,numArgs)==0) //não é uma funcionalidade embutida no nosso shell
                execute(args,0);
        }
    
        else{

            indice=containsPipe(numArgs,args);
            
            if (indice==(-1)){
                
                if(builtin(args,numArgs-1)==0)
                    execute(args,1);
            }

            else
                pipe1(args,numArgs,indice);
        }
    }

    return(0);
}

int builtin (char **args, int numArgs){

    if(strcmp(args[0],"sair")==0 || strcmp(args[0],"exit")==0)  //sair do shell
    	exit(0);

    if(strcmp(args[0],"aviso")==0){
    	
    	pthread_t th;
    	aviso_t *ptr = (aviso_t *)malloc(sizeof(aviso_t));
    	strcpy(ptr->msg, args[1]);
    	ptr->tempo = atoi(args[2]);
    	pthread_create(&th, NULL, avisowrapper, (void*)ptr);
    	return 1;
  	}

    if((numArgs+1)>1 && (strcmp(args[1],">")==0 || strcmp(args[1],"<")==0 || strcmp(args[1],"2>")==0 || strcmp(args[1],">>")==0)){

    	redirects(numArgs+1,args);
        return(1);   
    }

    if(strcmp(args[0],"whoami")==0){ //mostrar qual é o utilizador atual
	    
	    system("whoami");
	    return(1);
	}

	if(strncmp(args[0],"PS1=",4)==0){ //mudança de prompt
		
		strcpy(prompt,strcat(args[1]," "));
		return(1);
	}

    if(strcmp(args[0],"42")==0){ //42 é a resposta para tudo

    	printf("42 is the answer to life the universe and everything\n");
    	return(1); // funcionalidade embutida
    }

	if(strcmp(args[0],"cd")==0){ //mudar de diretoria
    
		int aux;
    
    	if((args[1]==NULL) || (!strcmp(args[1], "~")))
      		aux=chdir(getenv("HOME"));
    
    	else
      		aux=chdir(args[1]);
    
    	if(aux<0)
      		fprintf(stderr, "ERRO! NÃO FOI POSSÍVEL MUDAR DE DIRETORIA\n");

    	return(1);
    }

	if(strcmp(args[0], "calc")==0){ //realizar operações entre 2 números reais

    	if((numArgs+1)==4)
      		calc(args);
    
    	else
      		fprintf(stderr, "ERRO! VALORES INVÁLIDOS\n");
    
    	return(1);
	}

	if(strcmp(args[0],"bits")==0){ //realizar operações entre 2 conjuntos de bits

    	if ((numArgs+1)==4)
    		bits(args);
    
    	else
     	 	printf("Bits invalid\n");
    
    	return(1);
  	}

	if(strcmp(args[0],"isJPG")==0){ //avaliar se um dado ficheiro é JPEG ou não

    	if((numArgs+1)==2){
      
        	int fd=open(args[1],O_RDONLY);
      
        	if(fd>0){
        
            	if(isJPG(fd))
            		printf("É um ficheiro JPG/JPEG\n");

            	else
                	printf("Não é um ficheiro JPG/JPEG\n");
        	}

        	else
            	fprintf(stderr, "ERRO! FICHEIRO INVÁLIDO\n");
    		}

    	else
      		fprintf(stderr, "ERRO! FICHEIRO INVÁLIDO\n");
    
    	return(1);
	}

    if(strcmp(args[0], "sols")==0){ //listar o conteúdo de uma diretoria (+ PODEROSO QUE O "ls")
    
    	sols(numArgs,args);
    	return(1);
	}

	if(strcmp(args[0], "socp")==0){
    
		int fd1=open(args[1],O_RDONLY), fd2=open(args[2],O_RDONLY);

    	socp(fd1,fd2);
    	return(1);
	}

    return(0);
}