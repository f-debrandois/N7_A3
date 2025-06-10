#include <stdio.h>
#include <stdlib.h>
#include <mpi.h>

// Perform x = A*y with x[m], y[n] and A[m,n]
void multAv(double x[], double *A, double y[], int m, int n);

// Initialize x[n] with 0.0
void init0(double x[], int n);

int main(int argc, char *argv[])
{

  int n = -1;
  int my_rank, size;

  MPI_Init(&argc, &argv);

  // Get my rank
  MPI_Comm_rank(MPI_COMM_WORLD, &my_rank);

  // Get number of processes and check that 4 processes are used
  MPI_Comm_size(MPI_COMM_WORLD, &size);
  if (size != 4)
  {
    printf("This application is meant to be run with 4 MPI processes.\n");
    MPI_Abort(MPI_COMM_WORLD, EXIT_FAILURE);
  }

  // Declaration of A, the global square matrix 
  double *A;

  // Only process 0 knows the square matrix A and its dimension n
  if (my_rank == 0)
  {
    n = 12;
    A = (double *) malloc(n * n * sizeof(double));

    for (int i = 0; i < n; i++)
    {
      for (int j = 0; j < n; j++)
      {
        A[i * n + j] = 1.0;
      }
    }
  }

  // Broadcast the dimension of the square matrix
  // ... TODO

  //  b, the size of a bloc of rows
  int b = n / size;

  // Declaration and allocation of A_loc, the local matrix
  // ... TODO

  // Communication of blocks of rows of A among the process
  // ... TODO

  // Declaration and allocation of vector v (needed by all process)
  double *v = (double *) malloc(n * sizeof(double));

  // Only process 0 knows the vector v
  if (my_rank == 0)
  {

    for (int i = 0; i < n; i++)
    {
      v[i] = i;
      // printf("Process [%d], x[%d] = %f\n", my_rank, i, v[i]);
    }
  }

  // Communication of v
  // ... TODO

  // Vector x_loc = A_loc * v
  double *x_loc; // ... TODO
  init0(x_loc, b);

  // Perform the multiplication x_loc = A_loc * v
  // ... TODO

  // Each node displays x (with A, full of ones, all the components of x should be the same)
  for (int i = 0; i < b; i++)
  {
    // comment to avoid segfault when original code is run
    //printf("Process [%d], x_loc[%d] = %f\n", my_rank, i, x_loc[i]);
  }

  // Process 2 collects the global x
  double *x;
  if (my_rank == 2)
  {
    // Allocate x
    // ... TODO
  }

  // Collect x
  // ... TODO

  if (my_rank == 2)
  {
    for (int i = 0; i < n; i++)
    {
      // comment to avoid segfault when original code is run
      //printf("Process [%d], x[%d] = %f\n", my_rank, i, x[i]);
    }
  }

  // Sequential computation on 0
  if(my_rank == 0){
    x = (double *) malloc(n * sizeof(double));
    multAv(x, A, v, n, n);
    for (int i = 0; i < n; i++)
    {
      printf("Process [%d], x_seq[%d] = %f\n", my_rank, i, x[i]);
    }
  }

  MPI_Finalize();

  return EXIT_SUCCESS;
}

void multAv(double x[], double *A, double y[], int m, int n){

  for(int i = 0; i < m; i++){
    x[i] = 0.0;
    for(int j = 0; j < n; j++){
      x[i] += A[i*n + j] * y[j];
    }
  }
  return;
}

void init0(double x[], int n){

  for(int i = 0; i < n; i++){
    x[i] = 0.0;
  }
  return;
}
