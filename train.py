# from pathlib import Path
# import numpy as np
# from sklearn.model_selection import train_test_split
# import torch
# from transformers import DistilBertTokenizerFast, DistilBertForSequenceClassification
# from transformers import Trainer, TrainingArguments
# import pandas as pd
# from toxic_comment_dataset import Toxic_Comment_Dataset

# device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')

# model_name = 'distilbert-base-uncased'

# df = pd.read_csv(r'jigsaw-toxic-comment-classification-challenge\train.csv\train.csv')
# df = df[:9000]
# train_df, val_df = train_test_split(df, test_size=0.10)

# print(train_df.shape, val_df.shape)
# # print(type(train_df))

# LABEL_COLUMNS = ['toxic', 'severe_toxic', 'obscene', 'threat', 'insult', 'identity_hate']

# # print(train_df[LABEL_COLUMNS].sum())

# # sample_row = train_df.iloc[12]

# # sample_comment = sample_row.comment_text
# # sample_labels = sample_row[LABEL_COLUMNS]

# # print(sample_comment)
# # print()
# # print(sample_labels.to_dict())

# train_labels = train_df[LABEL_COLUMNS].values.astype(float)
# val_labels = val_df[LABEL_COLUMNS].values.astype(float)

# train_comments = train_df['comment_text'].values.tolist()
# train_labels = train_labels.tolist()
# val_comments = val_df['comment_text'].values.tolist()
# val_labels = val_labels.tolist()

# print(train_labels[:8])

# tokenizer = DistilBertTokenizerFast.from_pretrained(model_name)

# train_encoding = tokenizer(train_comments, truncation=True, padding=True, max_length=512)
# val_encoding = tokenizer(val_comments, truncation=True, padding=True, max_length=512)

# print(train_encoding[4])

# train_dataset = Toxic_Comment_Dataset(train_encoding, train_labels)
# val_dataset = Toxic_Comment_Dataset(val_encoding, val_labels)

# training_args = TrainingArguments(
#     output_dir='/result',
#     num_train_epochs=2,
#     per_device_train_batch_size=16,
#     per_device_eval_batch_size=64,
#     warmup_steps=500,
#     learning_rate=5e-5,
#     weight_decay=0.01,
#     logging_dir='/logging',
#     logging_steps=10,
#     metric_for_best_model='f1'
# )

# model = DistilBertForSequenceClassification.from_pretrained(model_name, num_labels=6, problem_type="multi_label_classification").to(device)

# trainer = Trainer(
#     model=model,
#     args=training_args,
#     train_dataset=train_dataset,
#     eval_dataset=val_dataset
# )

# trainer.train()

# trainer.evaluate()

# text = "I really fucking hate that shirt, you should die and fuck your mom because your german!"

# encoding = tokenizer(text, return_tensors="pt")
# encoding = {k: v.to(device) for k,v in encoding.items()}

# outputs = trainer.model(**encoding)

# logits = outputs.logits
# logits.shape

# # apply sigmoid + threshold
# sigmoid = torch.nn.Sigmoid()
# probs = sigmoid(logits.squeeze().cpu())
# predictions = np.zeros(probs.shape)
# predictions[np.where(probs >= 0.5)] = 1
# # turn predicted id's into actual label names
# predicted_labels = [LABEL_COLUMNS[idx] for idx, label in enumerate(predictions) if label == 1.0]
# print(predicted_labels)