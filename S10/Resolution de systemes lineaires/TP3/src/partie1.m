clear all;

N = 64;
h = 1/N;
A = getMatrixA(N);
rhsf(1:N-1,1) = 0;

sol_ref = A \ rhsf;

omega = 2/3;

j = 1:N-1;
k = 48;

% kieme vecteur propre
um = sin(j/N*k*pi);

% Apply m iterations of weighted Jacobi
m = 10;
ump1 = weighted_jacobi(A, um', rhsf, omega, m);

x=h:h:1-h;
plot(x, um, x, ump1);
legend('um','ump1');
title('Damping effect of weighted Jacobi method')
