
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Sentiment Analysis", page_icon="😊")

st.title("AI-Powered Sentiment Analysis")
st.write("Analyze reviews as Positive, Negative, or Neutral.")

# Sample dataset
data = {
    "Review": [
        "This product is excellent",
        "I love this service",
        "Amazing quality",
        "Very happy with the product",
        "Wonderful experience",
        "This product is bad",
        "Very poor service",
        "I hate this product",
        "Worst experience ever",
        "I am disappointed",
        "The product is okay",
        "Average service",
        "Nothing special",
        "It is normal",
        "The service is acceptable"
    ],
    "Sentiment": [
        "Positive", "Positive", "Positive", "Positive", "Positive",
        "Negative", "Negative", "Negative", "Negative", "Negative",
        "Neutral", "Neutral", "Neutral", "Neutral", "Neutral"
    ]
}

df = pd.DataFrame(data)

st.subheader("Sample Reviews")
st.dataframe(df, use_container_width=True)

st.subheader("Sentiment Distribution")
st.bar_chart(df["Sentiment"].value_counts())

col1, col2, col3 = st.columns(3)
col1.metric("Positive", 5)
col2.metric("Negative", 5)
col3.metric("Neutral", 5)

st.subheader("Analyze New Reviews")

review1 = st.text_input("Enter Review 1")
review2 = st.text_input("Enter Review 2")
review3 = st.text_input("Enter Review 3")

positive_words = [
    "good", "great", "excellent", "love", "amazing",
    "happy", "wonderful", "best", "awesome", "nice"
]

negative_words = [
    "bad", "poor", "hate", "worst", "terrible",
    "disappointed", "awful", "angry", "boring"
]

def analyze_sentiment(text):
    words = text.lower().split()
    pos = sum(w.strip(".,!?") in positive_words for w in words)
    neg = sum(w.strip(".,!?") in negative_words for w in words)

    if pos > neg:
        return "Positive"
    elif neg > pos:
        return "Negative"
    return "Neutral"

if st.button("Analyze Sentiment"):
    reviews = [review1, review2, review3]
    reviews = [r for r in reviews if r.strip()]

    if not reviews:
        st.warning("Please enter at least one review.")
    else:
        results = [
            {"Review": r, "Sentiment": analyze_sentiment(r)}
            for r in reviews
        ]
        st.subheader("Prediction Results")
        st.dataframe(pd.DataFrame(results), use_container_width=True)
