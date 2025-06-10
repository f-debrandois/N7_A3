MPICC=smpicc
CFLAGS=-g -O4

all: ring

clean:
	rm -rf *.o ring

%.o: %.c
	echo $@
	$(MPICC) -c -Wall -o $@ $< 

ring: ring.o
	$(MPICC) -o $@ $^ 
