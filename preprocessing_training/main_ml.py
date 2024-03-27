import training_ml as ml
import pickle

'''Training-Main: Lädt die vorbereiteten Daten, splittet in Trainings- und Testdaten und trainiert das model. 
Wichtig: Wenn danach die Prediction-Main ausgeführt werden soll, muss save_model auf True gesetzt und der Vectorizer 
im Preprocessing gespeichert worden sein!'''

with open('pickles/data_pp.pkl', 'rb') as file:
    X, y = pickle.load(file)

X_train, X_test, y_train, y_test = ml.split(X, y)

svm, predicted_svm = ml.support_vector_machine(X_train, X_test, y_train, y_test, save_model=True)
# gd, predicted_gb = ml.gradient_boost(X_train, X_test, y_train, y_test, save_model=True)
# knn, predicted_knn = ml.k_nearest_neighbor(X_train, X_test, y_train, y_test, save_model=True)
# nb, predicted_nb = ml.naive_bayes(X_train, X_test, y_train, y_test, save_model=True)
# dt, predicted_dt = ml.decision_tree(X_train, X_test, y_train, y_test, save_model=True)
