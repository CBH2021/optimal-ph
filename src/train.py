import pandas as pd
from sklearn.model_selection import train_test_split
from model import BaselineModel

# Config
train_data_file_path = 'data/train_set.csv'
model_file_path = 'model.pickle'

# Load data set
with open(train_data_file_path, 'rb') as train_data:
    df = pd.read_csv(train_data)

df_train, df_test = train_test_split(df, test_size=0.2)

BaselineModel().train(df_train, model_file_path)
