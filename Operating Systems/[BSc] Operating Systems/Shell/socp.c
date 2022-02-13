#include "shell.h" //FICHA 7 alterar stin stdout e altera makeFILE //quem sou eu, prompt, copy

#define BUFFSIZE 128
void socp(int fdin,int fdout){
	//FICHAT7
	//copy/paste 7.2
	int n;
	char    buf[BUFFSIZE];
	while ((n = read(fdin, buf, BUFFSIZE)) > 0){
		fprintf(stderr, "\n*** N=%d dados lidos ***\n",n);
		if (write(fdout, buf, n) != n)
			perror("Erro de escrita!\n");
        }
	if (n < 0)
		perror("Erro de leitura!\n");
}
