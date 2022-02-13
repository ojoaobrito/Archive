#include "shell.h"

void execute (char **args, int nrArg) //wait 0 -> n espera
{
  int pid, status;

  //int waitaux; <- fazer aqui a função q verificava se era preciso
  //esperar ou n

  if ((pid = fork ()) < 0){
      perror ("forks");
      exit (1);
    }

  if (pid == 0){
//...


    execvp (*args, args);
    perror (*args);
    exit (1);
  }

  //if (!waitAux)
    while (wait (&status) != pid);
  
  return;
}
