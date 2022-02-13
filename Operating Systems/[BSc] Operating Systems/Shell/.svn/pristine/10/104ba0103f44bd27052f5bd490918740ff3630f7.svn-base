#include "shell.h"

char prompt[100];

int main ()
{
  int len;
  char buf[1024];		/* um comando */
  char *args[64];		/* com um maximo de 64 argumentos */

  strcpy (prompt, "SOSHELL: Introduza um comando : prompt>");

  while (1)
    {
      printf ("%s", prompt);

      if ( fgets(buf,1023,stdin) == NULL)
	{
	  printf ("\n");
	  exit (0);
	}
	len=strlen(buf);
	if ( 1==len ) continue;  // string is only a barra n
	if ( buf[len-1] == '\n' ) buf[len-1] ='\0';
	
        parse (buf, args);	/* particiona a string em argumentos */

        if (!builtin (args))
	  execute (args);		/* executa o comando */
    }
  return 0;
}

int builtin (char **args)
{
  if (strcmp (args[0], "sair") == 0)
    {
      exit (0);
      return 1;
    }
/*
  if (strcmp (args[0], "qualquercoisa") == 0)
    {
       funcinalidade
       return 1;
    }

   if ( strcmp(args[0],"socp")==0) { socp(..,..) open/creat/read/write ; return 1; }
*/

//devolver 0 indique que não há comnando embutido

  return 0;
}
