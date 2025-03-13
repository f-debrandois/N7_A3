%echo on
clear all;
close all;

figure(1);

A = [1 0 1 0 0 1 0 0;
     0 1 0 0 1 0 0 1;
     1 0 1 0 1 0 0 0;
     0 0 0 1 0 1 1 0;
     0 1 1 0 1 0 0 1;
     1 0 0 1 0 1 1 0;
     0 0 0 1 0 1 1 0;
     0 1 0 0 1 0 0 1];

% 1. Matrice Originale

% affichage de la structure de la matrice originale
subplot(2, 3, 1);
spy(A);
title('Original matrix A');

% factorisation symbolique de la matrice originale
[count, h, parent, post, R] = symbfact(A);
ALU = R+R';

% affichage de la structure des facteurs de la matrice originale
subplot(2, 3, 2)
spy(ALU);
title('Factors of A')
fillin = nnz(ALU)-nnz(A)

% visualisation du fill-in
A_ones = spones(A);
ALU_ones = spones(ALU);
FILL = ALU_ones - A_ones;
subplot(2, 3, 3)
spy(FILL)
title('Fill on A')

% 2. Matrice Permutée

% Minimal degree
P = [1 2 8 5 3 4 6 7];

B = A(P, P);
% affichage de la structure de la matrice permutée
subplot(2, 3, 4)
spy(B);
title('Permuted matrix B');

% factorisation symbolique de la matrice permutée
[count, h, parent, post, R] = symbfact(B);

% affichage de la structure des facteurs de la matrice permutée
BLU = R+R';
subplot(2, 3, 5)
spy(BLU);
title('Factors of B')
fillin = nnz(BLU) - nnz(A)

% visualisation du fill-in
B_ones = spones(B);
BLU_ones = spones(BLU);
FILLB = BLU_ones - B_ones;
subplot(2, 3, 6)
spy(FILLB);
title('Fill on B')


figure(2);

% 3. Cuthill-Mc Kee.

% Cuthill-Mc Kee permutation from 1
P = [1 3 6 4 7 5 2 8];

C = A(P, P);
% affichage de la structure de la matrice permutée
subplot(2, 3, 1)
spy(C);
title('Permuted matrix C');

% factorisation symbolique de la matrice permutée
[count, h, parent, post, R] = symbfact(C);

% affichage de la structure des facteurs de la matrice permutée
CLU = R+R';
subplot(2, 3, 2)
spy(CLU);
title('Factors of C')
fillin = nnz(CLU) - nnz(A)

% visualisation du fill-in
C_ones = spones(C);
CLU_ones = spones(CLU);
FILLC = CLU_ones - C_ones;
subplot(2, 3, 3)
spy(FILLC);
title('Fill on C')


% Cuthill-Mc Kee permutation from 2
P = [2 8 5 3 1 6 4 7];

D = A(P, P);
% affichage de la structure de la matrice permutée
subplot(2, 3, 4)
spy(D);
title('Permuted matrix D');

% factorisation symbolique de la matrice permutée
[count, h, parent, post, R] = symbfact(D);

% affichage de la structure des facteurs de la matrice permutée
DLU = R+R';
subplot(2, 3, 5)
spy(DLU);
title('Factors of D')
fillin = nnz(DLU) - nnz(A)

% visualisation du fill-in
D_ones = spones(D);
DLU_ones = spones(DLU);
FILLD = DLU_ones - D_ones;
subplot(2, 3, 6)
spy(FILLD);
title('Fill on D')
