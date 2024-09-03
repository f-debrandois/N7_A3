def visualize_performance(step, generator, discriminator, latent_dim=5, n_epochs=10000, n=100):
    '''Evaluate the discriminator and plot real and fake points'''
    
    # Generate real and fake samples
    x_real, y_real = generate_real_samples(n)
    x_fake, y_fake = generate_fake_samples(generator, latent_dim, n)
    
    # evaluate discriminator
    _, acc_real = discriminator.evaluate(x_real, y_real, verbose=0)
    _, acc_fake = discriminator.evaluate(x_fake, y_fake, verbose=0)
    
    print('\n')
    print('Iter {:d}/{:d}'.format(step,n_epochs))
    print('Accuracy on real data: {:2.4f}  -  Accuracy on fake data: {:2.4f}\n'.format(acc_real, acc_fake))
     
    # plot samples
    fig = plt.figure(figsize=(8,5))
    ax = plt.subplot(1,1,1)

    plt.scatter(x_real[:, 0], x_real[:, 1], color="purple", alpha=.5, label="Real data")
    plt.scatter(x_fake[:, 0], x_fake[:, 1], color="skyblue", alpha=.5, label="Fake data") 

    ax.grid(False)
    plt.show()