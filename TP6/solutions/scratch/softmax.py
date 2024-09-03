def softmax(x):
    # Applies the Softmax function to the input array.
    return np.exp(x) / np.sum(np.exp(x))