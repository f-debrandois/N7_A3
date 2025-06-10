MPICC=smpicc
CFLAGS=-g -O4

all: Send_Recv2V

clean:
	rm -f *.o Send_Recv2V

%.o: %.c
	echo $@
	$(MPICC) -c -Wall -o $@ $< 

Send_Recv2V: Send_Recv2V.o
	$(MPICC) -o $@ $^ 

