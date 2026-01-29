import pandas as pd
import streamlit as st
import nltk
import re

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error, r2_score

def load_nltk_resources():
    try:
        nltk.data.find('tokenizers/punkt_tab')
    except LookupError:
        nltk.download('punkt')
        nltk.download('punkt_tab')

load_nltk_resources()

st.set_page_config(page_title="AI Summarizer", layout="wide")
st.title("Text Summarization Tool (ML Based)")

@st.cache_resource
def prepare_model(csv_path):
    df = pd.read_csv(csv_path)
    df['sentence'] = df['sentence'].fillna('')
    df = df.dropna(subset=['score'])

    X = df['sentence']
    y = df['score']

    vectorizer = TfidfVectorizer()
    X_vec = vectorizer.fit_transform(X)

    model = SVR(kernel='rbf')
    model.fit(X_vec, y)
    
    return vectorizer, model, df

file_path = r"E:\Machine Learning\Project\yellow.csv"
vectorizer, model, df = prepare_model(file_path)

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("Input Section")
    user_text = st.text_area("Enter your long document here:", height=300)
    summarize_button = st.button("Generate Summary")

with col2:
    st.subheader("Model Performance Metrics")
    X_test_vec = vectorizer.transform(df['sentence'])
    predictions = model.predict(X_test_vec)
    
    st.write(f"R2 Score: {r2_score(df['score'], predictions):.4f}")
    st.write(f"Dataset Size: {len(df)} sentences")

if summarize_button:
    if not user_text.strip():
        st.warning("Please enter some text to summarize.")
    else:
        sentences = nltk.sent_tokenize(user_text)
        clean_sent = [re.sub(r'\W+', ' ', s) for s in sentences]

        sent_vec = vectorizer.transform(clean_sent)
        scores = model.predict(sent_vec)

        ranked = sorted(zip(scores, sentences), reverse=True)

        st.subheader("Generated Summary")
        
        num_sentences = min(3, len(sentences))
        summary = [s for _, s in ranked[:num_sentences]]

        for s in summary:
            st.write(s)