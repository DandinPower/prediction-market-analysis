# Analysis and Experiments

This module trains and evaluates prediction-market classifiers on preprocessed market folders, then writes plots and summary tables for comparison.

## 1. Prerequisite

Before running anything in this folder:

1. Complete the preprocessing pipeline in [preprocessing](../preprocessing/README.md).
2. Ensure mapped markets are generated at `datasets/mapped_markets`, with structure like:
   - `datasets/mapped_markets/<market_id>/metadata.json`
   - `datasets/mapped_markets/<market_id>/yes.csv`
   - `datasets/mapped_markets/<market_id>/no.csv`
3. Use the project virtual environment (managed by `uv`):
    ```bash
    source .venv/bin/activate
    ```

## 2. Scripts

### Run all experiments (default happy path, with cross-validation)

From project root:

```bash
source .venv/bin/activate
python -m analysis_and_experiments.experiments.runner \
  --preset all \
  --mapped-markets-path datasets/mapped_markets \
  --output-root outputs
```

Notes:
- Default behavior is **5-fold stratified cross-validation** (`--cv-folds 5`).
- This command runs all presets in order: `exp1`, `exp2`, `exp3`, `exp4`, `exp5`.

### Run analysis scripts (default happy path)

Outcome distribution analysis:

```bash
source .venv/bin/activate
python -m analysis_and_experiments.analysis.market_outcome
```

Market-type clustering analysis:

```bash
source .venv/bin/activate
python -m analysis_and_experiments.analysis.market_type
```

## 3. Experiments Explanation

### A. Motivation

The experiments are designed to answer three practical questions:

- Can market microstructure data predict final market outcome (`yes`/`no`)?
- Which modeling family works better for this dataset: sequence model (GRU) or engineered-feature tabular model (XGBoost)?
- How sensitive performance is to early-trade truncation ratio and sequence length choices?

### B. High-Level Approach

1. Load filtered markets and trades from `datasets/mapped_markets`.
2. Build model inputs:
   - GRU path: convert trade streams into candlestick sequences.
   - Tabular path: extract per-market statistical/flow features.
3. Train/evaluate using stratified CV by default.
4. Compare runs by validation metrics and average margin-of-victory proxy.
5. Save artifacts for review.

Preset intent:

- `exp1`: GRU baseline at default ratio/candle count.
- `exp2`: Tabular baseline at default ratio.
- `exp3`: GRU + Tabular ratio sweep (`0.33, 0.50, 0.67, 0.80, 0.95`).
- `exp4`: GRU candle-count sweep at default ratio.
- `exp5`: Same as ratio sweep, but with BTC-specific market filter policy.

### C. Output Result Format

All outputs are rooted at `outputs/`.

Plots (`.png`):

- ROC curves:
  - `outputs/plots/roc/gru/*.png`
  - `outputs/plots/roc/tabular/*.png`
- GRU train/val curves:
  - `outputs/plots/training_curves/gru/*_loss.png`
  - `outputs/plots/training_curves/gru/*_accuracy.png`
- Confusion matrices:
  - `outputs/plots/confusion_matrix/gru/*_train.png`, `*_val.png`
  - `outputs/plots/confusion_matrix/tabular/*_train.png`, `*_val.png`

CSV summaries:

- `outputs/results/<preset>/summary.csv`
  - One row per run (preset + strategy + ratio + metrics + artifact paths).
- `outputs/results/<preset>/summary_folds.csv`
  - One row per fold (fold index, train/val sizes, fold metrics, fold margin).

JSON summaries:

- `outputs/results/<preset>/summary.json`
  - Includes:
    - `runs`: full run payloads (metrics + artifact paths + fold results)
    - `ranking_by_margin`
    - `ranking_by_auc`

Default CV file naming:

- When running default CV (`cv_folds=5`), filenames include `_cv5`.
