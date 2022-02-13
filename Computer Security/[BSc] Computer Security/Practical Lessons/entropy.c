#include <stdio.h>
#include <math.h>

int main(int argc, char *argv[])
{
         FILE *fp;

         fp = fopen ( argv[1],"r" ) ;
         if( fp == NULL )
         {
               puts ( "cannot open file" ) ;
         }

	char ch = 1;
	unsigned char ch1 = 0;
	int iCounter = 0;
	int iaProbs[255];
	int i = 0;
	for(; i < 255; i++)
		iaProbs[i] = 0;

        while ( !feof( fp ) )
        {
                ch = fgetc ( fp ) ;
		iCounter++;
		ch1 = (unsigned char) ch;
		iaProbs[ch1]++;
		// printf("%d\n", iaProbs[ch1]);
        }

	i = 0;
	double f = 0;
	double dPr = 0;
	for(; i < 255; i++){
		dPr = (double) iaProbs[i]/ (double)iCounter;
		if(dPr > 0)
			f -= dPr * log((float) dPr);
	}


	printf("\n\tThe entropy value for file %s is\n\n \t\t\t%f \n", argv[1],f );
	printf("\n\tThe max value is %f \n\n", log((double)256) );
    fclose ( fp ) ;
}
