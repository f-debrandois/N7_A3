clc; clear; close all; 

overlap = 0; 
n_subdomains  = [60, 30, 20, 10, 5];
local_dofs    = [5, 10, 15, 30, 60];

figure;
for i =1:size(n_subdomains, 2)
    problem = Problem(n_subdomains(i), local_dofs(i),  overlap);
    [x_AS, iters_AS, res_AS] = problem.solve_richardson("TL_AS_mult_coarse_first", -1);
    hg = semilogy(res_AS, 'Linewidth', 3);
    color = hg.Color;
    hold on;
    
    [x_AS, iters_AS, res_AS] = problem.solve_richardson("AS", -1);
    semilogy(res_AS, ':', 'Color',  color, 'Linewidth', 3);
    hold on;    
end



grid on

xlabel('Iterations');
ylabel('||r||');
title('Schwarz preconditioners: Single vs. Two-level')
legend('AS(60)', 'TL-AS(60)', 'AS(30)', 'TL-AS(30)',  'AS(20)', 'TL-AS(20)', 'AS(10)','TL-AS(10)', 'AS(5)', 'TL-AS(5)');

