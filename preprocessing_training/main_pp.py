import preprocessing as pp
import pandas as pd
import pickle

'''Preprocessing-Main: Lädt die Trainingsdaten aus csv-Datei, bereinigt, vektorisiert und speichert die Daten als X 
und y in einer pickle-Datei ab. Reihenfolge der Skripte: main_pp -> main_ml -> main_predict Wenn sampling=True 
gesetzt ist, wird der Datensatz durch Undersampling balanciert. n ist dabei die Anzahl der Samples pro Label, 
auf die gesampelt werden soll. Wenn die gesamte Abfolge an Skripten ausgeführt werden soll, muss save_vectorizer auf 
True gesetzt sein. '''

# CSV laden
print("Loading csv...")
data = pd.read_csv("cleaned_data_final.csv", low_memory=False)
data.drop(columns=data.columns[0], axis=1, inplace=True)
print("Loaded csv into pandas dataframe with shape: ", data.shape)

# Preprocessing
print("Processing data...")
X, y = pp.pipeline_training(data, sampling=True, n=451, save_vectorizer=True)
print("Processed data with new shape: (", len(y), ", 2)")

# Speichern
print("Saving data...")
with open('pickles/data_pp.pkl', 'wb') as f:
    pickle.dump((X, y), f)

print("Data saved as: data_pp.pkl")
