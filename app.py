import streamlit as st
from transformers import pipeline

# x = st.slider('Select a value')
# st.write(x, 'squared is', x * x)

model_name = "distilbert-base-uncased-finetuned-sst-2-english"

classifier = pipeline("sentiment-analysis", model=model_name)
result = classifier(["We are very happy to show you the transformers library.", "We hope you dont hate it"])

for result in results:
  print(result)
