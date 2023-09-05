def plot_loss(val_loss, train_loss, ymax=100):
    plt.plot(val_loss, color='green', label='Erreur de validation')
    plt.plot(train_loss, color='blue', linestyle='--', label='Erreur d\'entraînement')
    plt.xlabel('Epochs')
    plt.ylim(0, ymax)
    plt.title('Évolution de la perte sur les ensembles d\'apprentissage et de validation au cours de l\'apprentissage')
    plt.legend()