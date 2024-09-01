# Create the model
model = Sequential()
model.add( Input(shape=(2,)) )
model.add( Dense(units=1, activation='sigmoid') )

# Configure the model and start training
sgd = optimizers.SGD(learning_rate=0.3)
model.compile(optimizer='sgd', loss='BinaryCrossentropy', metrics=['accuracy'])

model.fit(x_train, y_train, verbose=2, epochs=50, batch_size=20)

# Test the model after training
test_results = model.evaluate(x_test, y_test, verbose=1)
print(f'Test results - Loss: {test_results[0]} - Accuracy: {test_results[1]}%')