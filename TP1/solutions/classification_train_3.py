model = MultiLayerPerceptron()
model.add_layer(DenseLayer(2, 10, 'relu'))
model.add_layer(DenseLayer(10, 20, 'relu'))
model.add_layer(DenseLayer(20, 10, 'relu'))
model.add_layer(DenseLayer(10, 10, 'relu'))
model.add_layer(DenseLayer(10, 1, 'sigmoid'))

model = SGD(x_train, y_train, model, 'bce', 0.1, 60, 20)

print_decision_boundaries(model, x, y)