input_dim = x_train.shape[1]
print(f'Feature dim: {input_dim}')

# Create the model
model = Sequential()
model.add( Input(shape=(input_dim,)) )
model.add( Dense(units=10, activation='relu') )
model.add( Dense(units=1, activation='sigmoid') )

# Configure the model and start training
sgd = optimizers.SGD(learning_rate=0.1)
model.compile(loss='BinaryCrossentropy', optimizer='sgd', metrics=['accuracy'])
model.fit(x_train, y_train, epochs=60, batch_size=20, verbose=1)

# Test the model after training
test_results = model.evaluate(x_test, y_test, verbose=1)
print(f'Test results - Loss: {test_results[0]} - Accuracy: {test_results[1]}%')