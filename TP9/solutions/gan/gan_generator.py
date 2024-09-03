# define the standalone generator model
def define_generator(latent_dim=5, n_outputs=2):
    generator = keras.Sequential(name='generator')
    generator.add(kl.Dense(15, activation='relu', input_dim=latent_dim, kernel_initializer='he_uniform'))
    generator.add(kl.Dense(n_outputs, activation='linear'))
    return generator

# define the generator model
generator = define_generator()

# summarize the model
generator.summary()