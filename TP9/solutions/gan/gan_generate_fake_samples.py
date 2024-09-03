def generate_fake_samples(model, latent_dim=5, n=100):
    '''use the generator to generate n fake examples'''
    
    # generate n points in the latent space, according to a Gaussian distribution
    x_latent = np.random.randn(n,latent_dim)

    # predict and label outputs
    x = model.predict(x_latent)
    y = np.zeros((n, 1))
    return x, y