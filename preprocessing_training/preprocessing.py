import re
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle
from sklearn.preprocessing import LabelEncoder
from imblearn.under_sampling import NearMiss
import pandas as pd


# Labels mit weniger als 10 Einträgen entfernen
def remove_small_labels(data):
    label_counts = data["label"].value_counts()
    labels_with_more_than_10 = label_counts[label_counts >= 20].index
    df_with_more_than_10 = data[data["label"].isin(labels_with_more_than_10)].copy()
    df_with_more_than_10 = df_with_more_than_10.reset_index(drop=True)
    removed_labels = label_counts[label_counts < 20].index.tolist()

    return df_with_more_than_10


# Tags mit eckigen Klammern entfernen
def remove_tags(x):
    pattern_imported_message = r"\[i:.*?\](.*?)\[/i:.*?\]"
    pattern_tags = r"\[.*?\]"

    x = x.apply(lambda l: re.sub(pattern_imported_message, '', l))
    x = x.apply(lambda l: re.sub(pattern_tags, '', l))
    return x


# Hilfsmethode URLs
def remove_urls_util(text):
    url_pattern = re.compile(r'http[s]?://\S+|www\.\S+')
    return url_pattern.sub('', text)


# URLs entfernen
def remove_urls(x):
    x = x.apply(remove_urls_util)
    return x


# Bereinigung
def clean(x):
    x = remove_tags(x)
    x = remove_urls(x)
    return x


# Vektorisieren
def vectorize(x, save_vectorizer=False, load_vectorizer=False):
    if load_vectorizer:
        with open('pickles/vectorizer.pkl', 'rb') as f:
            tfidf = pickle.load(f)
        x_vec = tfidf.transform(x)
        return x_vec
    else:
        tfidf = TfidfVectorizer()
        x_vec = tfidf.fit_transform(x)

    if save_vectorizer:
        with open('pickles/vectorizer.pkl', 'wb') as f:
            pickle.dump(tfidf, f)
    return x_vec


# Labels kodieren
def encode(y):
    label_encoder = LabelEncoder()
    y_encoded = label_encoder.fit_transform(y)
    with open('pickles/label_encoder.pkl', 'wb') as f:
        pickle.dump(label_encoder, f)
    return y_encoded


# Labels dekodieren
def decode(y):
    with open('pickles/label_encoder.pkl', 'rb') as file:
        label_encoder = pickle.load(file)
    y_decoded = label_encoder.inverse_transform(y)
    return y_decoded


# Aus Datensatz Labels entfernen, die Bedingung nicht erfüllen
def split_n(data, n):
    label_counts = data["label"].value_counts()
    labels_with_more_than_n = label_counts[label_counts >= n].index
    df_with_more_than_n = data[data["label"].isin(labels_with_more_than_n)].copy()
    df_with_more_than_n.reset_index(inplace=True, drop=True)
    return df_with_more_than_n


# Under-sampling
def undersample(x, y):
    nm = NearMiss(version=1, n_neighbors=3)
    x_res, y_res = nm.fit_resample(x, y)
    return x_res, y_res


# Gesamte Pipeline fürs Training
def pipeline_training(data: pd.DataFrame, n: int, sampling=False, save_vectorizer=False, load_vectorizer=False):
    data = remove_small_labels(data)

    if sampling:
        sample_df = split_n(data, n)
        x = sample_df["text"]
        y = sample_df["label"]
        x_res, y_res = undersample(vectorize(clean(x), save_vectorizer=save_vectorizer, load_vectorizer=load_vectorizer), encode(y))
        return x_res, decode(y_res)

    x = data["text"]
    y = data["label"]

    return vectorize(clean(x), save_vectorizer=save_vectorizer, load_vectorizer=load_vectorizer), y


# Gesamte Pipeline fürs Testen
def pipeline_testing(x):
    x_vec = vectorize(x, load_vectorizer=True)
    return x_vec
