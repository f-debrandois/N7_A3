def mean_square_error(y_true, y_pred):
    loss = np.mean(np.square(y_true - y_pred))
    grad = -2 * (y_true - y_pred) / y_true.shape[0]

    return loss, grad