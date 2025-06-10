CC=gcc
MPICC=smpicc
CFLAGS=-g -O4

all: CG_par CG_sq

clean:
	rm -rf *.o CG_par CG_sq

%.o: %.c
	echo $@
	$(MPICC) -c -Wall -o $@ $<

CG_par: util.o CG_par.o main_par.o
	$(MPICC) -o $@ $^  -lm

CG_sq: util.o CG_sq.o main_sq.o
	$(MPICC) -o $@ $^  -lm
