plt.figure(figsize=(18, 9))
 
n_rows = 4
n_cols = 8
 
# plot each of the images in the batch and the associated ground truth labels
for i in range(n_rows*n_cols):
    ax = plt.subplot(n_rows, n_cols, i + 1)
    plt.imshow(X_train[i,:,:])
    title = '['+y_train[i][0].astype('str')+'] '+class_names[y_train[i][0]]
    plt.title(title)
    plt.axis("off")
    
#plt.tight_layout()
plt.show()