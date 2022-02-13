#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <sys/types.h> //biblioteca com as funções open(), creat(), ...
#include <sys/stat.h> //" " " "
#include <fcntl.h> //biblioteca com as flags e permissões
#include <unistd.h> //biblioteca com as funções close(), read(), write(), ... 
#include <dirent.h> //biblioteca com as funções/ferramentas de manipulação de diretorias 

typedef struct{

	char *tamanho; //tamanho dos ficheiros
	char *blocks; //blocks usados
	char *user_permissions; //permissões de utilizador
	char *group_permissions; //permissões de grupo
	char *other_permissions; //outras permissões
	char *ficheiros; //veredito final

}Relatorio;

Relatorio* criarRelatorio(struct stat fprop1, struct stat fprop2){

	int i=0, controlo=0;
	mode_t *permissoes=NULL;
	Relatorio *relatorio=(Relatorio*)malloc(sizeof(Relatorio));

	relatorio->ficheiros="Ficheiros Igual\n";

	if(((int)fprop1.st_size)!=((int)fprop2.st_size)){

		relatorio->tamanho="Tamanho Diferente\n";
		relatorio->ficheiros="Ficheiros Diferente\n";
	}

	else	
		relatorio->tamanho="Tamanho Igual\n";

	if(((int)fprop1.st_blocks)!=((int)fprop2.st_blocks)){

		relatorio->blocks="Blocks Usados Diferente\n";
		relatorio->ficheiros="Ficheiros Diferente\n";
	}

	else
		relatorio->blocks="Blocks Usados Igual\n";

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

	for(i=0; i<3; i++){ //permissões de utilizador

		((fprop1.st_mode & permissoes[i])==(fprop2.st_mode & permissoes[i]))?(controlo=1):(controlo=0);			
		
		if(controlo==0){

			relatorio->user_permissions="User Permissions Diferente\n";
			relatorio->ficheiros="Ficheiros Diferente\n";
			break;
		}

		if(i==2){

			relatorio->user_permissions="User Permissions Igual\n";
			break;
		}
	}

	for(i=3; i<6; i++){ //permissões de grupo

		((fprop1.st_mode & permissoes[i])==(fprop2.st_mode & permissoes[i]))?(controlo=1):(controlo=0);			
		
		if(controlo==0){

			relatorio->group_permissions="Group Permissions Diferente\n";
			relatorio->ficheiros="Ficheiros Diferente\n";
			break;
		}

		if(i==5){

			relatorio->group_permissions="Group Permissions Igual\n";
			break;
		}
	}

	for(i=6; i<9; i++){ //outras permissões

		((fprop1.st_mode & permissoes[i])==(fprop2.st_mode & permissoes[i]))?(controlo=1):(controlo=0);			
		
		if(controlo==0){

			relatorio->other_permissions="Other Permissions Diferente\n";
			relatorio->ficheiros="Ficheiros Diferente\n";
			break;
		}

		if(i==8){

			relatorio->other_permissions="Other Permissions Igual\n";
			break;
		}
	}

	return(relatorio);
}

int main(int argc, char *argv[]){

	int i=0, fd1=0, fd2=0, contador1=0, contador2=0;
	char ficheiro1[100], ficheiro2[100], elemento1[100], elemento2[100];
	struct stat fprop1, fprop2;
	struct dirent **diretoria1, **diretoria2;
	Relatorio *relatorio=NULL;

	scanf("%s %s",ficheiro1,ficheiro2);

	if(strcmp(ficheiro1,ficheiro2)==0){ //ficheiros iguais

		printf("Nomes Iguais\n");
		return(0);
	}

	fd1=open(ficheiro1,O_RDONLY); //abrir o primeiro ficheiro
	fd2=open(ficheiro2,O_RDONLY); //abrir o segundo ficheiro

	if(fstat(fd1, &fprop1)!=0 || fstat(fd2, &fprop2)!=0){ //cria uma estrutura com propriedades de cada ficheiro ("fprop1" e "fprop2")
		
		printf("Erro\n");
		free(relatorio);
		close(fd1);
		close(fd2);
		return(0);		
	}

	if(S_ISREG(fprop1.st_mode)==1 && S_ISREG(fprop2.st_mode)==1){ //se os 2 ficheiros forem regulares
		
		relatorio=criarRelatorio(fprop1,fprop2);
		printf("%s",relatorio->tamanho);
		printf("%s",relatorio->blocks);
		printf("%s",relatorio->user_permissions);
		printf("%s",relatorio->group_permissions);
		printf("%s",relatorio->other_permissions);
		printf("%s",relatorio->ficheiros);
	}

	else if(S_ISDIR(fprop1.st_mode)==1 && S_ISDIR(fprop2.st_mode)==1){ //se os 2 inputs forem diretorias
	
		contador1=scandir(ficheiro1, &diretoria1, NULL, alphasort);
		contador2=scandir(ficheiro2, &diretoria2, NULL, alphasort);
	
		if(contador1!=contador2){ //se as diretorias não tiverem o mesmo número de ficheiros

			printf("Directories Differente\n");
			free(relatorio);
			return(0);
		}

		if(contador1==(-1) || contador2==(-1)){ //se ocorrer algum erro

			printf("Erro\n");
			free(relatorio);
			return(0);
		}

		for(i = 0; i < contador1; i++){

    		if(((strcmp(".", diretoria1[i]->d_name)==0) && (strcmp(".", diretoria2[i]->d_name)==0)) || ((strcmp("..", diretoria1[i]->d_name)==0) && (strcmp("..", diretoria2[i]->d_name)==0))) //ignorar estes ficheiros
    			continue;

    		elemento1[0] = '\0'; //ficheiro da primeira diretoria
    		elemento2[0] = '\0'; //ficheiro da segunda diretoria

    		strcat(elemento1, ficheiro1);
    		strcat(elemento2, ficheiro2);

    		strcat(elemento1, "/");
    		strcat(elemento2, "/");

    		strcat(elemento1, diretoria1[i]->d_name);
    		strcat(elemento2, diretoria2[i]->d_name);

    		stat(elemento1, &fprop1);
    		stat(elemento2, &fprop2);

    		if(S_ISREG(fprop1.st_mode)==1 && S_ISREG(fprop2.st_mode)==1){

    			relatorio=criarRelatorio(fprop1,fprop2);

    			if(strcmp(relatorio->ficheiros,"Ficheiros Igual\n")==0){

    				free(diretoria1[i]);
    				free(diretoria2[i]);
    			}

    			else{

    				printf("Directories Differente\n");
    				free(relatorio);
    				free(diretoria1);
    				free(diretoria2);
    				return 0;
    			}
    		}
    	}

    	printf("Directories Igual\n");
    	free(relatorio);
    	free(diretoria1);
    	free(diretoria2);
    	return(0);
	}

	else
		printf("Erro\n");

	free(relatorio);
	close(fd1);
	close(fd2);
	return(0);
}