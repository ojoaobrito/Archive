#include "shell.h"

/*
    parse . particiona o comando Unix (armazenado em buf) em argumentos
*/

void parse (char *buf, char **args)
{
  while ('\0' != *buf)
    {
      /* strip whitespace. Usa um NULL para indicar que o argumento anterior e. o ultimo */
      while (isspace((unsigned char)*buf))
	*buf++ = '\0';

      *args++ = buf;		/* salvaguarda argumento */

      while ((*buf != '\0') && (!isspace((unsigned char)*buf)))	/* salta sobre o argumento */
	buf++;
    }
  *args = (char *) NULL;	/* o ultimo argumento e. NULL */
  return;
}
