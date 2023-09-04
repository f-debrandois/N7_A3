# Create the model
model = Sequential()
model.add( Dense(units=1, input_dim=1, activation='linear') )

# Configure the model and start training
sgd = optimizers.SGD(learning_rate=0.1)
model.compile(optimizer='sgd', loss='mean_squared_error')

model.fit(x_train, y_train, verbose=2, epochs=10, batch_size=20)

# --- #

plt.plot(x_train, y_train, 'b.', label='Ensemble d\'apprentissage')
plt.plot(x_test, y_test, 'r+', label='Ensemble de test')

x_gen = np.linspace(-3, 3, 10)
y_gen = model.predict(x_gen)

plt.plot(x_gen[:], y_gen[:], 'g-', label='Prédiction du modèle')
plt.legend()
plt.show()