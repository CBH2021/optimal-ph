import pandas as pd
import argparse
from sklearn.metrics import mean_squared_error
from scipy.stats import spearmanr


def benchmark(predictions_file, actuals_file):
    predictions_array = pd.read_csv(predictions_file)['prediction'].to_numpy()
    actuals_array = pd.read_csv(actuals_file)['actual'].to_numpy()

    mse = mean_squared_error(y_true=actuals_array, y_pred=predictions_array)
    correlation, pvalue = spearmanr(a=actuals_array, b=predictions_array)

    return {
        'mean_squared_error': mse,
        'spearman_rank': {
            'correlation':  correlation,
            'pvalue': pvalue,
        }
    }


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--predictions', default='predictions.csv')
    parser.add_argument('--actual', default='actual.csv')
    args = parser.parse_args()
    print('Benchmarks: ', benchmark(args.predictions, args.actual))
