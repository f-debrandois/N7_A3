% Script Full multigrid FMG(nu1, nu2)
clear all;
N = 2^2; %coarsest grid with 4 elements
h = 1/N;
xi=h:h:1-h; xi=xi';% Mesh points

% Setup Jacobi
omega = 2/3;

nu1 = 2; % Presmoothing
nu2 = 1; % Postsmoothing

% Setup the matrix and the right-hand side at the coarsest level
Ah = getMatrixA(N);
rhsf= -2 *(1-xi).^2 + 8*xi.*(1-xi) - 2*xi.^2;

% Get the intial solution on the coarsest grid
sol_ref = Ah \ rhsf;

% Get solution u and the L2-error of the error
usol = xi.^2.*(1-xi).^2;
err(1) = compute_L2_error(N,usol,sol_ref);
v = sol_ref;

% Move to next finer grid
NN = 2*N; h = 1/NN; % 8 elements
xi=h:h:1-h; xi=xi'; %overwrite mesh

% Get interpolation operators, right-hand side and the stiffness matrix at the next higher level

I2hh = interpol(NN);
Ah = getMatrixA(NN);
rhsf= -2 *(1-xi).^2 + 8*xi.*(1-xi) - 2*xi.^2;

% Interpolate the last solution as initiel guess to next higher level
v = I2hh * v;

% Run a (1+1)-level V-cycle with initial guess v
v = V_cycle_L(Ah,rhsf,v,omega,nu1,nu2,NN,1);

% Get solution u and the L2-error of the error
usol = xi.^2.*(1-xi).^2;
err(2) = compute_L2_error(NN,usol,v);