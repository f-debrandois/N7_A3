% Script Full multigrid FMG(nu1, nu2)
clear all;
N = 2^2; %coarsest grid with 4 elements
h = 1/N;
% Evaluate the solution and rhs at mesh points
xi=h:h:1-h; xi=xi';
rhsf= -2 + 12*xi - 12*xi.^2;
usol = xi.^2.*(1-xi).^2; 

% Setup Jacobi
omega = 2/3;
nu1 = 1; % Presmoothing
nu2 = 1; % Postsmoothing
% Setup the matrix and the right-hand side at the coarsest level
Ah = getMatrixA(N);
% Get the intial solution on the coarsest grid
sol_ref = Ah \ rhsf;


target = 4;

errorL2 = zeros(target+1,1);
errorL2(1) = compute_L2_error(N,usol,sol_ref);
v = sol_ref;


for i=1:target

    NN = 2^i*N;
    h = 1/NN;
    xi=h:h:1-h; xi=xi';

    rhsf= -2 + 12*xi - 12*xi.^2;
    usol = xi.^2.*(1-xi).^2; 

    % Setup interpolation operator, system matrix and rhs for next higher level
    I2hh = interpol(NN);
    Ah = getMatrixA(NN);


    % Interpolate the last solution as initial guess to next higher level
    v = I2hh * v;

    % Run a L+1 level V-cycle with initial guess v
    v = V_cycle_L(Ah,rhsf,v,omega,nu1,nu2,NN,i);
  %  v = V_cycle_L(Ah,rhsf',v,omega,nu1,nu2,NN,i);
    errorL2(i+1) = compute_L2_error(NN,usol,v);
end 

errorL2(1:target)./errorL2(2:target+1)
