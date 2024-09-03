(x, y), (x_test, y_test) = boston_housing.load_data()
x_train, x_val, y_train, y_val = train_test_split(x, y, test_size=1/10, random_state=2)

# Normalisation des entrées
x_mean = np.mean(x_train, axis=0)
x_std = np.std(x_train, axis=0)

x_train = (x_train-x_mean)/x_std
x_val = (x_val-x_mean)/x_std
x_test = (x_test-x_mean)/x_std

print(x_train)
print(x_std)


# ------ #
print(" ")
print(" ")
# ------ #


model = Sequential()
model.add(Input(shape=(13,)))
model.add(Dense(10, activation='relu'))
model.add(Dense(100, activation='relu'))
model.add(Dense(50, activation='relu'))  # kernel_regularizer=regularizers.L1(0.01)
model.add(Dense(100, activation='relu'))
model.add(Dense(1, activation='linear'))


optim = optimizers.Adam(learning_rate = 0.01)
model.compile(optimizer=optim, loss='mse', metrics=['mae'])

history = model.fit(x_train, y_train, validation_data=(x_val, y_val), epochs=100, batch_size=32)