import argparse
import pandas as pd
from model import BaselineModel

parser = argparse.ArgumentParser()
parser.add_argument('--input_csv', default='input.csv')
args = parser.parse_args()

# Config
output_file_path = 'predictions.csv'

# Load input.csv
with open(args.input_csv) as input_csv:
    df = pd.read_csv(input_csv)

# Run predictions
y_predictions = BaselineModel(model_file_path='src/model.pickle').predict(df)

# Save predictions to file
df_predictions = pd.DataFrame({'prediction': y_predictions})
df_predictions.to_csv(output_file_path, index=False)

print(f'{len(y_predictions)} predictions saved to a csv file')
