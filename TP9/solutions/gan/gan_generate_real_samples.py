def generate_real_samples(n=100):
    x = generate_samples(n=n)
    y = np.ones((n, 1))
    return x, y

def generate_fake_samples(n=100):
    x = 2*np.random.rand(n,2)-1
    y = np.zeros((n, 1))
    return x, y


# generate samples
x_real, y_real = generate_real_samples()
x_fake, y_fake = generate_fake_samples()

# plot samples
fig, ax = plt.subplots(1, 1, figsize = (8,5))

plt.scatter(x_real[:, 0], x_real[:, 1], color="purple", alpha=.5, label="Real data")
plt.scatter(x_fake[:, 0], x_fake[:, 1], color="skyblue", alpha=.5, label="Fake data") 

ax.grid(False)
plt.show()