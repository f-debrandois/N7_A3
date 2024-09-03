# 1- Initialisation des paramètres du modèle

model = DenseLayer(2, 1, 'sigmoid')
model = SGD(x_train, y_train, model, 'bce', 0.3, 50, 20)

plt.plot(x_train[y_train==0,0], x_train[y_train==0,1], 'b.')
plt.plot(x_train[y_train==1,0], x_train[y_train==1,1], 'r.')

plt.plot(x_test[y_test==0,0], x_test[y_test==0,1], 'b+')
plt.plot(x_test[y_test==1,0], x_test[y_test==1,1], 'r+')

x_gen = np.linspace(-6, 2, 10)
y_gen = -model.Wxy[0,0]*x_gen/model.Wxy[0,1] - model.by[0,0]/model.Wxy[0,1]

plt.plot(x_gen, y_gen, 'g-')

plt.show()