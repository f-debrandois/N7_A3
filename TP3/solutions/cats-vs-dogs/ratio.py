total_train = train_df.shape[0]
total_validate = validation_df.shape[0]
total_test = test_df.shape[0]

ratio_train = np.sum(train_categories)/total_train
ratio_validate = np.sum(validation_categories)/total_validate
ratio_test = np.sum(test_categories)/total_test

print("Ratio chien/chat - Train :", ratio_train)
print("Ratio chien/chat - Validation :", ratio_validate)
print("Ratio chien/chat - Test :", ratio_test)