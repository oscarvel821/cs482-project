import streamlit as st
import pandas as pd
from transformers import pipeline
from transformers import AutoTokenizer ,DistilBertTokenizerFast, AutoModelForSequenceClassification

@st.experimental_memo
def classifier1_data(_classifier, comments):
  test_comments_prob = _classifier(comments)

  sorted_test_comments_prob = []

  highest = []
  highest_prob = []
  second_highest = []
  second_highest_prob = []

  for inner_list in test_comments_prob:
      sorted_inner_list = sorted(inner_list, key=lambda x: x['score'], reverse=True)
      highest.append(sorted_inner_list[0]['label'])
      highest_prob.append(sorted_inner_list[0]['score'])
      second_highest.append(sorted_inner_list[1]['label'])
      second_highest_prob.append(sorted_inner_list[1]['score'])
      sorted_test_comments_prob.append(sorted_inner_list)

  return pd.DataFrame(
        {
            "text_comment": test_comments,
            "class 1": highest,
            "prob 1": highest_prob,
            "class 2" : second_highest,
            "prob 2" : second_highest_prob
        }
    )

@st.experimental_memo
def classifier2_data(_classifier, comments):
  test_comments_prob = _classifier(comments)

  sorted_test_comments_prob = []

  highest = []
  highest_prob = []
  second_highest = []
  second_highest_prob = []

  for inner_list in test_comments_prob:
      sorted_inner_list = sorted(inner_list, key=lambda x: x['score'], reverse=True)
      highest.append(sorted_inner_list[0]['label'])
      highest_prob.append(sorted_inner_list[0]['score'])
      second_highest.append(sorted_inner_list[1]['label'])
      second_highest_prob.append(sorted_inner_list[1]['score'])
      sorted_test_comments_prob.append(sorted_inner_list)

  return pd.DataFrame(
        {
            "text_comment": test_comments,
            "class one": highest,
            "prob 1": highest_prob,
            "class 2" : second_highest,
            "prob 2" : second_highest_prob
        }
    )


# st.set_page_config(layout="wide")

st.title("Toxic Comment Classifier App")

st.markdown("Welcome to my toxic classifier app! With this app, you can easily check whether a piece of text contains toxic language or not. \
            Whether you're a parent concerned about what your child is exposed to online, or a business owner looking to maintain a safe and respectful workplace,\
             my app can help you quickly identify potentially harmful language. Simply enter the text you want to analyze, and my algorithm will provide you with a toxicity score.\
             I hope my app can help make the internet a safer and more welcoming place for everyone. Let's get started!")

st.markdown("The Finetuned Bert consist of six classes with following labels: ")

LABEL_COLUMNS = ['toxic', 'severe_toxic', 'obscene', 'threat', 'insult', 'identity_hate']

for label in LABEL_COLUMNS:
   st.markdown("* " + label)

st.markdown("For example, the 'threat' label is used to identify text that contains threats of harm or violence, while the label 'toxic' us used to identify text that contains offensive or disrespectful language")
st.markdown("While the Toxic Comment Classifier App mainly focuses on the Finetuned Bert model with the 6 classes above\
            , there is an option where you can use the pretrained model 'distilbert-base-uncased-finetuned-sst-2-english' \
            which contains the following two classes: ")

for label in ['Postive', 'Negative']:
   st.markdown('* ' + label)

df = pd.read_csv(r'data/test_examples.csv')

test_comments = df['comment_text'].values.tolist()

index = 0

classifier1 = pipeline('sentiment-analysis', model='oscarvel821/my_model_3', return_all_scores=True)

model = AutoModelForSequenceClassification.from_pretrained('distilbert-base-uncased-finetuned-sst-2-english')
tokenizer = DistilBertTokenizerFast.from_pretrained('distilbert-base-uncased-finetuned-sst-2-english')

classifier2 = pipeline('sentiment-analysis', model=model, tokenizer=tokenizer, return_all_scores=True)

classifiers = [classifier1, classifier2]

col1, col2 = st.columns(2)
with col1:
  option = st.selectbox('Select a model', ('Finetuned bert', 'Distilbert base uncased') )

  st.write("You selected:", option)

  if option == 'Finetuned bert':
    index = 0
  elif option == 'Distilbert base uncased':
    index = 1

with col2:
  text = st.text_area("enter some text")

  if text:
    out = classifiers[index](text)
    for dic in out[0]:
       st.markdown(dic['label'] + " " + str(round(dic['score'], 3)))


data1 = classifier1_data(classifiers[0], test_comments)
data2 = classifier2_data(classifiers[1], test_comments)

st.markdown("Below are some examples of random tweets generated over time, the table shows the text and the two most likely classes with their probability")

with st.container():
  if index == 0:
     st.dataframe(data1, use_container_width=True)
  elif index == 1:
     st.dataframe(data2, use_container_width=True)
