function ump1 = weighted_jacobi(A, um, f, omega, m)

D = diag(diag(A));
Id = speye(size(A,1));
invD = inv(D);
 
for i =1:m
    um = (Id-omega*invD*A)*um + omega*(invD*f);
end

ump1 = um;
