import pandas as pd
from sklearn.model_selection import train_test_split
from model import BaselineModel

# Load data set
with open('data/train_set.csv', 'rb') as train_data:
    df = pd.read_csv(train_data, nrows=1000)

df_train, df_test = train_test_split(df, test_size=0.2)

BaselineModel(model_file_path='src/model.pickle').train(df_train)
