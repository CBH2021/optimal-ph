# Optimal-pH

The Optimal-pH challenge from [Copenhagen Bioinformatics Hackathon: 2021 Protein Edition](https://biohackathon.dk). 

**Benchmarking scoreboard:** [biolib.com/biohackathon/optimal-ph-scoreboard/](https://biolib.com/biohackathon/optimal-ph-scoreboard/)

## Challenge Aim

The focus of this challenge is to apply machine learning to predict the optimal pH of enzyme activity given the primary
amino acid sequences as input. A training set of about 105,000 protein sequences and the growth pH values of their hosts
organisms are provided.

## Getting Started

To get started ensure to follow the
guide [here](https://www.notion.so/Benchmarking-System-46bfaeea0119490cb611688b493c589a).

## Training

This repository contains a [baseline model](src/model.py) and a [training script](src/train.py) that trains the baseline
model and saves it to a pickle file as [src/model.pickle](src/model.pickle). You can run the training script
with `python3 src/train.py`

### Dataset

The dataset for training can be found [here](data/train_set.csv). It contains 105,000 primary protein
sequences (`sequence`), and the growth pH values of their hosts organisms (`mean_growth_PH`).

## Predictions

The goal is to predict `mean_growth_PH`. At prediction time you are given a csv file with the single column `sequence`
like:

```csv
sequence
MKKRAHIISFILILALLFTGCSGNKENTSKEPVKETTEKGTGNIKTGTTETNAKPIDDNYGT...
MGKGKRKKRIALYFKRAAVAMLVMVMLLQPIPGTAGSSVKSVEAAVTTGDYIDLQNTATELW...
MLFIDVLILTFALISSLWILLQSLYYTETPLKCEGHTSSNRKASIIVAIKDEPPKVIEELIE...
MIKPSIFLMILILIGFVVGIITYNQSPLLFSLLIQVNYFVLRGDYLSLITSILVTNSFTDFI...
```

Your [src/predict.py](src/predict.py) code should output a file called `predictions.csv` in the following format:

```
prediction
6.75
7.0
5.0
3.5
```

You can run the prediction script with `python3 src/predict.py --input_csv submission/input.csv`
