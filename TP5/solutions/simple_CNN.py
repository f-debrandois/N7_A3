def simple_CNN(image_size=64):
    # Définition du modèle simple, de type "LeNet" (§ 4.1.1)
    
    model = models.Sequential()
    
    model.add(Conv2D(32,(3,3), padding='same', input_shape=(image_size,image_size,3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(64,(3,3), padding='same', activation='relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(96,(3,3), padding='same', activation='relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Conv2D(128,(3,3), padding='same', activation='relu'))
    model.add(MaxPooling2D(pool_size=(2,2)))
    
    model.add(Flatten())
    model.add(Dense(512, activation='relu'))
    model.add(Dense(28, activation='linear'))
    model.add(Reshape((2,14)))

    return model