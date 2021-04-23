import argparse
import pandas as pd

from model import baseline_model

parser = argparse.ArgumentParser()
parser.add_argument('--input_csv', default='input.csv')
args = parser.parse_args()

# Config
model_to_use = baseline_model
output_file_path = '../test/predictions.csv'

# Load input.csv
with open(args.input_csv) as input_csv:
    data_frame = pd.read_csv(input_csv)

# Run predictions
Y_predictions = []
for index, row in data_frame.iterrows():
    prediction = model_to_use(row['sequence'])
    Y_predictions.append(prediction)

# Save predictions to file
df_predictions = pd.DataFrame({'prediction': Y_predictions})
df_predictions.to_csv(output_file_path, index=False)
