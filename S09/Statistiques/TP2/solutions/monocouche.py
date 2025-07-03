model = Sequential()
model.add(Dense(1, activation='linear', input_dim=13))

optim = optimizers.Adam(learning_rate = 0.01)
model.compile(optimizer=optim, loss='mse', metrics=['mae'])

history = model.fit(x_train, y_train, validation_data=(x_val, y_val), epochs=100, batch_size=16)