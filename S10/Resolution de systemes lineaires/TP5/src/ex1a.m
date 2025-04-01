clc; clear; close all; 


overlap = 0;
n_subdomains  = [60, 30, 20, 10, 5];
local_dofs    = [5, 10, 15, 30, 60];


figure;



for i =1:size(n_subdomains, 2)
    problem = Problem(n_subdomains(i), local_dofs(i),  overlap);
    [x_AS, iters_AS, res_AS] = problem.solve_richardson("AS", -1);
    semilogy(res_AS, 'Linewidth', 3);
    hold on;
end



grid on

xlabel('Iterations');
ylabel('||r||');
title('Richardson with Schwarz preconditioner wrt. number of subdomains')
legend('AS(60)', 'AS(30)', 'AS(20)', 'AS(10)', 'AS(5)');








problem = Problem(n_subdomains(1), local_dofs(1),  overlap);
[x, iters, res] = problem.solve_pcg();



figure;
semilogy(res, 'Linewidth', 3);
hold on;


for i =1:size(n_subdomains, 2)
    problem = Problem(n_subdomains(i), local_dofs(i),  overlap);
    [x_AS, iters_AS, res_AS] = problem.solve_pcg_precond_AS();
    semilogy(res_AS, 'Linewidth', 3);
    
end



grid on

xlabel('Iterations');
ylabel('||r||');
title('CG with Schwarz preconditioner wrt. number of subdomains')
legend('CG','CG-AS(60)', 'CG-AS(30)', 'CG-AS(20)', 'CG-AS(10)', 'CG-AS(5)');

