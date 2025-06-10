#include <stdio.h>
#include <stdlib.h>
#include <mpi.h>

int main( int argc, char *argv[] ) {

  int value;
  int my_rank, size;
  int previous, next;
  MPI_Status status;

  MPI_Init (NULL, NULL);

  // Get number of processes
  MPI_Comm_rank (MPI_COMM_WORLD, &my_rank);
  MPI_Comm_size (MPI_COMM_WORLD, &size);

  // determine my neighbors according to my rank
  previous = (my_rank - 1 + size) % size; // previous node in the ring
  next = (my_rank + 1) % size; // next node in the ring

  // Initialize the value to be transmitted
  value = 1;

  // The nodes, starting with node 0, transmit the value to each other,
  // each time multiplying it by 2.
  // At the end of the transmission, node 0 receives the value 2^(size-1)
  //
  // Instruction: before each send and after each receive, each node displays
  //   - its rank
  //   - the type communication (send, recv)
  //   - the value
  if (my_rank == 0) {
    printf("Node %d sending value %d to node %d\n", my_rank, value, next);
    MPI_Send(&value, 1, MPI_INT, next, 0, MPI_COMM_WORLD);
    MPI_Recv(&value, 1, MPI_INT, previous, 0, MPI_COMM_WORLD, &status);
    printf("Node %d received value %d from node %d\n", my_rank, value, previous);
  } else {
    MPI_Recv(&value, 1, MPI_INT, previous, 0, MPI_COMM_WORLD, &status);
    printf("Node %d receiving value %d from node %d\n", my_rank, value, previous);

    value *= 2;

    printf("Node %d sending value %d to node %d\n", my_rank, value, next);
    MPI_Send(&value, 1, MPI_INT, next, 0, MPI_COMM_WORLD);
  }

  printf("The End\n");

  MPI_Finalize();

  return EXIT_SUCCESS;

}
