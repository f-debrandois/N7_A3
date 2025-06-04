MPICC=smpicc
CFLAGS=-g -O4

all: message_matching_Bsend

clean:
	rm -f *.o message_matching_Bsend

%.o: %.c
	echo $@
	$(MPICC) -c -Wall -o $@ $< 

message_matching_Bsend: message_matching_Bsend.o
	$(MPICC) -o $@ $^ 

