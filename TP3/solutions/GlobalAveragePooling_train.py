
# Entraînement des dernières couches denses du réseau

conv_base.trainable = False

model.compile(
    loss = 'binary_crossentropy',
    optimizer = optimizers.Adam(learning_rate=3e-4),
    metrics = ['acc']
)

history = model.fit(
    train_generator_augmented,
    epochs = 10,
    validation_data = validation_generator)