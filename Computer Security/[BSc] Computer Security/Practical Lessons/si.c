 #include <stdio.h>
 #include <stdlib.h>

void encrypt(char *in, char *out, unsigned int ikey){

    char b;

    FILE *fin = fopen(in,"r");
    FILE *fout = fopen(out,"w");

    if(fin==fout)
        fprintf(stderr,"Deu bosta, abortar já!!");

    srand(ikey); //inicializar o gerador de números aleatórios

    while(!feof(fin)){

        b = fgetc(fin);
        b = b ^ rand(); //fazer o xor (" ^ ") com a chave aleatória gerada
        fputc(b,fout);
    }

    printf("\n");

    fclose(fin);
    fclose(fout);
}

 int main(){

     unsigned int ikey = 123456789;
     srand(ikey);
     int i;

     for(i=0; i<1000; i++){

         printf("%u\n",(unsigned int)rand());
     }

     encrypt("plaintext.txt","ciphertext.txt",123456789);
     encrypt("ciphertext.txt","plaintext2.txt",123456789);

     return(0);
 }
