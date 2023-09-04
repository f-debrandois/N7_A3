class DenseLayer:
    def __init__(self, input_size, output_size, activation):
        self.input_size = input_size
        self.output_size = output_size
        self.activation = activation
        self.cache = None  # Le cache sera mis à jour lors de la passe forward
        
        ### A COMPLETER ###
        limit = math.sqrt(6 / (input_size + output_size))
        self.Wxy = np.random.uniform(low=-limit, high=limit, size=(output_size, input_size)) # https://www.tensorflow.org/api_docs/python/tf/keras/initializers/GlorotUniform
        self.by = np.zeros((output_size, 1))

    def forward(self, x_batch):
        y, cache = dense_layer_forward(x_batch, self.Wxy, self.by, self.activation)
        self.cache = cache
        return y

    def backward(self, dy):
        return dense_layer_backward(dy, self.Wxy, self.by, self.activation, self.cache)

    def update_parameters(self, gradients, learning_rate):
        self.Wxy -= learning_rate * gradients["dWxy"]
        self.by  -= learning_rate * gradients["dby"]