CC = cc
FLAGS= -c -Wall
LIBS= -lm -lpthread


all: client server


client : $(OBJS)
	$(CC) -o client client.c $(LIBS)


server : $(OBJS)
	$(CC) -o server server.c $(LIBS)


clean limpar:
		rm -f server *.o
		rm -f client *.o

