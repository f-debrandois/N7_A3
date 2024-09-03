x_test_encoded_ad = encoder_ad.predict(x_test_ad, batch_size=batch_size)
anomaly_encoded = encoder_ad.predict(anomaly_test, batch_size=batch_size)

fig = plt.figure(figsize=(10, 6))
ax = plt.subplot(1,1,1)
    
plt.scatter(x_test_encoded_ad[:, 0], x_test_encoded_ad[:, 1], color="skyblue", alpha=.5, label="Normal")
plt.scatter(anomaly_encoded[:, 0], anomaly_encoded[:, 1], color="purple", alpha=.5, label="Outliers") 
    
ax.grid(False)
plt.legend()
plt.show()