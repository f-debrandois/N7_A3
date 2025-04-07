function I2hh = interpol(N)

I2hh = zeros(N-1, N/2-1);

for j=1:N/2-1
    i = 2*j -1;
    I2hh(i:i+2,j) = [1 2 1]';
end

I2hh = 0.5*I2hh;
