import argparse
from collections import Counter
from pathlib import Path
import pandas as pd

AA = list("ACDEFGHIKLMNPQRSTVWY")

def composition(seqs):
    counts = Counter("".join(seqs))
    total = sum(counts.values())
    return pd.DataFrame([
        {"amino_acid": aa, "count": counts.get(aa, 0),
         "frequency": counts.get(aa, 0) / total if total else 0}
        for aa in AA
    ])

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--input", required=True)
    p.add_argument("--sequence-column", default="sequence")
    p.add_argument("--score-column", default="docking_score")
    p.add_argument("--top-fraction", type=float, default=0.10)
    p.add_argument("--output-dir", default="results")
    args = p.parse_args()

    df = pd.read_csv(args.input).dropna(subset=[args.sequence_column, args.score_column]).copy()
    df[args.sequence_column] = df[args.sequence_column].astype(str).str.upper().str.strip()
    df[args.score_column] = pd.to_numeric(df[args.score_column])

    out = Path(args.output_dir)
    out.mkdir(parents=True, exist_ok=True)

    composition(df[args.sequence_column].tolist()).to_csv(out/"amino_acid_composition.csv", index=False)

    n_top = max(1, int(len(df) * args.top_fraction))
    top = df.nsmallest(n_top, args.score_column)
    top.to_csv(out/"top_ranked_peptides.csv", index=False)

    print(f"Saved results to {out.resolve()}")

if __name__ == "__main__":
    main()
