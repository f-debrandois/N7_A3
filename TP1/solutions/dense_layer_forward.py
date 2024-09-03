def dense_layer_forward(x, Wxy, by, activation):
    """
    Réalise une unique étape forward de la couche dense telle que décrite dans la figure (2)

    Arguments:
    x -- l'entrée, tableau numpy de dimension (n_x, m).
    Wxy -- Matrice de poids multipliant l'entrée, tableau numpy de shape (n_y, n_x)
    by -- Biais additif ajouté à la sortie, tableau numpy de dimension (n_y, 1)
    activation -- Chaîne de caractère désignant la fonction d'activation choisie : 'linear', 'sigmoid' ou 'relu'

    Retourne :
    y_pred -- prédiction, tableau numpy de dimension (n_y, m)
    cache -- tuple des valeurs utiles pour la passe backward (rétropropagation du gradient), contient (x, z)
    """

    # calcul de z
    z = np.matmul(Wxy, x) + by
    # calcul de la sortie en appliquant la fonction d'activation
    if activation == 'relu':
        y = np.maximum(z, 0)
    elif activation == 'sigmoid':
        y = 1/(1 + np.exp(-z))
    elif activation == 'linear':
        y = z
    else:
        print("Erreur : la fonction d'activation n'est pas implémentée.")
    
    # sauvegarde du cache pour la passe backward
    cache = (x, z)
    
    return y, cache