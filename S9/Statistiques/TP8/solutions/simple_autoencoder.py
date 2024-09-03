simple_autoencoder = Sequential(name = "simple_autoencoder")
simple_autoencoder.add(Dense(n_latent, activation='relu', input_shape=(n_input,),name="encoder_layer"))
simple_autoencoder.add(Dense(n_input, activation='sigmoid', name = "decoder_layer" ))
simple_autoencoder.summary()