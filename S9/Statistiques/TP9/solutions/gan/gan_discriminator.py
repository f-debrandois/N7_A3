# define the standalone discriminator model
def define_discriminator(n_inputs=2):
    discriminator = keras.Sequential(name='discriminator')
    discriminator.add(kl.Dense(25, activation='relu', input_dim=n_inputs, kernel_initializer='he_uniform'))  #kernel_initializer='he_uniform'
    discriminator.add(kl.Dense(1, activation='sigmoid'))

    # compile model
    discriminator.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    return discriminator
 
    
# define the discriminator model
discriminator = define_discriminator()
discriminator.summary()