if not os.path.exists(path + "cv"):
    os.mkdir(path + "cv")
    
    
categories = []

#Images d'entrainement
path_train = path + "train/train/"
train_filenames = os.listdir(path + "train/train")
for filename in train_filenames:
    shutil.copyfile(path_train+filename, path+"cv/"+filename)
    category = filename.split('.')[0]
    if category == 'dog':
        categories.append(1)
    else:
        categories.append(0)

#Images de validation
path_validation = path + "validation/"
validation_filenames = os.listdir(path + "validation")
for filename in validation_filenames:
    shutil.copyfile(path_validation+filename, path+"cv/"+filename)
    category = filename.split('.')[0]
    if category == 'dog':
        categories.append(1)
    else:
        categories.append(0)
            

cv_df = pd.DataFrame({
    'filename': train_filenames+validation_filenames,
    'category': categories
})
cv_df['category'] = cv_df['category'].astype(str)
cv_df.head()