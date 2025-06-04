#include <stdio.h>
#include <stdlib.h>
#include <mpi.h>

int main(int argc, char* argv[]) {

  MPI_Init(&argc, &argv);

  int my_rank;
  MPI_Comm_rank(MPI_COMM_WORLD, &my_rank);

  // processor 1 sends its integer data x(=5) to processor 3
  // ...

  // processor 3 receives a integer from processor 1 in its data y and displays it
  // ...

  MPI_Finalize();

  return EXIT_SUCCESS;
}

