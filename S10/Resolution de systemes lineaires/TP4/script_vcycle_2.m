% Script to run the V-cycle
%...
%...
% Evaluate the solution at each mesh point
xi=h:h:1-h; xi = xi'; % row vector to column vector
usol = ?
rhsf= -2 + 12*xi - 12*xi.^2;
% ...
% ...
maxit = 10
% Initialize errors variable and compute initial errors
res = zeros(maxit+1,1);
errorL2 = zeros(maxit+1,1);
% Initial residual and L2 error
res(1) = norm(rhsf - Ah*v);
errorL2(1) = ?
nu1=1;
nu2=1;
for i=1:10
v = V_cycle(Ah,rhsf,v,omega,nu1,nu2,N);
% Compute errors after each iteration
errorL2(i+1) = ?
res(i+1) = norm(rhsf - Ah*v);
end