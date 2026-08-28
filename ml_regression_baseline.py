import argparse, json
from pathlib import Path
import numpy as np
import pandas as pd
from scipy.stats import spearmanr
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder

AA = list("ACDEFGHIKLMNPQRSTVWY")

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--input", required=True)
    p.add_argument("--sequence-column", default="sequence")
    p.add_argument("--target-column", default="docking_score")
    p.add_argument("--output-dir", default="results_ml")
    args = p.parse_args()

    df = pd.read_csv(args.input).dropna(subset=[args.sequence_column, args.target_column]).copy()
    seq = df[args.sequence_column].astype(str).str.upper().str.strip()
    if seq.str.len().nunique() != 1:
        raise ValueError("All sequences must have equal length.")

    arr = np.array([list(s) for s in seq])
    enc = OneHotEncoder(categories=[AA] * arr.shape[1], handle_unknown="ignore", sparse_output=False)
    X = enc.fit_transform(arr)
    y = pd.to_numeric(df[args.target_column]).to_numpy()

    Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2, random_state=42)
    model = Ridge(alpha=1.0).fit(Xtr, ytr)
    pred = model.predict(Xte)

    metrics = {
        "MAE": float(mean_absolute_error(yte, pred)),
        "R2": float(r2_score(yte, pred)),
        "Spearman": float(spearmanr(yte, pred).statistic)
    }

    out = Path(args.output_dir)
    out.mkdir(parents=True, exist_ok=True)
    pd.DataFrame({"observed": yte, "predicted": pred}).to_csv(out/"predicted_vs_observed.csv", index=False)
    (out/"metrics.json").write_text(json.dumps(metrics, indent=2))
    print(json.dumps(metrics, indent=2))

if __name__ == "__main__":
    main()
