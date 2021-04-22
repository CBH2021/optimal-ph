# Optimal-pH

This challenge repository is to be forked by the participants at
the [Copenhagen Bioinformatics Hackathon 2021](https://biohackathon.dk).

## Challenge Aim

When identifying novel enzymes to fit a specific industrial application it is essential to select enzyme candidates with
the right pH optimum profile. Being able to predict this property from the protein’s 3D structure or the primary
sequence can greatly accelerate the discovery process. We have collected a set of optimal growth pH of publicly
sequenced microbial genomes. The secreted proteins of these genomes have been gathered alongside. If we rely on the
assumption, that the secreted enzymes are evolutionary coupled with the preferred growth conditions of the organism, we
may use the organism’s growth pH as a proxy for the optimal pH of the enzymes it secretes.

The focus of this challenge will be to apply machine learning to predict the optimal pH of enzyme activity given the
primary amino acid sequences as input. A training set of about 170,000 protein sequences and the growth pH values of
their hosts organisms will be provided.

## Data

The dataset for training can be found [here](data/train_set.csv).

### Example Output

You code should output a file called `predictions.csv` in the following format:

```
prediction
3.5
6
7
```

## Benchmarking System

The continuous integration script in `.github/workflows/ci.yml` will automatically build the `Dockerfile` on every
commit to the `main` branch. This docker image will be published as your hackathon submission
to `https://biolib.com/<YourTeam>/<TeamName>`. For this to work, make sure you set the `BIOLIB_TOKEN`
and `BIOLIB_PROJECT_URI` accordingly as repository secrets.

To read more about the benchmarking
system [click here](https://www.notion.so/Benchmarking-System-46bfaeea0119490cb611688b493c589a).
