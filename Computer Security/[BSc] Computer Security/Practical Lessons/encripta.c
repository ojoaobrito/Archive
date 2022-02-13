#include <stdio.h>

void encrypt(char *in, char *out, char *key, int size){

	int i = 0;

	for(i=0; i<size; i++){

		int iFound = 0;
		int j = 0;

		while(iFound==0){

			if(in[i]==key[j])
				iFound=1;

			else
				j++;
		}

		out[i] = key[26+j];
	}
}

void decrypt(char *in, char *out, char *key, int size){

	int i = 0;

	for(i=0; i<size; i++){

		int iFound = 0;
		int j = 26;

		while(iFound==0){

			if(in[i]==key[j])
				iFound=1;

			else
				j++;
		}

		out[i] = key[j-26];
	}
}

int main(){

	char key[2*26] = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
						'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
					  'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
					  'S', 'Q', 'T', 'U', 'H', 'J', 'I', 'B', 'Y', 'K',
						'A', 'V', 'L', 'C', 'W', 'E', 'Z', 'N' ,'R',
					  'M', 'X', 'G', 'F', 'P', 'D', 'O'};

	char plaintext[12] = "OLACOMOESTA";
	char ciphertext[12] = "XXXXXXXXXXX";
	char plaintext2[12] = "XXXXXXXXXXX";

	printf("%s\n",plaintext);
	encrypt(plaintext,ciphertext,key,11);
	printf("%s\n",ciphertext);
	decrypt(ciphertext,plaintext2,key,11);
	printf("%s\n",plaintext2);
}