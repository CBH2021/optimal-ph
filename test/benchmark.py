import pandas as pd
import numpy as np
import argparse


def benchmark(predictions_file, actuals_file):
    predictions = pd.read_csv(predictions_file).to_dict(orient="records")
    actuals = pd.read_csv(actuals_file).to_dict(orient="records")

    predictions_dict = {}
    for prediction in predictions:
        predictions_dict[prediction["name"]] = prediction["prediction"]

    actuals_dict = {}
    for actual in actuals:
        actuals_dict[actual["name"]] = actual["actual"]

    results = []
    for (name, actual) in actuals_dict.items():
        results.append(1 if predictions_dict[name] == actual else 0)

    accuracy = np.array(results).mean()
    result = {}
    result["accuracy"] = accuracy
    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--predictions')
    parser.add_argument('--actual')
    args = parser.parse_args()
    print("Benchmarks:", benchmark(args.predictions, args.actual))
