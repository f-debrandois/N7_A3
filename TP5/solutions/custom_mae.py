# y_true : vérité terrain de dimension B x 3 x 14
# y_pred : une prédiction de dimension B x 2 x 14 (on ne prédit pas la visibilité)
# B est le nombre d'images considérées (par exemple, pourra être la taille d'un mini-batch)

def custom_mae(y_true, y_pred):
    y_true = K.permute_dimensions(y_true, (0, 2, 1))
    y_true = K.reshape(y_true, shape=(-1, 3))
  
    y_pred = K.permute_dimensions(y_pred, (0, 2, 1))
    y_pred = K.reshape(y_pred, shape=(-1, 2))
    
    visible = K.greater_equal(y_true[:, 2], 1)  
    indices = K.arange(0, K.shape(y_true)[0])
    indices_visible = indices[visible]
    
    y_true_visible = K.gather(y_true[:,0:2], indices_visible)
    y_pred_visible = K.gather(y_pred, indices_visible)
    
    return K.mean(K.abs(y_pred_visible[:,0] - y_true_visible[:,0]) + K.abs(y_pred_visible[:,1] - y_true_visible[:,1]))