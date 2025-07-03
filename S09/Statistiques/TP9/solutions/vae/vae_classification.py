x_test_encoded = encoder.predict(x_test, batch_size=batch_size)

fig = plt.figure(figsize=(10, 6))
ax = plt.subplot(1,1,1)

for i in range(10):
    x_test_encoded_i = x_test_encoded[y_test==i]
    plt.scatter(x_test_encoded_i[:, 0], x_test_encoded_i[:, 1], label=i)
ax.grid(False)
plt.legend()

plt.show()