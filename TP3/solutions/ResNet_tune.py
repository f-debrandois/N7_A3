conv_base.trainable = True

model.compile(
    loss = 'binary_crossentropy',
    optimizer = optimizers.Adam(learning_rate=1e-5), # Taux d'apprentissage réduit
    metrics = ['acc']
)

history = model.fit(
    train_generator_augmented,
    epochs = 10,
    validation_data = validation_generator
)