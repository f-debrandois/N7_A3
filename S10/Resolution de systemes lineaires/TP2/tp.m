close all;
clear all;

load mat0;

n = size(A,1);

subplot(2,3,1);
spy(A);
title('Original matrix A');
 
[count, h, parent, post, R] = symbfact(A);
ALU = R+R';
subplot(2,3,2)
spy(ALU);
title('Factors of A')
fillin = nnz(ALU)-nnz(A)

% visualisation du fill
C = spones(A);
CLU = spones(ALU);
FILL = CLU-C;
subplot(2,3,3)
spy(FILL)
title('Fill on original A')

% Permutation (à modifier)
P = symamd(A);

B = A(P,P);
subplot(2,3,4)
spy(B);
title('Permuted matrix')

[count, h, parent, post, R] = symbfact(B);
BLU = R+R';
subplot(2,3,5)
spy(BLU);
fillin = nnz(BLU)-nnz(A)
title('Factors of permuted A');

B = spones(B);
BLU = spones(BLU);
FILL = BLU-B;
subplot(2,3,6)
spy(FILL);
title('Fill on permuted A');


x_ref = A \ b;

L = chol(A, "lower");

y = L \ b;
x1 = L' \ y;

cout1 = 4*nnz(L)

be1 = norm(A*x1-b)/norm(b)
fe1 = norm(x1-x_ref)/norm(x_ref)

P = symrcm(A);
B = A(P,P);

L = chol(B, "lower");

y = L \ b(P);
z = L' \ y;
x2 = zeros(n,1);
x2(P) = z;

cout2 = 4*nnz(L)

be2 = norm(A*x2-b)/norm(b)
fe2 = norm(x2-x_ref)/norm(x_ref)