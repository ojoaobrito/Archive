#include <openssl/des.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void enc_des_ecb(char *entrada, char *chave, char *saida){

    // devido ao uso de cifras, trabalhamos em modo binário
    FILE *in = fopen(entrada,"rb");
    FILE *out = fopen(saida,"wb");
    int bit;

    // inicializar a cifra
    DES_cblock Key2;
    DES_key_schedule schedule;
    const_DES_cblock bIn;
    DES_cblock bOut;

    // de forma "vanilla" podemos ter arrays de 8 elementos (64 bits)
    // unsigned char bIn[8];
    // unsigned char bOut[8];

    if(in==NULL || out==NULL){

        fprintf(stderr,"Erro na abertura dos ficheiros!\n");
        exit(1);
    }

    // 1. Inicializar a cifra
    memcpy(Key2,chave,8); // garantir que a chave tem mesmo 64 bits
    DES_set_odd_parity(&Key2);
    DES_set_key_checked(&Key2,&schedule); //expandir a chave

    // 2. Ler ficheiro de entrada bloco a bloco (8 bytes de cada vez)
    while(!feof(in)){

        fread(bIn,8,1,in); // ler o bloco
        DES_ecb_encrypt(&bIn,&bOut,&schedule,DES_ENCRYPT); // cifrar o bloco
        fwrite(&bOut,8,1,out); // cifro o bloco
    }

    fclose(in);
    fclose(out);
}

void dec_des_ecb(char *entrada, char *chave, char *saida){

    // devido ao uso de cifras, trabalhamos em modo binário
    FILE *in = fopen(entrada,"rb");
    FILE *out = fopen(saida,"wb");
    int bit;

    // inicializar a cifra
    DES_cblock Key2;
    DES_key_schedule schedule;
    const_DES_cblock bIn;
    DES_cblock bOut;

    // de forma "vanilla" podemos ter arrays de 8 elementos (64 bits)
    // unsigned char bIn[8];
    // unsigned char bOut[8];

    if(in==NULL || out==NULL){

        fprintf(stderr,"Erro na abertura dos ficheiros!\n");
        exit(1);
    }

    // 1. Inicializar a cifra
    memcpy(Key2,chave,8); // garantir que a chave tem mesmo 64 bits
    DES_set_odd_parity(&Key2);
    DES_set_key_checked(&Key2,&schedule); //expandir a chave

    // 2. Ler ficheiro de entrada bloco a bloco (8 bytes de cada vez)
    while(!feof(in)){

        fread(bIn,8,1,in); // ler o bloco
        DES_ecb_encrypt(&bIn,&bOut,&schedule,DES_DECRYPT); // decifrar o bloco
        fwrite(&bOut,8,1,out); // cifro o bloco
    }

    fclose(in);
    fclose(out);
}

int main(int argc, char**argv){

    char *entrada=NULL;
    char *saida=NULL;

    if(argc==5){

        entrada=argv[2];
        saida=argv[4];

        if(strcmp(argv[1],"-e")==0)
            enc_des_ecb(argv[2],argv[3],argv[4]);


        else
            dec_des_ecb(argv[2],argv[3],argv[4]);
    }

    else{

        fprintf(stderr,"Erro nos parâmetros!\n");
        exit(1);
    }

    return(0);
}
