model = MultiLayerPerceptron()
model.add_layer(DenseLayer(2, 10, 'relu'))
model.add_layer(DenseLayer(10, 1, 'sigmoid'))

model = SGD(x, y, model, 'bce', 0.1, 75, 20)

print_decision_boundaries(model, x, y)