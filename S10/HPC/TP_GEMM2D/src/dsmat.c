#include <mpi.h>
#include <stdlib.h>
#include <stdio.h>
#include <cblas.h>

#include "simgrid/actor.h"
#include <simgrid/exec.h>

#include "utils.h"
#include "dsmat.h"

/* Tracing purposes */
static char* COMPUTE = "Computing";
static char* IDLE = "Idling";

void init_trace() {
//  TRACE_host_state_declare(COMPUTE);
//  TRACE_host_state_declare(IDLE);
}

int dsmat_fill(Matrix* a, int m, int n, int b, int p, int q, char* name) {
  int me, node;
  MPI_Comm_rank(MPI_COMM_WORLD, &me);
  int mb = m/b, nb = n/b;
  int ii, jj;
  int row, col;
  a->mb = mb;
  a->nb = nb;
  a->b = b;
  //printf("%d] %s : m x n (b) = %d x %d (%d)\n", me, name, mb, nb, b);
  a->blocks = calloc(mb,sizeof(Block*));
  for (ii = 0; ii < mb;ii++) {
    a->blocks[ii] = calloc(nb,sizeof(Block));
    for (jj = 0; jj < nb;jj++) {
      node = get_node(p,q,ii,jj);
      node_coordinates_2i(p,q,node,&row,&col);
      a->blocks[ii][jj].owner = node;
      a->blocks[ii][jj].row = row;
      a->blocks[ii][jj].col = col;
      a->blocks[ii][jj].request = MPI_REQUEST_NULL;
      if (me == a->blocks[ii][jj].owner) {
	//printf("%d]allocating x_%d,%d\n",me,ii,jj);
	a->blocks[ii][jj].c = calloc(b*b,sizeof(float));
	rand_mat(b,b,a->blocks[ii][jj].c,10);
      } else {
	a->blocks[ii][jj].c = NULL;
      }
    }
  }
  return 0;
}

int dsmat_fill_v(Matrix* a, int m, int n, int b, int p, int q, char* name, float value) {
  int me, node;
  MPI_Comm_rank(MPI_COMM_WORLD, &me);
  int mb = m/b, nb = n/b;
  int ii, jj;
  int row, col;
  a->mb = mb;
  a->nb = nb;
  a->b = b;
  a->blocks = calloc(mb,sizeof(Block*));
  for (ii = 0; ii < mb;ii++) {
    a->blocks[ii] = calloc(nb,sizeof(Block));
    for (jj = 0; jj < nb;jj++) {
      node = get_node(p,q,ii,jj);
      node_coordinates_2i(p,q,node,&row,&col);
      a->blocks[ii][jj].owner = node;
      a->blocks[ii][jj].row = row;
      a->blocks[ii][jj].col = col;
      a->blocks[ii][jj].request = MPI_REQUEST_NULL;
      if (me == a->blocks[ii][jj].owner) {
	//printf("%d]allocating x_%d,%d to fill with %f\n",me,ii,jj, value);
	a->blocks[ii][jj].c = calloc(b*b,sizeof(float));
	val_mat(b,b,a->blocks[ii][jj].c,value);
      } else {
	a->blocks[ii][jj].c = NULL;
      }
    }
  }
  return 0;
}

int dsmat_fill_s(Matrix* a, int m, int n, int b, int p, int q, char* name) {
  int me, node;
  MPI_Comm_rank(MPI_COMM_WORLD, &me);
  int mb = m/b, nb = n/b;
  int ii, jj;
  int row, col;
  a->mb = mb;
  a->nb = nb;
  a->b = b;
  a->blocks = calloc(mb,sizeof(Block*));
  for (ii = 0; ii < mb;ii++) {
    a->blocks[ii] = calloc(nb,sizeof(Block));
    for (jj = 0; jj < nb;jj++) {
      node = get_node(p,q,ii,jj);
      node_coordinates_2i(p,q,node,&row,&col);
      a->blocks[ii][jj].owner = node;
      a->blocks[ii][jj].row = row;
      a->blocks[ii][jj].col = col;
      a->blocks[ii][jj].request = MPI_REQUEST_NULL;
      if (me == a->blocks[ii][jj].owner) {
	//printf("%d] s_allocating %s_%d,%d to fill with %f\n",me,name,ii,jj,(float)nb*(ii+1)+(jj+1));
	a->blocks[ii][jj].c = calloc(b*b,sizeof(float));
	val_mat(b,b,a->blocks[ii][jj].c,(float) nb*(ii+1)+(jj+1));
      } else {
	a->blocks[ii][jj].c = NULL;
      }
    }
  }
  return 0;
}

int dsmat_destroy(Matrix* a, char* name) {
  int me;
  MPI_Comm_rank(MPI_COMM_WORLD, &me);
  int mb = a->mb, nb = a->nb;
  //printf("[%d] destroying matrix %s (mb=%d,nb=%d,b=%d)\n",me, name, mb, nb, a->b);
  int ii, jj;
  Block * a_ij;
  for (ii = 0; ii < mb ; ii++) {
    for (jj = 0; jj < nb ; jj++) {
      a_ij = & a->blocks[ii][jj];
      //if (a_ij->c != NULL) { // && a_ij.owner == me) {
      if (a_ij->c != NULL && a_ij->owner == me) {
	free(a_ij->c);
      }		
    }
    free(a->blocks[ii]);
  }
  free(a->blocks);
  return 0;
}

int dsmat_scal_check(Matrix* A, float alpha) {
  int i,j;
  int me;
  if (alpha == 0.0) return 0;
  MPI_Comm_rank(MPI_COMM_WORLD, &me);
  Block* Aij;
  for(i = 0; i < A->mb; i++) {
    for(j = 0; j < A->nb; j++) {
      Aij = & A->blocks[i][j];
      if (Aij->owner == me) {
	double computation_amount = 2.0*A->b*A->b*A->b;
	cblas_sgemm(CblasRowMajor, CblasNoTrans, CblasNoTrans, A->b, A->b, A->b,
	    0.0, Aij->c, A->b, Aij->c, A->b,
	    alpha, Aij->c, A->b);
      }	
    }
  }
  return 0;
}

int dsmat_scal(Matrix* A, float alpha) {
  int i,j;
  int me;
  if (alpha == 0.0) return 0;
  MPI_Comm_rank(MPI_COMM_WORLD, &me);
  Block* Aij;
  SMPI_SAMPLE_LOCAL(i = 0, i < A->mb, i++, 10, 0.005) {
    SMPI_SAMPLE_LOCAL(j = 0, j < A->nb, j++, 10, 0.005) {
      Aij = & A->blocks[i][j];
      if (Aij->owner == me) {
	double computation_amount = 2.0*A->b*A->b*A->b;
	cblas_sgemm(CblasRowMajor, CblasNoTrans, CblasNoTrans, A->b, A->b, A->b,
	    0.0, Aij->c, A->b, Aij->c, A->b,
	    alpha, Aij->c, A->b);
      }	
    }
  }
  return 0;
}

// FIXME : remove alpha/beta
int local_outer_product_check(float alpha, Matrix* A, Matrix* B, Matrix* C, int l, int p, int q) {
  int i, j, err;
  for(i = 0; i < C->mb; i++) {
    for(j = 0; j < C->nb; j++) {
      err = compute_local_op(alpha, A, B, C, i, j, l);
      if (err != 0) return 1;
    }
  }
  /* free useless memory */
  free_local_op(A, B, l, p, q);
  return 0;
}

int local_outer_product(float alpha, Matrix* A, Matrix* B, Matrix* C, int l, int p, int q) {
  int i, j, err;
  SMPI_SAMPLE_LOCAL(i = 0, i < C->mb, i++, 10, 0.005) {
    SMPI_SAMPLE_LOCAL(j = 0, j < C->nb, j++, 10, 0.005) {
      err = compute_local_op(alpha, A, B, C, i, j, l);
      if (err != 0) return 1;
    }
  }
  /* free useless memory */
  free_local_op(A, B, l, p, q);
  return 0;
}

int compute_local_op(float alpha, Matrix* A, Matrix* B, Matrix* C, int i, int j, int l) {
  int me;
  int b;
  Block *Ail, *Blj, *Cij;
  MPI_Comm_rank(MPI_COMM_WORLD, &me);
  Cij = & C->blocks[i][j];
  b = C->b;
  if (Cij->owner == me) {
    Ail = & A->blocks[i][l];
    if (Ail->c == NULL) { return 1; }
    Blj = & B->blocks[l][j];
    if (Blj->c == NULL) { return 2; }
//    TRACE_host_set_state(COMPUTE);
    cblas_sgemm(CblasRowMajor, CblasNoTrans, CblasNoTrans, b,b,b,
	alpha, Ail->c, b, Blj->c, b,
	1.0, Cij->c, b); 
//    TRACE_host_set_state(IDLE);
  }
  return 0;
}

int free_local_op(Matrix* A, Matrix* B, int l, int p, int q) {
  int i,j;
  int me, me_coord[2];
  MPI_Comm_rank(MPI_COMM_WORLD, &me);
  node_coordinates(p,q,me,me_coord);
  Block *Ail, *Blj;
  for (i = 0; i < A->mb; i++) {
    Ail = & A->blocks[i][l];
    if (Ail->owner != me && Ail->c != NULL) {
      free(Ail->c);
      Ail->c = NULL;
    }
  }
  for (j = 0; j < B->nb; j++) {
    Blj = & B->blocks[l][j];
    if (Blj->owner != me && Blj->c != NULL) {
      free(Blj->c);
      Blj->c = NULL;
    }
  }
  return 0;
}

int block_copy(float * a, float * b, int m, int n) {
  int i, j;
  for (i = 0; i < m ; i++) {
    for (j = 0; j < n ; j++) {
      a[n*i+j] = b[n*i+j];		
    }	
  }	
  return 0;
}

int block_print(float * a, int m, int n, char* name) {
  int i, j;
  printf("block %s\n", name);
  for (i = 0; i < m ; i++) {
    for (j = 0; j < n ; j++) {
      printf("%9.2f\t", a[n*i+j]);
    }	
    printf("\n");
  }	
  printf("\n");
  return 0;
}

// A <- B
int dsmat_copy(Matrix * A, Matrix * B) {
  int i, j;
  int me;
  int mb, nb, b;
  Block *Aij, *Bij;

  MPI_Comm_rank(MPI_COMM_WORLD, &me);

  A->mb = B->mb;
  A->nb = B->nb;
  A->b = B->b;

  mb = A->mb;
  nb = A->nb;
  b = A->b;

  A->blocks = calloc(mb, sizeof(Block*));
  for (i = 0; i<mb;i++){
    A->blocks[i] = calloc(nb, sizeof(Block));
    for (j = 0; j<nb;j++){
      Aij = & A->blocks[i][j];
      Bij = & B->blocks[i][j];
      Aij->owner = Bij->owner;
      Aij->row = Bij->row;
      Aij->col = Bij->col;
      Aij->request = MPI_REQUEST_NULL;
      if (Bij->owner == me) {
        Aij->c = calloc(b*b,sizeof(float));
	block_copy(Aij->c, Bij->c, b, b);
      }
    }
  }
  return 0;
}

int dsmat_copy_to(Matrix * A, Matrix * B, int rcv, char* copy, char* copied) {
  int i, j, l;
  int me,tag;
  int mb, nb, b;
  Block *Aij, *Bij;
  float* localA;
  MPI_Status status;

  MPI_Comm_rank(MPI_COMM_WORLD, &me);
  A->nb = 1;
  A->mb = 1;
  A->b = -1;

  mb = B->mb;
  nb = B->nb;
  b = B->b;

  tag = 0;
  A->blocks = malloc(sizeof(Block*));
  A->blocks[0] = malloc(sizeof(Block));
  Aij = & A->blocks[0][0];
  Aij->owner = rcv;
  Aij->row = -1;
  Aij->col = -1; // not on a grid ...
  Aij->request = MPI_REQUEST_NULL;
  if (me == rcv) {
    Aij->c = malloc(mb*b*nb*b *sizeof(float));
  }
  for (i = 0; i<mb;i++){
    for (j = 0; j<nb;j++){
      Bij = & B->blocks[i][j];
      if (Bij->owner == me) {
	if (rcv != me) {
	  MPI_Send(Bij->c, b*b, MPI_FLOAT, 
	      rcv, tag,
	      MPI_COMM_WORLD); 
	} else {
	  for (l = 0; l<b; l++) {
	    block_copy(&Aij->c[nb*i*b*b+j*b+l*nb*b], Bij->c, 1, b);
	  }
	}
      } else if (me == rcv) {
        localA = malloc(b*b*sizeof(float));
	MPI_Recv(localA, b*b, MPI_FLOAT, 
	    Bij->owner, tag,
	    MPI_COMM_WORLD,&status); 
	for (l = 0; l<b; l++) {
	  block_copy(&Aij->c[nb*i*b*b+j*b+l*nb*b], localA, 1, b);
	}
        free(localA);
      }
    }
  }
  return 0;
}
