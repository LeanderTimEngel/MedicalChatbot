import re
from symspellpy import SymSpell, Verbosity
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

sym_spell = SymSpell()
sym_spell.load_dictionary("en.txt", 0, 1)

lemmatizer = WordNetLemmatizer()

#Argument muss als Array geliefert werden bspw.: preprocess_text(["text"])
def preprocess_text(text):
    text = [t.lower() for t in text]

    text = [re.sub(r'https?://\S+|www\.\S+', '', t) for t in text]

    text = [re.sub(r'[^a-zA-Z0-9]', ' ', t) for t in text]

    stop_words = set(stopwords.words('english'))
    text = [' '.join([word for word in t.split() if word not in stop_words]) for t in text]

    text = [' '.join([lemmatizer.lemmatize(word) for word in t.split()]) for t in text]

    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"
                               u"\U0001F300-\U0001F5FF"
                               u"\U0001F680-\U0001F6FF"
                               u"\U0001F1E0-\U0001F1FF"
                               u"\U00002702-\U000027B0"
                               u"\U000024C2-\U0001F251"
                               "]+", flags=re.UNICODE)
    text = [re.sub(emoji_pattern, '', t) for t in text]

    corrected_text = []
    for t in text:
        corrected_words = []
        for word in t.split():
            suggestions = sym_spell.lookup(word, Verbosity.CLOSEST, max_edit_distance=2)
            if suggestions:
                corrected_word = suggestions[0].term
                corrected_words.append(corrected_word)
            else:
                corrected_words.append(word)
        corrected_text.append(' '.join(corrected_words))

    return corrected_text
