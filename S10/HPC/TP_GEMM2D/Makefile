CC=gcc
MPICC=smpicc
LD=smpicc
LDFLAGS=
CFLAGS=-O4
CLIBS=-lblas -llapack 
INCLUDES=
SOURCEDIR=src
BUILDDIR=build

all: dir main # test 

test_env: dir who_am_i

dir:
	mkdir -p $(BUILDDIR)/bin

clean:
	rm -rf $(BUILDDIR)

%.o: $(SOURCEDIR)/%.c
	echo $@
	$(MPICC) -c -Wall -o $(BUILDDIR)/$@ $< $(CFLAGS) $(INCLUDES)

main: main.o gemms.o ex1.o ex2.o ex3.o utils.o dsmat.o
	$(LD) -o $(BUILDDIR)/bin/$@ $(addprefix $(BUILDDIR)/,$^) $(CLIBS) $(LDFLAGS)
