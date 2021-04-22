import argparse
import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument('--input_csv')
args = parser.parse_args()

# Load input.csv
with open(args.input_csv) as input_csv:
    print(input_csv)
    data_frame = pd.read_csv(input_csv)

print(data_frame)
