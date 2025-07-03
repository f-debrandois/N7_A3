n = 100
f = lambda x: x*x

def generate_samples(fun=f,n=100):    
    # generate random inputs in [-0.5, 0.5]
    x1 = np.random.rand(n) - 0.5
    # generate outputs x^2 (quadratic)
    x2 = fun(x1)
    # stack arrays
    x1 = x1.reshape(n, 1)
    x2 = x2.reshape(n, 1)
    return np.hstack((x1, x2))
 
    
# generate samples
x = generate_samples()

# plot samples
fig, ax = plt.subplots(1, 1, figsize = (8,5))
plt.scatter(x[:, 0], x[:, 1])
ax.grid(False)
plt.show()