close all;
clear all;

%% Multigrille 1D : -u'' = f

N = 64;
h = 1/N;
A = getMatrixA(N);
omega = 2/3;
j = 1:N-1;

% f = 2
rhsf = 2 * ones(N-1, 1);

% Solution directe
sol_ref = A\rhsf;

% kieme vecteur propre de A
k = 6;
[um, D] = eig(full(A));
um = um(:,k);

m = 10;
ump1 = weighted_jacobi(A, um, rhsf, omega, m);

x=h:h:1-h;
figure;
plot(x,um,x, ump1);
legend('um','ump1');
title('Damping effect of weighted Jacobi method')


%% Operateurs de transfert

%clear all;

% Setup maillage
N = 64;
h = 1/N;

% Setup Jacobi
omega = 2/3;

% Setup of the fine and coarse grid matrix
% and the right-hand side
Ah = getMatrixA(N);
A2h = getMatrixA(N/2);
rhsf = 2*ones(N-1,1);

% Compute direct solution of linear system
sol_ref = Ah\rhsf;

% Setup interpolation matrix
I2hh = interpol(N);
Ih2h = I2hh' / 2;

% Initial vector
v(1:N-1,1) = 0;

% Vector to store the error at each iteration.
% We do 10 iterations.
err(1:10) = 0;

% Multigrid iterations with 2 pre-smoothing steps
for i=1:10
    v = weighted_jacobi(Ah,v,rhsf,omega,2);
    % residual on fine grid
    res_h = rhsf - Ah*v;

    % Restriction of residual to coarser grid
    res_2h = Ih2h * res_h;

    % Solve the coarse grid error equation
    e_2h = A2h\res_2h;

    % Interpolate the coarse grid error to the fine grid
    e_h = I2hh * e_2h;

    % Update the approximate fine grid solution
    v = v + e_h;

    % Compute the error with respect to the direct
    % solution of the linear system
    err(i) = norm(sol_ref-v);
end

% Plot the error
figure;
plot(1:10,err);
title('Error of the multigrid method');
xlabel('Iteration');
ylabel('Error');


%% Adaptation du critere d’arret

%clear all;

% Initial vector
v(1:N-1,1) = 0;

% Vector to store the error at each iteration.
err_vec = [];

epsilon = 1e-6;
max_iter = 100;

i = 1;
while i <= max_iter
    v = weighted_jacobi(Ah,v,rhsf,omega,2);
    % residual on fine grid
    res_h = rhsf - Ah*v;

    % Restriction of residual to coarser grid
    res_2h = Ih2h * res_h;

    % Solve the coarse grid error equation
    e_2h = A2h\res_2h;

    % Interpolate the coarse grid error to the fine grid
    e_h = I2hh * e_2h;

    % Update the approximate fine grid solution
    v = v + e_h;

    % Compute the error
    err = norm(res_h) / norm(rhsf);
    err_vec = [err_vec err];
    if err < epsilon
        break;
    end
    i = i + 1;
end

% Plot the error
figure;
plot(1:i,err_vec);
title('Error of the multigrid method');
xlabel('Iteration');
ylabel('Error');