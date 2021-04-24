import pandas as pd
import numpy as np

data = pd.read_csv("../data/train_set.csv")
out_str = "> Seq" + data.index.astype(str) + " pH" + data.mean_growth_PH.astype(str) + "\n" + data.sequence
np.savetxt('train_set.fasta', out_str, fmt = "%s")