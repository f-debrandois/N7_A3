clear all;
% Setup maillage
N = 128;
h = 1/N;
% Evaluate the solution and rhs at mesh points
xi=h:h:1-h; xi=xi';
rhsf= -2 + 12*xi - 12*xi.^2;
usol = xi.^2.*(1-xi).^2; 

% Jacobi weighting parameter
omega = 2/3;
% Setup of the fine grid matrix and the right-hand side
Ah = getMatrixA(N);
% Initial vector
v(1:N-1,1) = 0;

% We do 10 iterations.
maxit = 10;

res = zeros(maxit+1,1);
errorL2 = zeros(maxit+1,1);

% Initial residual error
res(1) = norm(rhsf - Ah*v);
errorL2(1) = compute_L2_error(N,usol,v);

nu1=1;
nu2=1;

for i=1:10
    v = V_cycle(Ah,rhsf,v,omega,nu1,nu2,N);
    res(i+1) = norm(rhsf - Ah*v);
    errorL2(i+1) = compute_L2_error(N,usol,v);
end