def train_discriminator(model, n_epochs=1000, n_batch=128):
    ''' Train the discriminator model '''
    
    half_batch = int(n_batch / 2)
    
    # run epochs manually
    for step in range(n_epochs):
        # generate real and fake examples
        x_real, y_real = generate_real_samples(half_batch)
        x_fake, y_fake = generate_fake_samples(half_batch)
        
        # update model
        model.train_on_batch(x_real, y_real)
        model.train_on_batch(x_fake, y_fake)
        
        # evaluate the model
        _, acc_real = model.evaluate(x_real, y_real, verbose=0)
        _, acc_fake = model.evaluate(x_fake, y_fake, verbose=0)
        
        if i%10 == 0:
            print('Iter {:d}/{:d}'.format(step,n_epochs))
            print('Accuracy on real data: {:2.4f}  -  Accuracy on fake data: {:2.4f}\n'.format(acc_real, acc_fake))
        
        
# define the discriminator model
discriminator = define_discriminator()

# fit the model
train_discriminator(discriminator)