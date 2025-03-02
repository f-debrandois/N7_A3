def build_sparse_autoencoder(n_latent=32, l=1e-4):
    # Dimension de l'entrée
    input_img = Input(shape=(n_input,))

    # Définition de l'encoder
    x = Dense(128, activation='relu')(input_img)
    encoded = Dense(n_latent, activation='linear', activity_regularizer = regularizers.l1(l))(x)
    encoder = Model(input_img, encoded, name = "sparse_encoder")

    # Définition du decoder
    decoder_input = Input(shape=(n_latent,))
    x = Dense(128, activation='relu')(decoder_input)
    decoded = Dense(784, activation='sigmoid')(x)
    decoder = Model(decoder_input, decoded, name = "decoder")

    # Construction de l'auto-encodeur
    encoded = encoder(input_img)
    decoded = decoder(encoded)
    autoencoder = Model(input_img, decoded, name = "sparse_autoencoder")

    return autoencoder, encoder, decoder