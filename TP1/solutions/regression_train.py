### A COMPLETER ###

model = DenseLayer(1, 1, 'linear')
model = SGD(x_train, y_train, model, 'mse', 0.1, 10, 20)

plt.plot(x_train, y_train, 'b.', label='Ensemble d\'apprentissage')
plt.plot(x_test, y_test, 'r+', label='Ensemble de test')

x_gen = np.expand_dims(np.linspace(-3, 3, 10), 1)
y_gen = np.transpose(model.forward(np.transpose(x_gen)))

plt.plot(x_gen, y_gen, 'g-', label='Prédiction du modèle')
plt.legend()
plt.show()