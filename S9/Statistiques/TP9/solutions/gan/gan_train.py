def train(gan, generator, discriminator, latent_dim=5, n_epochs=10000, n_batch=128, n_eval=200):
    '''train the generator and discriminator'''
    
    # determine half the size of one batch, for updating the discriminator
    half_batch = int(n_batch / 2)
    
    # manually enumerate epochs
    for step in range(n_epochs+1):
        # prepare real and fake samples
        x_real, y_real = generate_real_samples(half_batch)
        x_fake, y_fake = generate_fake_samples(generator, latent_dim, half_batch)
        
        # update discriminator
        discriminator.train_on_batch(x_real, y_real)
        discriminator.train_on_batch(x_fake, y_fake)
        
        # points in latent inverted labels, as input for the generator
        x = np.random.randn(n_batch,latent_dim)
        y = np.ones((n_batch, 1))
        
        # update the generator via the discriminator's error
        gan.train_on_batch(x, y)
        
        # evaluate the model every n_eval epochs
        if step % n_eval == 0:
            visualize_performance(step, generator, discriminator, latent_dim, n_epochs, half_batch)
        
        # Training step
        if (step+1) % 10 == 0:
            print('.', end='', flush=True)