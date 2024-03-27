import pickle
import preprocessing as pp
import numpy as np

'''Wichtig: Bevor dieses Skript ausgeführt werden kann, muss sichergestellt werden, dass beim Preprocessing der 
Trainingsdaten der Vectorizer gespeichert wurde. Die Prediction funktioniert nur, wenn derselbe Vectorizer wie beim 
Training genutzt wird. Also unbedingt beim Training auf das setzen von save_vectorizer=True achten!'''

x = ["I've been noticing a bulge or lump in my lower abdomen or groin area. It becomes more prominent when I cough or lift heavy objects. I also experience occasional discomfort or aching sensation around the bulge. I've scheduled an appointment with my doctor to discuss this condition further.",
     "Experiencing shortness of breath, persistent cough, and frequent respiratory infections. Seeking medical advice for further evaluation and management of symptoms",
     "Experiencing excruciating headaches on one side of the head, often accompanied by eye redness, tearing, and nasal congestion. These headaches occur in clusters and can last for weeks or months before going into remission.",
     "Noticing painful and recurring boils or abscesses in the armpits, groin, or buttocks area. These lumps are accompanied by inflammation, tenderness, and can sometimes discharge pus. Seeking medical assistance to manage this chronic skin condition.",
     "Experiencing frequent heartburn and regurgitation of stomach acid into the throat. Symptoms worsen after meals or when lying down. Seeking lifestyle modifications and medications to alleviate the discomfort.",
     "Dealing with chronic widespread pain, fatigue, and heightened sensitivity to touch. Also experiencing sleep disturbances, cognitive difficulties (fibro fog), and mood swings. Seeking medical support to manage symptoms and improve daily functioning.",
     "Having a persistent issue with bad breath, despite maintaining proper oral hygiene practices. The unpleasant odor is noticeable to others and is causing social discomfort. Seeking dental advice to identify the underlying cause and explore treatment options to improve breath freshness."]

print("Test data: ", x)

print("Vectorizing... ")
x_pp = pp.pipeline_testing(x)
print("Vectorized data")

print("Loading model...")
with open('pickles/linearsvc.pkl', 'rb') as f:
    model = pickle.load(f)
print("Loaded model")

print("Making prediction...")
y_predicted = model.predict(x_pp)
print("Prediction finshed: ")

print(y_predicted)

for i in range(len(y_predicted)):
    decision_scores = model.decision_function(x_pp)[i]
    top_indices = np.argsort(decision_scores)[-3:]
    best_score = model.classes_[top_indices[2]]
    second_best = model.classes_[top_indices[1]]
    third_best = model.classes_[top_indices[0]]
    print("Symptoms: ", x[i])
    print("Best score: ", best_score)
    print("Second best: ", second_best)
    print("Third best: ", third_best)

print("Saving prediction...")
with open('pickles/prediction.pkl', 'wb') as f:
    pickle.dump(y_predicted, f)
print("Saved prediction to prediction.pkl")
