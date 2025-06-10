MPICC=smpicc
CFLAGS=-g -O4

all: dotp

clean:
	rm -rf *.o dotp

%.o: %.c
	echo $@
	$(MPICC) -c -Wall -o $@ $<

dotp: dotp.o
	$(MPICC) -o $@ $^  -lm
