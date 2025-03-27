clear all;

% Setup maillage
N = 256;
h = 1/N;

% Interior mesh points
xi=h:h:1-h; xi = xi'; % row vector to column vector

% Jacobi weighting parameter
omega = 2/3;

% Setup of the fine grid matrix and the right-hand side
Ah = getMatrixA(N);
rhsf= -2 + 12*xi - 12*xi.^2;

% Initial vector
v(1:N-1,1) = 0;

% We do 10 iterations.
maxit = 10;
res = zeros(maxit+1,1);

% Initial residual
res(1) = norm(rhsf - Ah*v);

nu1=1;
nu2=1;

for i=1:10
    v = V_cycle(Ah,rhsf,v,omega,nu1,nu2,N);
    res(i+1) = norm(rhsf - Ah*v);
end