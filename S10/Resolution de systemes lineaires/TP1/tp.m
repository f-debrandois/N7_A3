close all;
clear all;

%load mat1;
%load pde225_5e-1;
load hydcar20.mat;

n = size(A,1);
fprintf('dimension de A : %4d \n' , n);

b = [1:n]';

x0 = zeros(n, 1);

eps = 1e-6;

kmax = n;

% FOM
fprintf('FOM\n');
[x, flag, relres, iter, resvec] = krylov(A, b, x0, eps, kmax, 0);
fprintf('Nb iterations : %4d \n' , iter);
semilogy(resvec, 'c');
legend('FOM');
if(flag ~= 0)
  fprintf('pas de convergence\n');
end

pause

% GMRES
fprintf('GMRES\n');
[x, flag, relres, iter, resvec] = krylov(A, b, x0, eps, kmax, 1);
fprintf('Nb iterations : %4d \n' , iter);
hold on
semilogy(resvec, 'r');
legend('FOM', 'GMRES');
if(flag ~= 0)
  fprintf('pas de convergence\n');
end

pause

% GMRES Matlab
fprintf('GMRES Matlab\n');
[x, flag, relres, iter, resvec] = gmres(A, b, [], eps, kmax, [], [], x0);
fprintf('Nb iterations : %4d \n' , iter);
semilogy(resvec, 'g');
legend('FOM', 'GMRES', 'GMRES Matlab');
if(flag ~= 0)
  fprintf('pas de convergence\n');
end
