conv_autoencoder = build_conv_autoencoder()
conv_autoencoder.compile(optimizer='Adam', loss='binary_crossentropy')

conv_autoencoder.fit(x_train_noisy, x_train,
  epochs=10,
  batch_size=256,
  validation_data=(x_test_noisy, x_test))