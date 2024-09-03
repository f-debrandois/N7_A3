n = 10
m = 10

# We keep the same data as before
# idx = [rd.randint(0, x_test.shape[0]) for _ in range(0, n)]

encoder_seq, decoder_seq, vae_seq = make_vae()
vae_seq.compile(optimizer='adam')

plt.figure(figsize=(2*n, 2*(m+2)))


# display original
for i in range(n):
    ax = plt.subplot(m+2, n, i+1)
    plt.imshow(x_test[idx[i]].reshape(28, 28))
    plt.gray()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    
    
print("=== Epoch 0/"+str(m)+" ===")
x_test_decoded_vae_seq = vae_seq.predict(x_test, batch_size=batch_size)

# display initialization
for i in range(n):
    ax = plt.subplot(m+2, n, i+1 + n)
    plt.imshow(x_test_decoded_vae_seq[idx[i]].reshape(28, 28))
    plt.title('Init')
    plt.gray()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    
for j in range(m):
    print("=== Epoch "+str(j+1)+"/"+str(m)+" ===")  
    vae_seq.fit(x_train,
            epochs=1,
            batch_size=batch_size,
            validation_data=(x_test, None),
            verbose=0)
    
    x_test_decoded_vae_seq = vae_seq.predict(x_test, batch_size=batch_size)
    
    # display reconstruction
    for i in range(n):
        ax = plt.subplot(m+2, n, i+1 + (j+2)*n)
        plt.imshow(x_test_decoded_vae_seq[idx[i]].reshape(28, 28))
        plt.title('Epoch '+str(j))
        plt.gray()
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)
            
plt.show()
plt.tight_layout()