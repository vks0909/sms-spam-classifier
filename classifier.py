import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Sklearn imports
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

# NLP imports
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import string

# NLTK downloads usually required once
# nltk.download('stopwords')

def load_data(filepath):
    """
    Load the dataset. You can use the standard UCI SMS Spam Collection dataset.
    Wait for the dataset to download. Format is typically tab-separated or CSV.
    """
    # df = pd.read_csv(filepath, sep='\t', names=["label", "message"])
    # return df
    pass

def preprocess_text(text):
    """
    Basic NLP Preprocessing Pipeline:
    1. Remove punctuation
    2. Convert to lowercase
    3. Remove stopwords (common words like 'the', 'is', 'a')
    4. Apply Stemming (reducing words to their root, e.g., 'running' -> 'run')
    """
    # ps = PorterStemmer()
    # nopunc = ''.join([char for char in text if char not in string.punctuation])
    # clean_words = [ps.stem(word.lower()) for word in nopunc.split() if word.lower() not in stopwords.words('english')]
    # return ' '.join(clean_words)
    pass

def train_model(X_train, y_train):
    """
    Train a classification model. Try comparing Naive Bayes and SVM!
    """
    # Option A: Naive Bayes (Fast and effective for text)
    # model = MultinomialNB()
    
    # Option B: SVM with L2 Regularization parameter 'C'
    # model = SVC(C=1.0, kernel='linear')
    
    # model.fit(X_train, y_train)
    # return model
    pass

def evaluate_model(model, X_test, y_test):
    """
    Evaluate your model's performance correctly on an imbalanced dataset.
    """
    # predictions = model.predict(X_test)
    # print("Confusion Matrix:\n", confusion_matrix(y_test, predictions))
    # print("\nClassification Report:\n", classification_report(y_test, predictions))
    # print("\nAccuracy:", accuracy_score(y_test, predictions))
    pass

if __name__ == "__main__":
    print("Welcome to your SMS Spam Classifier Project!")
    print("Uncomment the code in the functions above to start building your model step-by-step.")
    
    # Step 1: Download the dataset and load it
    # df = load_data('spam.csv')
    
    # Step 2: Clean the text messages
    # df['cleaned_message'] = df['message'].apply(preprocess_text)
    
    # Step 3: Feature Extraction (Convert Text to Numbers using TF-IDF)
    # tfidf = TfidfVectorizer()
    # X = tfidf.fit_transform(df['cleaned_message']).toarray()
    
    # Convert labels ('spam' or 'ham') to 1s and 0s
    # y = df['label'].map({'ham': 0, 'spam': 1})
    
    # Step 4: Split data into Training and Testing sets
    # X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Step 5: Train Model
    # model = train_model(X_train, y_train)
    
    # Step 6: Evaluate Model
    # evaluate_model(model, X_test, y_test)
