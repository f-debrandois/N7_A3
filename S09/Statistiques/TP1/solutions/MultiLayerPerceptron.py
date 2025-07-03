class MultiLayerPerceptron:
    def __init__(self):
        self.layers = []

        
    def add_layer(self, layer):
        self.layers.append(layer)

        
    def forward(self, x_batch):
        output_l = x_batch

        for i in range(len(self.layers)):
            # La sortie de la couche précédente est passée en entrée de la couche courante
            input_l = output_l
            output_l = self.layers[i].forward(input_l)  
      
        # La sortie de la dernière couche est la sortie finale du réseau
        y = output_l

        return y
     
        
    def backward(self, dy):
        gradients = []
      
        for i in reversed(range(len(self.layers))):
            # La sortie de la couche précédente est passée en entrée de la couche courante
            layer_gradients = self.layers[i].backward(dy)  
            gradients.append(layer_gradients) 
            dy = layer_gradients["dx"]
      
        gradients.reverse()
        return gradients


    def update_parameters(self, gradients, learning_rate):
        for i in range(len(self.layers)):
            self.layers[i].update_parameters(gradients[i], learning_rate)