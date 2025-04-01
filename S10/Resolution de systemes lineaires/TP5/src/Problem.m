classdef Problem
    properties
        n_dofs          % Number of dofs in V
        h               % Mesh size
        A               % Stifness matrix
        rhs             % Right-hand side
        
        n_subd          % Number of subdomains
        n_loc           % Number of dofs per subdomain
        overlap         % Overlap
        I               % Interpolation matrices for local spaces
        I_coarse        % Interpolation matrices for coarse space - Nicolaides approach
        I_coarse_geo    % Interpolation matrices for coarse space - geometric approach
        D               % Scaling matrices
    end
    
    methods
        function obj = Problem(n_subd, n_loc, overlap)
            obj.n_subd  = n_subd;
            obj.overlap = overlap;
            obj.n_loc   = n_loc;
            
            obj.n_dofs = n_subd*n_loc - (n_subd-1)*overlap;
            obj.h = 1/(obj.n_dofs-1);
            
            obj.A   = sparse(diag(2*ones(obj.n_dofs,1)) - diag(ones(obj.n_dofs-1,1),1) - diag(ones(obj.n_dofs-1,1),-1)) ./ obj.h; % (for simplicity)
            obj.rhs = ones(obj.n_dofs, 1)*obj.h;
            
            obj = obj.assembly_interpolation_subdomains();
            obj = obj.assembly_interpolation_coarse();
            obj = obj.assembly_subdomain_scaling_matrices();
            
            obj = obj.assembly_interpolation_coarse_geo();
            
        end
        
        
        function [obj]  = assembly_subdomain_scaling_matrices(obj)
            %   Assembly scaling matrices for local spaces
            obj.D = cell(obj.n_subd,1);
            for i = 1:obj.n_subd
                d= ones(obj.n_loc, 1);
                
                % TODO:: modify d accordingly, so it scales corrections in
                % overlapping region following the partition of unity
                % approach
                % .......
                
                obj.D{i} = diag(d);
            end
        end
        
        
        function [obj]  = assembly_interpolation_subdomains(obj)
            % Assembly interpolation matrices for local spaces
            obj.I = cell(obj.n_subd,1);
            for i = 1:obj.n_subd
                obj.I{i} = sparse(obj.n_dofs, obj.n_loc);
                left = (i-1)*(obj.n_loc-obj.overlap) + 1;
                right = left + obj.n_loc-1;
                obj.I{i}(left:right,1:obj.n_loc) = eye(obj.n_loc);
            end
        end
        
        
        function [obj]  = assembly_interpolation_coarse(obj)
            % Assembly interpolation matrix for coarse space
            % Use Nicolaides approach
            obj.I_coarse = zeros(obj.n_dofs, obj.n_subd);
            
            for i = 1:obj.n_subd
                % Add appropriate entries of interpolation operator
                
            end
        end
        
        
        function [obj]  = assembly_interpolation_coarse_geo(obj)
            % Assembly interpolation matrix for coarse space
            % Use geometric approach, where you coarsen by factor of two
            obj.I_coarse_geo = zeros(obj.n_dofs, floor(obj.n_dofs/2-1));
            
            % TODO:: implement correctly entries of obj.I_coarse_geo
            
        end
        
        
        function [sol, iters, res] = solve_pcg(obj)
            [sol,~,~,iters, res] = pcg(obj.A, obj.rhs, 1e-8, 5000);
        end
        
        
        function [sol, iters, res] = solve_pcg_precond_AS(obj)
            [sol,~,~,iters, res] = pcg(obj.A, obj.rhs, 1e-8, 5000, @(r)obj.apply_AS(r));
        end
        
        
        function [sol, iters, rnorms] = solve_pcg_precond_two_level_AS_additive(obj)
            [sol,~,~,iters, rnorms] = pcg(obj.A, obj.rhs, 1e-8, 5000, @(r)obj.apply_two_level_AS_multiplicative_coarse_first(r));
        end
        
        
        function [sol, iters, rnorms] = solve_richardson(obj, flg, alpha0)
            
            iters = 1;
            converged = false;
            sol = ones(size(obj.rhs));
            max_it = 3000;
            atol = 1e-8;
            
            
            r = obj.rhs - obj.A*sol;
            rnorms(iters) =  norm(r);
            
            while ~converged
                
                if(flg=="AS")
                    corr = obj.apply_AS(r);
                elseif(flg=="RAS")
                    corr = obj.apply_RAS(r);
                elseif (flg=="TL_AS_add")
                    corr = obj.apply_two_level_AS_additive(r);
                elseif (flg=="TL_AS_mult_coarse_first")
                    corr = obj.apply_two_level_AS_multiplicative_coarse_first(r);
                elseif (flg=="TL_AS_mult_coarse_second")
                    corr = obj.apply_two_level_AS_multiplicative_coarse_second(r);
                elseif (flg=="TG")
                    corr = obj.apply_TG(r);
                elseif (flg=="TG_geo")
                    corr = obj.apply_TG_geo(r);
                else
                    corr = r;
                end
                
                
                if(alpha0==-1)
                    alpha = dot(corr, r)/dot(obj.A*corr, corr);
                else
                    alpha = alpha0;
                end
                
                
                sol = sol + alpha*corr;
                
                r = obj.rhs - obj.A*sol;
                
                iters = iters+1;
                rnorms(iters) =  norm(r);
                
                if(iters > max_it || rnorms(iters) < atol)
                    converged = true;
                end
                
            end
            
            
        end
        
        
        function corr = apply_AS(obj, rhs)
            % One step of the one-level additive Schwarz method.
            % INPUT PARAMETERS:
            %   * rhs: right-hand side/residual
            % OUTPUT:
            %   * corr: preconditioned residual / correction
            
            
            % Restrict residual to V_0,V_1,...,V_S
            rloc = zeros(obj.n_loc, obj.n_subd);
            for i = 1:obj.n_subd
                rloc(:,i) = obj.I{i}'*rhs;
            end
            
            % Solve subproblems in V_0,V_1,...,V_S
            corrloc = zeros(obj.n_loc, obj.n_subd);
            for i = 1:obj.n_subd
                A_loc   =  obj.I{i}'*obj.A*obj.I{i};
                corrloc(:,i) = A_loc\rloc(:,i);
            end
            
            % Add corrections
            corr = zeros(obj.n_dofs,1);
            for i = 1:obj.n_subd
                corr = corr + obj.I{i}*corrloc(:,i);
            end
            
        end
        
        
        function corr = apply_RAS(obj, rhs)
            % One step of the one-level restricted additive Schwarz method.
            % INPUT PARAMETERS:
            %   * rhs: right-hand side/residual
            % OUTPUT:
            %   * corr: preconditioned residual / correction
            
            
            % Restrict residual to V_0,V_1,...,V_S
            rloc = zeros(obj.n_loc, obj.n_subd);
            for i = 1:obj.n_subd
                rloc(:,i) =  obj.I{i}'*rhs;
            end
            
            % Solve subproblems in V_0,V_1,...,V_S
            corrloc = zeros(obj.n_loc, obj.n_subd);
            for i = 1:obj.n_subd
                A_loc   =  obj.I{i}'*obj.A*obj.I{i};
                corrloc(:,i) = A_loc\rloc(:,i);
            end
            
            % Add corrections
            corr = zeros(obj.n_dofs,1);
            for i = 1:obj.n_subd
                corr = corr + obj.I{i}*corrloc(:,i);
            end
            
        end
        
        
        function corr = apply_two_level_AS_additive(obj, rhs)
            % One step of the two-level additive Schwarz method with additively added coarse-space.
            % INPUT PARAMETERS:
            %   * rhs: right-hand side/residual
            % OUTPUT:
            %   * corr: preconditioned residual / correction
            
            corr = obj.apply_AS(rhs);
            
            %             r_coarse = ...
            %             A_coarse = ...
            %             corr_coarse = ..
            
            % corr = corr +  ...
        end
        
        
        
        
        function corr = apply_two_level_AS_multiplicative_coarse_first(obj, rhs)
            % One step of the two-level additive Schwarz method with additively added coarse-space before the subdomain solve.
            % INPUT PARAMETERS:
            %   * rhs: right-hand side/residual
            % OUTPUT:
            %   * corr: preconditioned residual / correction
            
            
            corr = obj.apply_AS(rhs);
            
            %             r = ...
            %             r_coarse = ...
            %             A_coarse = ...
            %             corr_coarse = ...
            %
            %             corr = ...
        end
        
        
        function corr = apply_two_level_AS_multiplicative_coarse_second(obj, rhs)
            % One step of the two-level additive Schwarz method with additively added coarse-space after the subdomain solve.
            % INPUT PARAMETERS:
            %   * rhs: right-hand side/residual
            % OUTPUT:
            %   * corr: preconditioned residual / correction
            
            corr = 0.0*rhs;
            
            %             r_coarse = ...
            %             A_coarse = ...
            %             corr_coarse = ...
            
            %             corr = ...
            %             r = ...
            %             corr = corr + obj.apply_AS(r);
            
        end
        
        function corr = apply_TG(obj, rhs)
            % One step of two-level multigrid method with AS smoother
            % INPUT PARAMETERS:
            %   * rhs: right-hand side/residual
            % OUTPUT:
            %   * corr: preconditioned residual / correction
            
            corr = 0*rhs;
            
            %             % Call smoother
            %             corr = ...
            %
            %             % Coarse-step
            %             r = ...
            %             r_coarse = ...
            %             A_coarse = ...
            %             corr_coarse = ...
            %             corr = ...
            %
            %             % Call smoother
            %             r = ...
            %             corr = ...
        end
        
        
        function corr = apply_TG_geo(obj, rhs)
            % One step of two-level multigrid method with AS smoother
            % INPUT PARAMETERS:
            %   * rhs: right-hand side/residual
            % OUTPUT:
            %   * corr: preconditioned residual / correction
            
            corr = 0*rhs;
            
            % Call smoother
            %             corr = ...
            
            % Call coarse-step
            %r = ...
            %r_coarse = ...
            %A_coarse = ...
            %corr_coarse = ...
            %corr = ...
            
            % Call smoother
            %r = ...
            %corr = ...
        end
        
        
    end
end

