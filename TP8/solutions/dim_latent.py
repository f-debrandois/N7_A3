vect_latent = []
vect_reconstruction_loss = []

for n_latent in range(10, 50, 10):
    print("Dimension espace latent : "+str(n_latent))
    autoencoder, encoder, decoder = build_autoencoder(n_latent)
    autoencoder.compile(optimizer='Adam', loss='binary_crossentropy')

    autoencoder.fit(x_train, x_train,
                  epochs=50,
                  batch_size=128,
                  shuffle=True,
                  validation_data=(x_test, x_test))

    loss = autoencoder.evaluate(x_test, x_test)
    vect_latent.append(n_latent)
    vect_reconstruction_loss.append(loss)
    print(" ")

# --- #

plt.plot(vect_latent, vect_reconstruction_loss, 'b')
plt.show()