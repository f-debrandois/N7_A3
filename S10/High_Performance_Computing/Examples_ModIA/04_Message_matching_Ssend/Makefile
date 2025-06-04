MPICC=smpicc
CFLAGS=-g -O4

all: message_matching_Ssend

clean:
	rm -f *.o message_matching_Ssend

%.o: %.c
	echo $@
	$(MPICC) -c -Wall -o $@ $< 

message_matching_Ssend: message_matching_Ssend.o
	$(MPICC) -o $@ $^ 

