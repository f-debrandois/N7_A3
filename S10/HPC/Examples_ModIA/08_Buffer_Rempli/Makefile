MPICC=smpicc
CFLAGS=-g -O4

all: Buffer_rempli

clean:
	rm -f *.o message_matching_Bsend

%.o: %.c
	echo $@
	$(MPICC) -c -Wall -o $@ $< 

Buffer_rempli: Buffer_rempli.o
	$(MPICC) -o $@ $^ 

