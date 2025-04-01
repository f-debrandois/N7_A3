clc; clear; close all; 

n_subdomains  = 20;
local_dofs   = 10;

overlaps = [0, 1, 3]; 

figure;
for i =1:size(overlaps, 2)
	problem = Problem(n_subdomains, local_dofs,  overlaps(i));
    
    step_size = 1.0; 
    
    [x_AS, iters_AS, res_AS] = problem.solve_richardson("AS", step_size);
    hg = semilogy(res_AS, 'Linewidth', 3);
    color = hg.Color;
    hold on;
    
end



grid on

xlabel('Iterations');
ylabel('||r||');
title('Richardson with Schwarz preconditioner (fixed step-size)')
legend('TL-AS-o0','TL-AS-o1', 'TL-AS-o3');







figure;
for i =1:size(overlaps, 2)
	problem = Problem(n_subdomains, local_dofs,  overlaps(i));
    
    [x_AS, iters_AS, res_AS] = problem.solve_richardson("AS", -1);
    hg = semilogy(res_AS, 'Linewidth', 3);
    color = hg.Color;
    hold on;
    
end



grid on

xlabel('Iterations');
ylabel('||r||');
title('Richardson with Schwarz preconditioner (adaptive step-size)')
legend('TL-AS-o0','TL-AS-o1', 'TL-AS-o3');


