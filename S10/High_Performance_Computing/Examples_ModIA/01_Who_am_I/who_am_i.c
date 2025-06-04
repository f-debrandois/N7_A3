#include <stdio.h>
#include <mpi.h>

int main( int argc, char *argv[] ) {

  int rank = -1;
  int comm_size = -1;
  int namelen;
  char procname[MPI_MAX_PROCESSOR_NAME];

  // Initialise MPI
  MPI_Init(NULL, NULL);

  // Get my rank
  MPI_Comm_rank(MPI_COMM_WORLD, &rank);

  // Get tne number of processor in the communicator MPI_COMM_WORLD
  MPI_Comm_size(MPI_COMM_WORLD, &comm_size);

  // Get the name of the processor
  MPI_Get_processor_name(procname, &namelen);

  // display the informations
  printf("Hello world from process %d of %d on processor named %s\n", rank, comm_size, procname);
  
  // Tell MPI to shut down.
  MPI_Finalize();
  
  return 0;
}
