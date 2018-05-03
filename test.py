import csv
import string
from sklearn.cross_validation import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk import word_tokenize


all_training = []
all_labels = []

with open('cases.csv', 'r') as f:
    reader = csv.DictReader(f)
    cases = [row for row in reader]
    f.close()

for case in cases:
    all_training.append(case["text"])
    all_labels.append(case["label"])

def train(classifier, X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=33)
    classifier.fit(X_train, y_train)
    print ("Accuracy: %s" % classifier.score(X_test, y_test))
    return classifier

def stemming_tokenizer(text):
    stemmer = PorterStemmer()
    return [stemmer.stem(w) for w in word_tokenize(text)]

trial1 = Pipeline([
    ('vectorizer', TfidfVectorizer(stop_words=stopwords.words('english') + list(string.punctuation))),
    ('classifier', MultinomialNB(alpha=0.5)),
])

clf = train(trial1, all_training, all_labels)

all_testing = []
with open('predictions.csv', 'r') as f:
    reader = csv.DictReader(f)
    predictions = [row for row in reader]
    f.close()

for prediction in predictions:
    all_testing.append(prediction["text"])

answers = clf.predict(all_testing)
# print(answers)
