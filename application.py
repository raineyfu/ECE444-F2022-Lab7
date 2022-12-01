from flask import Flask, request, jsonify
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import os 
import pickle 

app = Flask(__name__)


loaded_model = None
with open('basic_classifier.pkl', 'rb') as fid:
    loaded_model = pickle.load(fid)

vectorizer = None
with open('count_vectorizer.pkl', 'rb') as vd:
    vectorizer = pickle.load(vd)


@app.route("/")
def hello():
    return "Hello World!"

@app.route("/predict", methods=['POST'])
def predict():

    data = None

    data = request.json["text"]

    print(data)
    prediction = loaded_model.predict(vectorizer.transform([data]))[0]
    print(prediction)
    
    if (prediction == "FAKE"):
        return "1"
    else:
        return "0"
    return prediction



if __name__ == "__main__":
    app.run()