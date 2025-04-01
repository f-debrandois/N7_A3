close all;
clear all;

load mat1;
%load pde225_5e-1;
%load hydcar20.mat;

n = size(A,1);
fprintf('dimension de A : %4d \n' , n);

b = [1:n]';

x0 = zeros(n, 1);

eps = 1e-3;

kmax = n;

x_exact = A \ b;

fprintf('FOM\n');
[x, flag, relres, iter, resvec] = krylov(A, b, x0, eps, kmax, 0);
fprintf('Nb iterations : %4d \n' , iter);
relative_error = norm(x - x_exact) / norm(x_exact);
fprintf('L''erreur relative est : %.2e\n', relative_error);
semilogy(resvec, 'c');
legend('FOM');
if(flag ~= 0)
  fprintf('pas de convergence\n');
end

pause

fprintf('GMRES\n');
[x, flag, relres, iter, resvec] = krylov(A, b, x0, eps, kmax, 1);
fprintf('Nb iterations : %4d \n' , iter);
relative_error = norm(x - x_exact) / norm(x_exact);
fprintf('L''erreur relative est : %.2e\n', relative_error);
hold on
semilogy(resvec, 'r');
legend('FOM', 'GMRES');
if(flag ~= 0)
  fprintf('pas de convergence\n');
end

pause

%pre conditionement
% M1 = diag(diag(A));
% M2 = speye(n);


fprintf('GMRES matlab\n');
[x, flag, relres, iter, resvec] = gmres(A, b, [], eps, kmax, [], [], x0);
% [x, flag, relres, iter, resvec] = gmres(A, b, [], eps, kmax, M1, M2, x0);
fprintf('Nb iterations : %4d \n' , iter);
relative_error = norm(x - x_exact) / norm(x_exact);
fprintf('L''erreur relative est : %.2e\n', relative_error);
semilogy(resvec, '+r');
legend('FOM', 'GMRES', 'GMRES matlab');
if(flag ~= 0)
  fprintf('pas de convergence\n');
end