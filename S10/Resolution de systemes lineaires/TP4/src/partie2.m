format long e
clear all;
% Setup maillage
N = 8;
h = 1/N;
% Setup Jacobi
omega = 2/3;
% Setup of the fine and coarse grid matrix
% and the right-hand side
Ah = getMatrixA(N);
A2h = getMatrixA(N/2);
rhsf = 2*ones(N-1,1);
% Compute direct solution of linear system
sol_ref = Ah \ rhsf;
% Setup interpolation matrix
I2hh = interpol(N);
Ih2h = 0.5*I2hh';

% Initial vector
v(1:N-1,1) = 0;
v0 = v;
% Vector to store the error at each iteration.
% We do 10 iterations.
maxit = 10;

residu = zeros(maxit+1, 1);
% Multigrid iterations with 2 pre-smoothing steps
residu(1) = norm(rhsf - Ah*v, 2)/norm(rhsf - Ah*v0,2);
%epsilon = 10e-10;
%i = 1;
%Solve for a fixed number of cycles
for i=1:10
% We could also stop for a given tolerance:    
% while (residu(i) > epsilon) && (i < maxit)
    v = weighted_jacobi(Ah, v, rhsf, omega, 2);
    % residual on fine grid
    res_h = rhsf - Ah*v;
    % Restriction of residual to coarser grid
    res_2h = Ih2h*res_h;
    % Solve the coarse grid error equation
    e_2h = A2h \ res_2h;
    % Interpolate the coarse grid error to the fine grid
    e_h = I2hh*e_2h;
    % Update the approximate fine grid solution
    v = v + e_h;
    % Compute the residual
    residu(i+1) = norm(rhsf - Ah*v, 2)/norm(rhsf - Ah*v0,2);
    %i = i + 1;
end