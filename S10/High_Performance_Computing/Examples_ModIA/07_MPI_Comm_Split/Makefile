MPICC=smpicc
CFLAGS=-g -O4

all: MPI_Comm_split

clean:
	rm -f *.o MPI_Comm_split

%.o: %.c
	echo $@
	$(MPICC) -c -Wall -o $@ $< 

MPI_Comm_split: MPI_Comm_split.o
	$(MPICC) -o $@ $^ 

