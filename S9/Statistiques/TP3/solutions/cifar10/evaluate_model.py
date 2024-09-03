def evaluate_model(dataset, model):
 
    class_names =['Airplane', 'Automobile', 'Bird', 'Cat', 'Deer', 'Dog', 'Frog', 'Horse', 'Ship', 'Truck']
    n_rows = 3
    n_cols = 6
     
    # Retrieve a number of images from the dataset.
    data_batch = dataset[0:n_rows*n_cols]
 
    # Get predictions from model.  
    predictions = model.predict(data_batch)
 
    plt.figure(figsize=(20, 8))
    n_matches = 0
         
    for idx in range(n_rows*n_cols):
        ax = plt.subplot(n_rows, n_cols, idx+1)
        plt.axis("off")
        plt.imshow(data_batch[idx])
 
        pred_idx = tf.argmax(predictions[idx]).numpy()
        truth_idx = np.nonzero(y_test[idx])
             
        title = str(class_names[truth_idx[0][0]]) + " | " + str(class_names[pred_idx])
        title_obj = plt.title(title, fontdict={'fontsize':13})
             
        if pred_idx == truth_idx:
            n_matches += 1
            plt.setp(title_obj, color='g')
        else:
            plt.setp(title_obj, color='r')
                 
        acc = n_matches/(idx+1)
    print("Prediction accuracy: ", int(100*acc)/100)
     
    return