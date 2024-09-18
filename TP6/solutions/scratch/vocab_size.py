vocab = list(set([w for text in train_data.keys() for w in text.split(' ')]))
vocab_size = len(vocab)

print('Vocabulary:',vocab)
print('--> %d unique words' % vocab_size)