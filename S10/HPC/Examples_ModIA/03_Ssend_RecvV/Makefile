MPICC=smpicc
CFLAGS=-g -O4

all: Ssend_RecvV

clean:
	rm -f *.o Ssend_RecvV

%.o: %.c
	echo $@
	$(MPICC) -c -Wall -o $@ $< 

Ssend_RecvV: Ssend_RecvV.o
	$(MPICC) -o $@ $^ 

