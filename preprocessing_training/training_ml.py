from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics
import pickle


# Aufsplitten in Test- und Trainingsdaten
def split(x, y):
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=123)
    return x_train, x_test, y_train, y_test


# util-Methode fürs Training
def train_and_test_classifier(classifier, x_train, x_test, y_train, y_test, save_model=False):
    print(f"{classifier.__class__.__name__}:")

    print("Training...")
    classifier.fit(x_train, y_train)
    print("Training finished")

    print("Testing...")
    predicted = classifier.predict(x_test)
    print("Finished Testing:")
    print(metrics.classification_report(y_test, predicted))

    if save_model:
        print(f"Saving model as {classifier.__class__.__name__.lower()}.pkl...")
        with open(f"pickles/{classifier.__class__.__name__.lower()}.pkl", 'wb') as f:
            pickle.dump(classifier, f)
        print(f"Saved as {classifier.__class__.__name__.lower()}.pkl")

    return classifier, predicted


# SVM
def support_vector_machine(x_train, x_test, y_train, y_test, save_model: bool):
    svm = LinearSVC()
    svm, predicted = train_and_test_classifier(svm, x_train, x_test, y_train, y_test, save_model)
    return svm, predicted


# Gradient Boost
def gradient_boost(x_train, x_test, y_train, y_test, save_model: bool):
    gb = GradientBoostingClassifier()
    gb, predicted = train_and_test_classifier(gb, x_train, x_test, y_train, y_test, save_model)
    return gb, predicted


# K-nearest-neighbor
def k_nearest_neighbor(x_train, x_test, y_train, y_test, save_model: bool):
    knn = KNeighborsClassifier()
    knn, predicted = train_and_test_classifier(knn, x_train, x_test, y_train, y_test, save_model)
    return knn, predicted


# Naive Bayes
def naive_bayes(x_train, x_test, y_train, y_test, save_model: bool):
    nb = MultinomialNB()
    nb, predicted = train_and_test_classifier(nb, x_train, x_test, y_train, y_test, save_model)
    return nb, predicted


# Decision Tree
def decision_tree(x_train, x_test, y_train, y_test, save_model: bool):
    d_tree = DecisionTreeClassifier()
    d_tree, predicted = train_and_test_classifier(d_tree, x_train, x_test, y_train, y_test, save_model)
    return d_tree, predicted
