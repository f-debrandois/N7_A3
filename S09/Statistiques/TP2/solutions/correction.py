# Création d'un ensemble de validation
(x, y), (x_test, y_test) = boston_housing.load_data()
x_train, x_val, y_train, y_val = train_test_split(x, y, test_size=1/10, random_state=2)

# Activation linéaire sur la couche de sortie
model = Sequential()
model.add(Dense(4, activation='relu', input_dim=13))
model.add(Dense(1, activation='linear'))

optim = optimizers.Adam(learning_rate = 0.01)
model.compile(optimizer=optim, loss='mse', metrics=['mae'])

# Calcul de l'erreur de validation au cours de l'optimisation
history = model.fit(x_train, y_train, validation_data=(x_val, y_val), epochs=50, batch_size=32)