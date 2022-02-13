#include<stdio.h>
#include<stdlib.h>

void alterbyte(char * in, char * out, int ibytenumber){

  FILE *fIN, *fOUT;
  fIN  = fopen(in,  "r");
  fOUT = fopen(out, "w");
  if( (fIN == NULL) | (fOUT == NULL) ) {
    fprintf(stderr, "Problem with file\n");
    exit(1);
  }

  int b, i = 1;
  b = fgetc(fIN);
  while (!feof(fIN)) {
    if(i == ibytenumber)
      b = b ^ 0x01;
    fputc(b, fOUT);
    b = fgetc(fIN);
    i++;
  }
  fclose(fIN);
  fclose(fOUT);
}

int main(int argc, char **argv){
  alterbyte(argv[1],argv[2],atoi(argv[3]));
}
