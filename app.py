import streamlit as st
import pandas as pd
from transformers import pipeline
from transformers import AutoTokenizer ,DistilBertTokenizerFast, AutoModelForSequenceClassification

# model_name = "distilbert-base-uncased-finetuned-sst-2-english"

# model = AutoModelForSequenceClassification.from_pretrained(model_name)
# tokenizer = AutoTokenizer.from_pretrained(model_name)

# classifier = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)
# results = classifier(["We are very happy to show you the transformers library.", "We hope you dont hate it"])

# for result in results:
#   print(result)
  
# text = st.text_area("enter some text")

# if text:
#   out = classifier(text)
#   st.json(out)

# model_name = 'C:\Users\Oscar\Desktop\CS482-project\my_model'

# classifier = pipeline("sentiment-analysis", model=model_name)

model_name = 'distilbert-base-uncased'
tokenizer = DistilBertTokenizerFast.from_pretrained(model_name)

classifier = pipeline('sentiment-analysis', model=r'my_model', tokenizer=tokenizer, return_all_scores=True)

# results = classifier(["Go to hell, I hope you die!.", "We hope you dont hate it"])

# for result in results:
#   print(result)

text = st.text_area("enter some text")

if text:
  out = classifier(text)
  toxic = 'Toxic '
  severe_toxic = 'Severe Toxic '
  obscene = 'Obscene '
  threat = 'Threat '
  insult = 'Insult '
  identity_hate = 'Identity_hate '
  for d in out:
    print("dict",d[0])
    print(d[0]['score'])
    toxic += str(d[0]['score'])
    severe_toxic += str(d[1]['score'])
    obscene += str(d[2]['score'])
    threat += str(d[3]['score'])
    insult += str(d[4]['score'])
    identity_hate += str(d[5]['score'])

  # st.json(out)
  st.markdown(toxic)
  st.markdown(severe_toxic)
  st.markdown(obscene)
  st.markdown(threat)
  st.markdown(insult)
  st.markdown(identity_hate)

# df = pd.read_csv(r'jigsaw-toxic-comment-classification-challenge\test.csv\test.csv')

# comments = df['comment_text'].values.tolist()

# comments = [element for element in comments if len(str(element)) < 512]

# comments = comments[:200]

# test_results = classifier(comments)

# print(test_results[0][0])

# toxic
# severe_toxic
# obscene
# threat
# insult
# identity_hate

# toxic, severe_toxic, obscene, threat, insult, identity_hate = [],[],[],[],[],[]

# for result in test_results:
#   result[0]
