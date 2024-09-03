# Regular data
x_test_decoded_ad = vae_ad.predict(x_test_ad, batch_size=batch_size)
mse_normal = np.linalg.norm(x_test_ad-x_test_decoded_ad, axis=1)

# Outliers data
anomaly_decoded = vae_ad.predict(anomaly_test, batch_size=batch_size)
mse_outliers = np.linalg.norm(anomaly_test-anomaly_decoded, axis=1)

# Random data
x_random = np.random.uniform(size=(1000, 784),low=0.0, high=1.0)
x_random_decoded =  vae_ad.predict(x_random, batch_size=batch_size)
mse_random = np.linalg.norm(x_random-x_random_decoded, axis=1)


# Histograms 
fig = plt.figure(figsize=(9,5))
ax = plt.subplot(1,1,1)

sns.histplot(data=mse_normal, stat='density', color="skyblue", ax=ax, label="Normal", kde=True)
sns.histplot(data=mse_outliers, stat='density', color="purple", ax=ax, label="Outliers", kde=True)
sns.histplot(data=mse_random, stat='density', color="teal", ax=ax, label="Random", kde=True)

ax.set_xlabel('Reconstruction Error')
plt.legend()
plt.show()