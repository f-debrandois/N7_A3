def create_new_model(image_size=150, choice='CNN'):
    model = models.Sequential()
    
    if choice == 'CNN':
        model.add(Conv2D(32,(3,3),input_shape=(image_size,image_size,3),activation='relu'))
        model.add(MaxPooling2D(pool_size=(2,2)))
        model.add(Conv2D(64,(3,3),activation='relu'))
        model.add(MaxPooling2D(pool_size=(2,2)))
        model.add(Conv2D(96,(3,3),activation='relu'))
        model.add(MaxPooling2D(pool_size=(2,2)))
        model.add(Conv2D(128,(3,3),activation='relu'))
        model.add(MaxPooling2D(pool_size=(2,2)))
        model.add(Flatten())
        model.add(Dense(512,activation='relu'))
        model.add(Dense(1,activation='sigmoid'))
        
    elif choice == 'VGG16':
        conv_base = VGG16(
            weights = 'imagenet',
            include_top = False,
            input_shape = (150, 150, 3)
        )
        model.add(conv_base)
        model.add(layers.Flatten())
        model.add(layers.Dense(256, activation='relu'))
        model.add(layers.Dense(1, activation='sigmoid'))
        conv_base.trainable = False
    
    else:
        print("Network not implemented")
        
    return model