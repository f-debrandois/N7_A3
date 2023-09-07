model.compile(
    loss = 'binary_crossentropy',
    optimizer = optimizers.Adam(learning_rate=3e-4),
    metrics = ['acc']
)

history = model.fit(
    train_generator_augmented, 
    validation_data = validation_generator,
    epochs=50
)