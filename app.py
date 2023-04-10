import streamlit as st
from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForSequenceClassification

# x = st.slider('Select a value')
# st.write(x, 'squared is', x * x)

model_name = "distilbert-base-uncased-finetuned-sst-2-english"

model = AutoModelForSequenceClassification.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

classifier = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)
results = classifier(["We are very happy to show you the transformers library.", "We hope you dont hate it"])

for result in results:
  print(result)
  
text = st.text_area("enter some text")

if text:
  out = classifier(text)
  st.json(out)
  
# tokens = tokenizer.tokenize("We are very happy to show you the transformers library.")
# token_ids = tokenizer.convert_token_to_ids(tokens)
# input_ids = tokenizer("We are very happy to show you the transformers library.")

# print(f'  tokens:{tokens}')
