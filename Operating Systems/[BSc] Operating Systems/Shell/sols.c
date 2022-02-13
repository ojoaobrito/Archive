#include "shell.h"

int sols(int argc, char **argv){
	
	DIR *dp;
	struct dirent *dirp;
	struct stat s;

	if(argc!=2)
		fprintf(stderr, "Usage: %s Um argumento é necessário\n", argv[0]);

	if((dp=opendir(argv[1]))==NULL)
		fprintf(stderr, "Impossível abrir diretoria %s\n", argv[1]);

	while((dirp=readdir(dp))!=NULL){

		stat(dirp->d_name, &s);

		if((s.st_mode & S_IFREG)==S_IFREG)
			printf("%s %ld\n",dirp->d_name,(long int)s.st_size);

		else
			printf("%s\n",dirp->d_name);
	}

	closedir(dp);
	return(0);
}