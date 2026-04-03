# Prediction Market Analysis

This repository builds a Polymarket dataset, maps trades into per-market folders, and then runs model experiments on the processed data.

## Quick Start

From repository root:

```bash
uv sync
source .venv/bin/activate
```

Run flow (in order):

1. Preprocess dataset (metadata + trades -> mapped markets).
2. Run analysis/experiments on `datasets/mapped_markets`.

## Project Structure

```text
prediction-market-analysis/
├── preprocessing/                 # Data pipeline (fetch, match, visualize)
│   ├── cli.py
│   ├── README.md
│   └── poly-trade-scan/          # Polygon scanner subproject
├── analysis_and_experiments/      # Model training, evaluation, and analysis scripts
│   ├── experiments/
│   ├── analysis/
│   └── README.md
├── datasets/
│   ├── metadata/                  # Raw/processed market metadata
│   ├── trades/                    # Raw trade files / split archives
│   └── mapped_markets/            # Generated per-market training inputs
├── outputs/                       # Experiment outputs (plots, summaries)
├── pyproject.toml
└── uv.lock
```

## How To Run

### 1) Preprocess Dataset

Recommended reproducible path (uses included dataset artifacts):

```bash
# metadata
gzip -dc datasets/metadata/all_markets_metadata.json.gz > datasets/metadata/all_markets_metadata.json

# trades
cat datasets/trades/2025_12_25_31.gz.part* > datasets/trades/2025_12_25_31.gz
gunzip datasets/trades/2025_12_25_31.gz -N

# map trades to market folders
python -m preprocessing.cli match
```

Optional visualization step:

```bash
python -m preprocessing.cli visualize
```

If you need to fetch/download fresh data instead of using included archives, see:
- [preprocessing/README.md](preprocessing/README.md)

### 2) Run Analysis Experiments

Run all experiment presets:

```bash
python -m analysis_and_experiments.experiments.runner \
  --preset all \
  --mapped-markets-path datasets/mapped_markets \
  --output-root outputs
```

Main outputs:

- `outputs/results/<preset>/summary.csv`
- `outputs/results/<preset>/summary_folds.csv`
- `outputs/results/<preset>/summary.json`
- `outputs/plots/...`

For detailed experiment and analysis usage, see:
- [analysis_and_experiments/README.md](analysis_and_experiments/README.md)
