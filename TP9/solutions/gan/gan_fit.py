latent_dim = 5
n_inputs = 2
n_outputs = 2

n_epochs = 10000
n_batch = 128
n_eval = 2000


# create the GAN model
discriminator = define_discriminator(n_inputs)
generator = define_generator(latent_dim, n_outputs)
gan = define_gan(generator, discriminator)

# train model
train(gan, generator, discriminator, latent_dim, n_epochs, n_batch, n_eval)