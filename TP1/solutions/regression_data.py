x, y = datasets.make_regression(n_samples=250, n_features=1, n_targets=1, random_state=1, noise=10)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=1/10, random_state=1)
x_train, x_val, y_train, y_val = train_test_split(x_train, y_train, test_size=1/9, random_state=1)

plt.plot(x_train, y_train, 'b.', label='Ensemble d\'apprentissage')
plt.plot(x_test, y_test, 'r+', label='Ensemble de test')

plt.legend()
plt.show()