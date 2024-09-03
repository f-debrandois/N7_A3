sparse_encoded_imgs = sparse_encoder.predict(x_test)
sparse_decoded_imgs = sparse_decoder.predict(sparse_encoded_imgs)

encoded_imgs = encoder.predict(x_test)
decoded_imgs = decoder.predict(encoded_imgs)

# --- #

n = 10
idx = [random.randint(0, x_test.shape[0]) for _ in range(0, n)]

plt.figure(figsize=(20, 8))
for i in range(n):
    # display original
    ax = plt.subplot(5, n, i+1)
    plt.imshow(x_test[idx[i]].reshape(28, 28))
    plt.gray()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    
    # display encoded
    ax = plt.subplot(5, n, i+1 + n)
    plt.imshow(encoded_imgs[idx[i]].reshape(4,8))
    plt.gray()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    
    # display sparse_encoded
    ax = plt.subplot(5, n, i+1 + 2*n)
    plt.imshow(sparse_encoded_imgs[idx[i]].reshape(4,8))
    plt.gray()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    
    # display decoded
    ax = plt.subplot(5, n, i+1 + 3*n)
    plt.imshow(decoded_imgs[idx[i]].reshape(28,28))
    plt.gray()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    
    # display sparse_decoded
    ax = plt.subplot(5, n, i+1 + 4*n)
    plt.imshow(sparse_decoded_imgs[idx[i]].reshape(28,28))
    plt.gray()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

title = ['test data','encoded','sparse encoded','decoded','sparse decoded']
for i in range(5) :  
    ax = plt.subplot(5,n,1+i*n)
    plt.title(title[i])

#plt.tight_layout()
plt.show()