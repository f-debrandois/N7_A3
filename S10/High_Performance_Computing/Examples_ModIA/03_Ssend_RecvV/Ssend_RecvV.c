#include <stdio.h>
#include <stdlib.h>
#include <mpi.h>

int main(int argc, char* argv[]) {

  MPI_Init(&argc, &argv);

  int my_rank;
  MPI_Comm_rank(MPI_COMM_WORLD, &my_rank);

  // processor 1 sends 10 integers stored in the vector x to processor 3
  // ...

  // processor 3 receives 10 integers from processor 1 in its vector y and displays y
  // ...

  MPI_Finalize();

  return EXIT_SUCCESS;
}

