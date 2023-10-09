encoder_ad, decoder_ad, vae_ad = make_vae()
vae_ad.compile(optimizer='adam')

vae_ad.fit(x_train_ad, 
           epochs = 40, 
           batch_size = batch_size, 
           validation_data = (x_test_ad, None))