MPICC=smpicc
CFLAGS=-g -O4

all: Ssend_Recv

clean:
	rm -f *.o Ssend_Recv

%.o: %.c
	echo $@
	$(MPICC) -c -Wall -o $@ $< 

Ssend_Recv: Ssend_Recv.o
	$(MPICC) -o $@ $^ 

