# Evaluation du modèle
train_loss=(history.history['mae'])
val_loss=(history.history['val_mae'])
plot_loss(val_loss, train_loss, ymax=30)

model.evaluate(x_test, y_test)