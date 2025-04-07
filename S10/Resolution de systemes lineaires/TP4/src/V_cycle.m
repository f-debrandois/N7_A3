function v = V_cycle(Ah,rhsf,u0,omega,nu1,nu2,N)

I2hh = interpol(N);
Ih2h = 0.5*I2hh';

v = weighted_jacobi(Ah, u0, rhsf, omega, nu1);
% residual on fine grid    
res_h = rhsf - Ah*v;
% Restriction of residual to coarser grid
res_2h = Ih2h*res_h;
% Coarse grid matrix with Galerkin projection
A2h = Ih2h*Ah*I2hh;
% Solve the coarse grid error equation
e_2h = A2h \ res_2h;
% Interpolate the coarse grid error to the fine grid
e_h = I2hh*e_2h;
% Update the approximate fine grid solution
v = v + e_h;
% nu2 steps of Jacobi postsmoothing
v = weighted_jacobi(Ah, v, rhsf, omega, nu2);

end
