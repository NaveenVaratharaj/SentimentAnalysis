#importing required packages
#Stremlit
#Nltk
#vader
#vader is a sentiment analysis tool that is specifically attuned to sentiments expressed in social media

import streamlit as st
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

#Title and the text in the UI
st.title("SENTIMENT ANALYSIS")

#Code to get input from the user
user_input = st.text_input("Provide a FeedBack:")

#Vader lexicon is used to text for sentiment analysis
nltk.download("vader Lexicon")
s = SentimentIntensityAnalyzer()

#Return a float for sentiment strength based on the input text.
score = s.polarity_scores(user_input)


#Analyzing the statements
if score == 0:
    st.header("Please type a valid statement")
elif score["neg"] == 1:
    st.header("The Statement you entered is Negative statement")
elif score["pos"] != 0:
    st.header("The Statement you entered is Positive statement")
else:
    st.header("The Statement you entered is Neutral statement")

st.write("Thank you for visiting!")
