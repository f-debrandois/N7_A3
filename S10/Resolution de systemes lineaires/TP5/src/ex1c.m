clc; clear; close all; 

n_subdomains  = 10;
local_dofs    = 10;

overlaps = [1, 3, 5]; 


figure;
for i =1:size(overlaps, 2)
	problem = Problem(n_subdomains, local_dofs,  overlaps(i));
    
    [x_AS, iters_AS, res_AS] = problem.solve_richardson("RAS", 1);
    semilogy(res_AS, ':', 'Linewidth', 3);
    hold on;        
    
end



grid on

xlabel('Iterations');
ylabel('||r||');
title('Schwarz preconditioners: RAS')
legend('TL-RAS-o1', 'TL-RAS-o3', 'TL-RAS-o5');







figure;
for i =1:size(overlaps, 2)
	problem = Problem(n_subdomains, local_dofs,  overlaps(i));
    
    [x_RAS, iters_RAS, res_RAS] = problem.solve_richardson("AS", -1);
    hg = semilogy(res_RAS, 'Linewidth', 3);
    color = hg.Color;
    hold on;
    
    
    [x_AS, iters_AS, res_AS] = problem.solve_richardson("RAS", -1);
    semilogy(res_AS, ':', 'Color', 0.7*color, 'Linewidth', 3);
    hold on;        
    
end



grid on

xlabel('Iterations');
ylabel('||r||');
title('Schwarz preconditioners: AS vs RAS')
legend('TL-AS-o1','TL-RAS-o1', 'TL-AS-o3','TL-RAS-o3', 'TL-AS-o5','TL-RAS-o5');



