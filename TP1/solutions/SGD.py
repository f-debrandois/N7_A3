def SGD(x_train, y_train, model, loss_function, learning_rate, epochs, batch_size):
    # Nombre de batches par epoch
    nb_batches = math.floor(x_train.shape[0] / batch_size)

    # Pour gérer le tirage aléatoire des batches parmi les données d'entraînement, génération et permutation des indices
    indices = np.arange(x_train.shape[0])
    indices = np.random.permutation(indices)

    for e in range(epochs):

        running_loss = 0

        for b in range(nb_batches):

            # Sélection des données du batch courant
            x_train_batch = x_train[indices[b*batch_size:(b+1)*batch_size]]
            y_train_batch = y_train[indices[b*batch_size:(b+1)*batch_size]]

            # Prédiction du modèle pour le batch courant
            y_pred_batch = model.forward(np.transpose(x_train_batch))

            # Calcul de la perte et des gradients sur le batch courant
            if loss_function == 'mse':
                batch_loss, batch_gradients = mean_square_error(y_train_batch, y_pred_batch)
            elif loss_function == 'bce':
                batch_loss, batch_gradients = binary_cross_entropy(y_train_batch, y_pred_batch)

            running_loss += batch_loss 

            # Calcul du gradient de la perte par rapport aux paramètres du modèle
            param_updates = model.backward(batch_gradients)

            # Mise à jour des paramètres du modèle
            model.update_parameters(param_updates, learning_rate)

        print("Epoch %4d : Loss : %.4f" % (e, float(running_loss/nb_batches)))

        # Nouvelle permutation des données pour la prochaine epoch
        indices = np.random.permutation(indices)
    
    return model