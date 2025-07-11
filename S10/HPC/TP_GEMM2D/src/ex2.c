#include <stdio.h>
#include <stdlib.h>
#include <mpi.h>
#include <cblas.h>
#include "utils.h"
#include "dsmat.h"
#include "gemms.h"

void bcast_A(int p, int q, Matrix *A, int i, int l, MPI_Comm row_comm) {
    int me, my_row, my_col;

    MPI_Comm_rank(MPI_COMM_WORLD, &me);
    node_coordinates_2i(p,q,me,&my_row,&my_col);

    Block *Ail;
    int b = A->b;
    Ail =  & A->blocks[i][l];

    /* TODO : transmit A[i,l] using MPI_Bcast */
    if (q > 1 && 1 /* Ail is stored on my row */) {
      if (Ail->owner != me) {
        Ail->c = calloc(b*b, sizeof(float));
      }
      // MPI_Bcast
      int root = Ail->owner % q; // root index in the row communicator
      MPI_Bcast(Ail->c, b * b, MPI_FLOAT, root, row_comm);
    }
    /* end TODO */
}


void bcast_B(int p, int q, Matrix *B, int l, int j, MPI_Comm col_comm) {
    int me, my_row, my_col;

    MPI_Comm_rank(MPI_COMM_WORLD, &me);
    node_coordinates_2i(p,q,me,&my_row,&my_col);

    Block *Blj;
    int b = B->b;
    Blj =  & B->blocks[l][j];

    /* TODO : transmit B[l,j] using MPI_Bcast */
    if (p > 1 && 1 /* Blj is stored on my column */) {
      if (Blj->owner != me) {
        Blj->c = calloc(b*b, sizeof(float));
      } 
      // MPI_Bcast
      int root = Blj->owner / q;  // root index in the column communicator
      MPI_Bcast(Blj->c, b * b, MPI_FLOAT, root, col_comm);
    }
    /* end TODO */
}
