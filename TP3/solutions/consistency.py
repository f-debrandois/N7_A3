plt.subplot(1,2,1)
plt.boxplot(VALIDATION_ACCURACY)
plt.title('Validation accuracy')

plt.subplot(1,2,2)
plt.boxplot(VALIDATION_LOSS)
plt.title('Validation loss')

plt.tight_layout()
plt.show()