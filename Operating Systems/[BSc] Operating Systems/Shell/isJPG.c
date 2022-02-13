#include "shell.h"

int isJPG(int fd){

    char b[4];
    
    lseek(fd, 0, SEEK_SET);
    read(fd, b, 4);
    
    if(b[0]==0xff && b[1]==0xd8 && b[2]==0xff && b[3]==0xe0)
        return 1;
    
    return 0;
}