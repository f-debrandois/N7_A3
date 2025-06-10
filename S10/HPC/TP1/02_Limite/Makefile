MPICC=smpicc
CFLAGS=-g -O4

all: limite

clean:
	rm -rf *.o limite

%.o: %.c
	echo $@
	$(MPICC) -c -Wall -o $@ $< 

limite: limite.o
	$(MPICC) -Dhave_mpi -o $@ $^ 
