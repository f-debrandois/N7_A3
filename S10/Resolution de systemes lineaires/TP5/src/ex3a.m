clc; clear; close all; 

n_subdomains  = 20; 
local_dofs   = 5; 
overlap = 0; 

problem = Problem(n_subdomains, local_dofs,  overlap); 


[~, iters_TAS_mult, res_AS] = problem.solve_richardson("AS", -1); 

[~, iters_TL_add, res_TL_add] = problem.solve_richardson("TG", -1); 



figure;
semilogy(res_AS, 'Linewidth', 3);     
hold on;
semilogy(res_TL_add, 'Linewidth', 3);      
grid on
xlabel('Iterations');
ylabel('||r||');
title('Schwarz preconditioners')
legend('AS','TG');


