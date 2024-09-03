def binary_cross_entropy(y_true, y_pred):
    loss = np.mean(- y_true * np.log(y_pred) - (1 - y_true) * np.log(1 - y_pred))
    grad =  (- y_true / y_pred + (1 - y_true) / (1 - y_pred))/y_true.shape[0]

    return loss, grad