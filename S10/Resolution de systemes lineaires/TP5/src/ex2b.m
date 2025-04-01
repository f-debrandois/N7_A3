clc; clear; close all; 

n_subdomains  = 20; 
local_dofs   = 5; 
overlap = 0; 

problem = Problem(n_subdomains, local_dofs,  overlap); 


[~, iters_TL_add, res_TL_add] = problem.solve_richardson("TL_AS_add", -1); 

[~, iters_TL_mult_second, res_TL_mult_second] = problem.solve_richardson("TL_AS_mult_coarse_second", -1); 

figure;
semilogy(res_TL_add, 'Linewidth', 3);     
hold on;
semilogy(res_TL_mult_second, 'Linewidth', 3);    
grid on
xlabel('Iterations');
ylabel('||r||');
title('Two-level schwarz preconditioners')
legend('TL-AS-add', 'TL-AS-mult-first', 'TL-AS-mult-second');



[~, iters_TL_mult_second, res_TL_mult_second] = problem.solve_richardson("TL_AS_mult_coarse_second", -1); 
[~, iters_TL_mult_first, res_TL_mult_first] = problem.solve_richardson("TL_AS_mult_coarse_first", -1); 

figure;
semilogy(res_TL_add, 'Linewidth', 3);     
hold on;
semilogy(res_TL_mult_first, 'Linewidth', 3);    
semilogy(res_TL_mult_second, 'Linewidth', 3);    
grid on
xlabel('Iterations');
ylabel('||r||');
title('Two-level schwarz preconditioners')
legend('TL-AS-add', 'TL-AS-mult-first', 'TL-AS-mult-second');



