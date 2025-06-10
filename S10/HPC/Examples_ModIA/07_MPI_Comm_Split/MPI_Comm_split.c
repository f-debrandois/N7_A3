/**
 * @author RookieHPC
 * @brief Original source code at https://rookiehpc.org/mpi/docs/mpi_comm_split/index.html
 **/

#include <stdio.h>
#include <stdlib.h>
#include <mpi.h>

int main(int argc, char* argv[])
{
    MPI_Init(&argc, &argv);

    int comm_size;
    MPI_Comm_size(MPI_COMM_WORLD, &comm_size);

    // Get my rank in the global communicator
    int my_rank;
    MPI_Comm_rank(MPI_COMM_WORLD, &my_rank);

    // Determine the colour and key based on whether my rank is even.
    char subcommunicator;
    int colour;
    int key;
    //if(my_rank % 2 == 0)
    if(my_rank < 4)
    {
        subcommunicator = 'A';
        colour = 0;
        key = my_rank;
    }
    else
    {
        subcommunicator = 'B';
        colour = 1;
        // same order
        key = my_rank;
        // opposite order
        //key = size - my_rank;
    }

    // Split de global communicator
    MPI_Comm new_comm;
    MPI_Comm_split(MPI_COMM_WORLD, colour, key, &new_comm);

    // Get my rank in the new communicator
    int my_new_comm_rank;
    MPI_Comm_rank(new_comm, &my_new_comm_rank);

    // Print my new rank and new communicator
    printf("[MPI process %d] I am now MPI process %d in subcommunicator %c.\n", my_rank, my_new_comm_rank, subcommunicator);

    MPI_Finalize();

    return EXIT_SUCCESS;
}
