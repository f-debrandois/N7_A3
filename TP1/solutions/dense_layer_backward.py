def dense_layer_backward(dy_hat, Wxy, by, activation, cache):
    """
    Implémente la passe backward de la couche dense.

    Arguments :
    dy_hat -- Gradient de la perte J par rapport à la sortie ŷ
    cache -- dictionnaire python contenant des variables utiles (issu de dense_layer_forward())

    Retourne :
    gradients -- dictionnaire python contenant les gradients suivants :
                        dx -- Gradients par rapport aux entrées, de dimension (n_x, m)
                        dby -- Gradients par rapport aux biais, de dimension (n_y, 1)
                        dWxy -- Gradients par rapport aux poids synaptiques Wxy, de dimension (n_y, n_x)
    """
    
    # Récupérer le cache
    (x, z) = cache

    ### A COMPLETER ###   
    # calcul de la sortie en appliquant l'activation
    # dy_dz -- Gradient de la sortie ŷ par rapport à l'état caché z
    if activation == 'relu':
        dy_dz = np.where(z > 0, 1, 0)
    elif activation == 'sigmoid':
        dy_dz = np.exp(-z)/np.square(1 + np.exp(-z))
    else: # Activation linéaire
        dy_dz = np.ones(dy_hat.shape)
        
    # calculer le gradient de la perte par rapport à x
    dx = np.matmul(np.transpose(Wxy), dy_hat*dy_dz)

    # calculer le gradient de la perte par rapport à Wxy
    dWxy = np.matmul(dy_hat*dy_dz, np.transpose(x))

    # calculer le gradient de la perte par rapport à by 
    dby = np.sum(dy_hat*dy_dz, axis=1, keepdims=True)

    ### FIN ###
    
    # Stocker les gradients dans un dictionnaire
    gradients = {"dx": dx, "dby": dby, "dWxy": dWxy}
    
    return gradients