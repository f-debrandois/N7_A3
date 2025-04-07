function A = getMatrixA(N)

h = 1/N;
two(1:N-1,1) = 2;
onevec(1:N-2,1) = 1;

A = 1/h^2 * sparse((diag(two,0)-diag(onevec,1)-diag(onevec,-1)));

% Shorter alternative:
%A = 1/h^2*sparse((diag(2*ones(N-1,1)) - diag(ones(N-2,1), -1) - diag(ones(N-2,1), 1)));
