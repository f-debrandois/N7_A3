batch_size = 256
epochs = 30

model.compile(optimizer = 'rmsprop', 
              loss = 'categorical_crossentropy',
              metrics = ['accuracy'],
             )

history = model.fit(X_train,
                    y_train,
                    batch_size = batch_size, 
                    epochs = epochs, 
                    verbose = 1, 
                    validation_split = .3,
                   )