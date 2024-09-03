x, y = datasets.make_blobs(n_samples=250, n_features=2, centers=2, center_box=(- 3, 3), random_state=1)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=1/10, random_state=1)
x_train, x_val, y_train, y_val = train_test_split(x_train, y_train, test_size=1/9, random_state=1)

plt.plot(x_train[y_train==0,0], x_train[y_train==0,1], 'b.')
plt.plot(x_train[y_train==1,0], x_train[y_train==1,1], 'r.')

plt.plot(x_test[y_test==0,0], x_test[y_test==0,1], 'b+')
plt.plot(x_test[y_test==1,0], x_test[y_test==1,1], 'r+')

plt.show()