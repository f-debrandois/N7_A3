function err = compute_L2_error(N,u,uh)
h = 1/N;

em = u-uh;

err = sqrt(h*em'*em);
end