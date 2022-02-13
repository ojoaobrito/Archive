#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int expoente(int base, int expoente){

	int i=0, valor=1;

	if(expoente==0)
		return(1);

	for(i=0; i<expoente; i++){

		valor=(valor*base);
	}

	return(valor);
}

int* removeEspacos(int base, char *s, int *size){

	int i=0, k=0, temp=0, tot=0, *v=NULL, aux=0;
	char *aux2=NULL;

	if(base==16){

		for(i=0; i<strlen(s)-1; i++){

			if(s[i]!=' '){

				aux2=(char*)realloc(aux2,(++aux)*sizeof(char));
				aux2[aux-1]=s[i];
			}

			else if(s[i]==' ' || s[i]=='\0' || s[i]=='\n'){ //se encontrarmos um espaço, "\0" ou "\n", então vamos guardar os carateres anteriores no vetor de inteiros

				v=(int*)realloc(v,(++tot)*sizeof(int));

				for(k=0; k<aux; k++){

					if((int)aux2[k]>57) //se o carater for uma letra então está mais à frente na tabela ASCII, pelo que temos de subtrair 87
						temp=(temp+(((int)aux2[k])-87)*(expoente(16,aux-1-k)));
					
					else //se for número basta fazer o que já fizeste antes e subtrair 48
						temp=(temp+(((int)aux2[k])-48)*(expoente(16,aux-1-k)));
				}

				v[tot-1]=temp;
				aux=0;
				temp=0;
			}
		}

		v=(int*)realloc(v,(++tot)*sizeof(int));

		for(k=0; k<aux; k++){

			if((int)aux2[k]>57)
				temp=(temp+(((int)aux2[k])-87)*(expoente(16,aux-1-k)));
					
			else
				temp=(temp+(((int)aux2[k])-48)*(expoente(16,aux-1-k)));
		}

		v[tot-1]=temp;

		*size=tot; //atualizar o tamanho deste vetor de inteiros e enviar essa informação para a função main

		free(aux2);
		return(v);
	} 

	for(i=0; i<strlen(s)-1; i++){

		if(s[i]!=' ')
			temp=(temp*10 + (((int)s[i])-48));
		
		else if(s[i]==' ' || s[i]=='\0' || s[i]=='\n'){

			v=(int*)realloc(v,(++tot)*sizeof(int));
			v[tot-1]=temp;
			temp=0;
		}
	}

	v=(int*)realloc(v,(++tot)*sizeof(int));
	v[tot-1]=temp;

	*size=tot;
	return(v);
}

int resultado(char operacao, int *s, int size){

	int i=0, temp=0;

	if(operacao=='+'){

		for(i=0; i<size; i++)
			temp=(temp+s[i]);

		return(temp);
	}

	else{

		temp=1;

		for(i=0; i<size; i++)
			temp=(temp*s[i]);

		return(temp);
	}
}

int main(int argc, char *argv[]){

	FILE **f=NULL;
	size_t buffer=0;
	int i=1, j=0, k=0, base=10, ftot=0, *num=NULL, size=0, tamanho=0;
	char operacao='+', *s=NULL;

	while(i!=argc){ //guardar a base e a operação a executar

		if(argv[i][0]=='-' && argv[i][1]=='b'){

			if(argv[i][6]=='1'){

				base=((((int)argv[i][6])-48)*10)+(((int)argv[i][7])-48);
			}
		
			else{

				base=(((int)argv[i][6])-48);
			}

			i++;
		}

		else if(argv[i][0]=='-'){

			operacao=argv[i][4];
			i++;
		}

		else
			break;
	}

	while(i!=argc){ //ver se há ficheiros para abrir

		f=(FILE**)realloc(f,(++ftot)*sizeof(FILE*));
		f[ftot-1]=NULL;
		f[ftot-1]=fopen(argv[i],"r");

		if(f[ftot-1]==NULL){

			printf("File Not Found %s\n",argv[i]);
			return(0);
		}

		i++;
	}

	if(f==NULL){

		while(getline(&s,&buffer,stdin)!=(-1)){

			if(s[strlen(s)-1]!='\n'){

				tamanho=strlen(s);

				s=(char*)realloc(s,(tamanho+1)*sizeof(char));
				s[tamanho+1]='\0';
				s[strlen(s)]='\n';
			}

			num=removeEspacos(base,s,&size);

			if(base==8)
				printf("%o\n",resultado(operacao,num,size));

			else if(base==10)
				printf("%d\n",resultado(operacao,num,size));

			else if(base==16)
				printf("%x\n",resultado(operacao,num,size));

		}

		return(0);
	}

	else{

		for(k=0; k<ftot; k++){

			while(getline(&s,&buffer,f[j])!=(-1)){

				if(s[strlen(s)-1]!='\n'){

					tamanho=strlen(s);

					s=(char*)realloc(s,(tamanho+1)*sizeof(char));
					s[tamanho+1]='\0';
					s[strlen(s)]='\n';
				}

				num=removeEspacos(base,s,&size);

				if(base==8)
					printf("%o\n",resultado(operacao,num,size));

				else if(base==10)
					printf("%d\n",resultado(operacao,num,size));

				else if(base==16)
					printf("%x\n",resultado(operacao,num,size));
			}

		}

		return(0);
	}

	for(i=0; i<ftot; i++)
		fclose(f[i]);

	free(f);
	free(num);
	return(0);
}