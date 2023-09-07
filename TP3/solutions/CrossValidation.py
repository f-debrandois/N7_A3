tf.keras.backend.clear_session()

VALIDATION_ACCURACY = []
VALIDATION_LOSS = []

n_folds = 3
kf = KFold(n_splits=n_folds, shuffle=True)
  # A COMPLETER

save_dir = './saved_models/'

for fold_no, (train_index, validation_index) in enumerate(kf.split(np.zeros(len(categories)), categories)):
    train_df = cv_df.iloc[train_index]
    validation_df = cv_df.iloc[validation_index]
    
    train_generator = train_datagen_augmented.flow_from_dataframe(
        train_df, 
        path + 'cv/', 
        x_col = 'filename', 
        y_col = 'category',
        target_size = (image_size,image_size),
        class_mode = 'binary',
        batch_size = batch_size)
    
    validation_generator = train_datagen_augmented.flow_from_dataframe(
        validation_df, 
        path + 'cv/', 
        x_col = 'filename', 
        y_col = 'category',
        target_size = (image_size,image_size),
        class_mode = 'binary',
        batch_size = batch_size)

    # CREATE NEW MODEL
    model = create_new_model()
    
    # COMPILE NEW MODEL
    model.compile(
        loss = 'binary_crossentropy',
        optimizer = optimizers.Adam(learning_rate=3e-4),
        metrics = ['accuracy'])
    
    # Generate a print
    print('------------------------------------------------------------------------')
    print(f'## Training for fold {fold_no+1}/{n_folds} ##')

    # CREATE CALLBACKS
    checkpoint = tf.keras.callbacks.ModelCheckpoint(
        save_dir+get_model_name(fold_no), 
        monitor = 'val_accuracy', 
        verbose = 1, 
        save_best_only = True, 
        mode = 'max')
    callbacks_list = [checkpoint]
    
    # FIT THE MODEL
    history = model.fit(
        train_generator,
        epochs = 2,
        callbacks = callbacks_list,
        validation_data = validation_generator)
    # Model weights are saved at the end of every epoch, if it's the best seen so far.

    # PLOT HISTORY
    plot_training_analysis()
    
    # LOAD BEST MODEL to evaluate the performance of the model
    model.load_weights(save_dir+"model_"+str(fold_no)+".h5")

    results = model.evaluate(validation_generator)
    results = dict(zip(model.metrics_names,results))

    VALIDATION_ACCURACY.append(results['accuracy'])
    VALIDATION_LOSS.append(results['loss'])

    tf.keras.backend.clear_session()