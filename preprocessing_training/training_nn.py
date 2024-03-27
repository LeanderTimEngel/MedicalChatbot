from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Embedding, LSTM
import numpy as np
from sklearn import metrics


def one_hot(y):
    num_classes = len(y.unique())
    y_encoded = np.eye(num_classes)[y]
    return y_encoded, num_classes


def keras_nn(x_train, x_test, y_train, y_test, num_classes):
    # Tokenize the symptoms and convert them into sequences
    max_words = 10000
    tokenizer = Tokenizer(num_words=max_words)
    tokenizer.fit_on_texts(x_train)
    x_train_sequences = tokenizer.texts_to_sequences(x_train)
    x_test_sequences = tokenizer.texts_to_sequences(x_test)

    # Pad the sequences to ensure that they are all the same length
    max_len = 200
    x_train_padded = pad_sequences(x_train_sequences, maxlen=max_len)
    x_test_padded = pad_sequences(x_test_sequences, maxlen=max_len)

    # Build the neural network model
    embedding_size = 128
    model = Sequential()
    model.add(Embedding(max_words, embedding_size, input_length=max_len))
    model.add(LSTM(128, dropout=0.2, recurrent_dropout=0.2,
                   return_sequences=True))  # bei mehreren Layers noch zusätzlich return_sequences=True eintragen
    model.add(LSTM(64, dropout=0.2, recurrent_dropout=0.2))
    model.add(Dense(num_classes, activation='softmax'))

    # Compile the model
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

    # Train the model
    batch_size = 64
    epochs = 15
    model.fit(x_train_padded, y_train, batch_size=batch_size, epochs=epochs, validation_data=(x_test_padded, y_test))

    predictions = model.predict(x_test_padded)

    predicted_labels = np.argmax(predictions, axis=1)
    y_true = np.argmax(y_test, axis=1)
    print(metrics.classification_report(y_true, predicted_labels))
    return predicted_labels, model

