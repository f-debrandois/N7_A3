MPICC=smpicc
CFLAGS=-g -O4

all: MultAv

clean:
	rm -rf *.o MultAv

%.o: %.c
	echo $@
	$(MPICC) -c -Wall -o $@ $<

MultAv: MultAv.o
	$(MPICC) -o $@ $^ 
