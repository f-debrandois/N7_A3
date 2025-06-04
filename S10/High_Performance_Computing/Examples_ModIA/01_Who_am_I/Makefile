MPICC=smpicc
CFLAGS=-g -O4

all: who_am_i

clean:
	rm -f *.o who_am_i

%.o: %.c
	echo $@
	$(MPICC) -c -Wall -o $@ $< 

who_am_i: who_am_i.o
	$(MPICC) -o $@ $^ 

