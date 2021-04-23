# Very simple baseline model
def baseline_model(fasta_sequence: str):
    return (6 + len(fasta_sequence)) / 1000 + 7
