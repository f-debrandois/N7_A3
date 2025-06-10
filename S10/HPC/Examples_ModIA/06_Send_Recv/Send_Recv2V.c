#include <stdio.h>
#include <stdlib.h>
#include <mpi.h>

int main(int argc, char* argv[]) {

  const int buffer_size = 10000;

  MPI_Status status;
  int x[buffer_size] ;
  int y[buffer_size] ;

  for(int i = 0; i < buffer_size; i++){
    x[i] = i;
  }

  MPI_Init(&argc, &argv);

  int size;
  MPI_Comm_size(MPI_COMM_WORLD, &size);

  int my_rank;
  MPI_Comm_rank(MPI_COMM_WORLD, &my_rank);

  if(my_rank == 1) {

    printf("MPI process %d sends value %d.\n", my_rank, x[10]);
    MPI_Send(x, buffer_size, MPI_INT, 3, 0, MPI_COMM_WORLD);

    MPI_Recv(y, buffer_size, MPI_INT, 3, 1, MPI_COMM_WORLD, &status);
    printf("MPI process %d received value %d.\n", my_rank, y[100]);

  } else if(my_rank == 3) {

    printf("MPI process %d sends value %d.\n", my_rank, x[100]);
    MPI_Send(x, buffer_size, MPI_INT, 1, 1, MPI_COMM_WORLD);

    MPI_Recv(y, buffer_size, MPI_INT, 1, 0, MPI_COMM_WORLD, &status);
    printf("MPI process %d received value %d.\n", my_rank, y[10]);

  }

  MPI_Finalize();

  return EXIT_SUCCESS;
}

