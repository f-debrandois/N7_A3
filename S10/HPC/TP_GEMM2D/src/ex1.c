#include <stdio.h>
#include <stdlib.h>
#include <mpi.h>
#include <cblas.h>
#include "utils.h"
#include "dsmat.h"
#include "gemms.h"

void p2p_transmit_A(int p, int q, Matrix *A, int i, int l) {
    int j;
    int me, my_row, my_col;
    MPI_Status status;
    MPI_Comm_rank(MPI_COMM_WORLD, &me);
    node_coordinates_2i(p,q,me,&my_row,&my_col);

    Block *Ail;
    int node, tag, b;
    Ail = & A->blocks[i][l];
    b = A->b;
    tag = 0;

    /* TODO : transmit A[i,l] using MPI_Ssend & MPI_Recv */
    if (Ail->owner == me /* I own A[i,l]*/) {
        /* MPI_Ssend A[i,l] to my row */
        for (j = 0; j < q; j++) {
          node = get_node(p, q, my_row, j);
          if (node != me) { // Do not send to myself
            MPI_Ssend(Ail->c, b*b, MPI_FLOAT, node, tag, MPI_COMM_WORLD);
          }
        }
    } else if (Ail->row == my_row /* A[i,l] is stored on my row */) {
        Ail->c = malloc(b*b*sizeof(float));
        /* MPI_Recv A[i,l] */
        MPI_Recv(Ail->c, b*b, MPI_FLOAT, Ail->owner, tag, MPI_COMM_WORLD, &status);
    }
    /* end TODO */
}


void p2p_transmit_B(int p, int q, Matrix *B, int l, int j) {
    int i;
    int me, my_row, my_col;
    MPI_Status status;
    MPI_Comm_rank(MPI_COMM_WORLD, &me);
    node_coordinates_2i(p,q,me,&my_row,&my_col);

    int node, tag, b;
    Block *Blj;
    Blj = & B->blocks[l][j];
    b = B->b;
    tag = 1;

    /* TODO : transmit B[l,j] using MPI_Ssend & MPI_Recv */
    if (Blj->owner == me /* I owned B[l,j]*/) {
        /* MPI_Ssend B[l,j] to my column */
        for (i = 0; i < p; i++) {
          node = get_node(p, q, i, my_col);
          if (node != me) { // Do not send to myself
            MPI_Ssend(Blj->c, b*b, MPI_FLOAT, node, tag, MPI_COMM_WORLD);
          }
        }
    } else if (Blj->col == my_col /* B[l,j] is stored on my column */) {
        Blj->c = malloc(b*b*sizeof(float));
        /* MPI_Recv B[l,j] */
        MPI_Recv(Blj->c, b*b, MPI_FLOAT, Blj->owner, tag, MPI_COMM_WORLD, &status);
    }
    /* end TODO */
}
