function A = getMatrixA(N)

h = 1/N;
A = 1/h^2*sparse((diag(2*ones(N-1,1)) - diag(ones(N-2,1), -1) - diag(ones(N-2,1), 1)));
