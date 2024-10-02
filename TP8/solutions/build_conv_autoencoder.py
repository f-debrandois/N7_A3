def build_conv_autoencoder():
    conv_encoder = Sequential(name="conv_encoder")
    conv_encoder.add(Input(shape=(28,28,1)))
    conv_encoder.add(Conv2D(16, (3,3) , activation='relu', padding='same' ))
    conv_encoder.add(MaxPooling2D((2, 2), padding='same'))
    conv_encoder.add(Conv2D(8, (3, 3), activation='relu', padding='same'))
    conv_encoder.add(MaxPooling2D((2, 2), padding='same'))
    conv_encoder.add(Conv2D(8, (3, 3), activation='relu', padding='same'))
    conv_encoder.add(MaxPooling2D((2, 2), padding='same'))

    conv_decoder = Sequential(name="conv_decoder")
    conv_decoder.add(Input(shape = (4, 4, 8)))
    conv_decoder.add(Conv2D(8, (3, 3), activation='relu', padding='same'))
    conv_decoder.add(UpSampling2D((2, 2)))
    conv_decoder.add(Conv2D(8, (3, 3), activation='relu', padding='same'))
    conv_decoder.add(UpSampling2D((2, 2)))
    conv_decoder.add(Conv2D(16, (3, 3), activation='relu'))
    conv_decoder.add(UpSampling2D((2, 2)))
    conv_decoder.add(Conv2D(1, (3, 3), activation='sigmoid', padding='same'))

    conv_autoencoder = Sequential(name="conv_autoencoder")
    conv_autoencoder.add(conv_encoder)
    conv_autoencoder.add(conv_decoder)

    return conv_autoencoder