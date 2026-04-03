# Dataset Preprocessing Pipeline

This document explains how to build preprocessing outputs for this project:

1. Fetch Polymarket market metadata.
2. Download Polymarket trades from Polygon.
3. Match trades to markets and generate visualization outputs.

## Environment

- Use the root project virtual environment for preprocessing CLI commands:

  ```bash
  source .venv/bin/activate
  ```

- `poly-trade-scan` uses a separate Python environment. For installation, setup, and full CLI usage, follow:
  - [preprocessing/poly-trade-scan/README.md](./poly-trade-scan/README.md)

## Step 1: Prepare Market Metadata

To reproduce the dataset results in this repo, **use the decompression path first**.

Use manual API fetching only when you intentionally want to change the experiment date range.

### Option A (Recommended): Use Pre-downloaded Compressed Metadata

```bash
gzip -dc datasets/metadata/all_markets_metadata.json.gz > datasets/metadata/all_markets_metadata.json
```

### Option B: Fetch from Polymarket API

```bash
source .venv/bin/activate
python -m preprocessing.cli fetch
```

Default output:

- `datasets/metadata/all_markets_metadata.json`

If needed, you can override dates/output path:

```bash
python -m preprocessing.cli fetch \
  --start-date-min 2025-12-25T00:00:00Z \
  --end-date-min 2025-12-25T00:00:00Z \
  --end-date-max 2025-12-31T23:59:59Z \
  --output-path datasets/metadata/all_markets_metadata.json
```

## Step 2: Prepare Trades Data

To reproduce the dataset results in this repo, **use the decompression path first**.

Use Polygon re-download only when you intentionally want to change the experiment date range.

### Option A (Recommended): Reassemble and Decompress the Pre-split Archive

```bash
cat datasets/trades/2025_12_25_31.gz.part* > datasets/trades/2025_12_25_31.gz
gunzip datasets/trades/2025_12_25_31.gz -N
```

### Option B: Download by Scanning Polygon

Use `poly-trade-scan` to crawl Polygon blocks and export trades CSV. Use the scanner setup and command details in:

- [preprocessing/poly-trade-scan/README.md](./poly-trade-scan/README.md)

Reference Polygon endpoint list:

- https://chainlist.org/chain/137

For the 2025-12-25 to 2025-12-31 window, use these block boundaries (mirrored from `preprocessing/NOTES.md`):

- `80750701`: end of 2025-12-24 / start of 2025-12-25
- `80923501`: end of 2025-12-28 / start of 2025-12-29
- `80966750`: end of 2025-12-29 / start of 2025-12-30
- `81009975`: end of 2025-12-30 / start of 2025-12-31
- `81053200`: end of 2025-12-31

Recommended scan range for full 2025-12-25 to 2025-12-31 coverage:

```bash
poly download --start 80750701 --end 81053200 --output datasets/trades/2025_12_25_31.csv
```

Expected runtime note:

- Downloading this full range can take about 1 day, depending on RPC performance and rate limits.

## Step 3: Match Trades to Markets

Run:

```bash
source .venv/bin/activate
python -m preprocessing.cli match
```

Default inputs:

- Metadata: `datasets/metadata/all_markets_metadata.json`
- Trades folder: `datasets/trades`

Default output:

- `datasets/mapped_markets/<market_id>/metadata.json`
- `datasets/mapped_markets/<market_id>/yes.csv`
- `datasets/mapped_markets/<market_id>/no.csv`

## Data Formats and Matching Logic

### `all_markets_metadata.json` format

- Top-level structure: a JSON array.
- Each element is one Polymarket market object from Gamma API (`/markets`), plus one field added by this pipeline:
  - `outcome`: derived in preprocessing (`"yes"` or `"no"`), based on `outcomePrices`.

Important fields used by the matching pipeline:

- `id`: market ID (used as folder name in `mapped_markets`).
- `question`: market title.
- `startDate`, `endDate`: market time range.
- `clobTokenIds`: JSON-encoded string with two token IDs.
- `outcomes`: JSON-encoded string for outcome labels (for example `["Up","Down"]`).
- `outcomePrices`: JSON-encoded string used to infer resolved side.

### Trades CSV format (scanner output)

Raw trades CSV files in `datasets/trades/*.csv` are expected to contain:

| Column | Meaning |
| --- | --- |
| `block_number` | Polygon block number |
| `timestamp` | Block timestamp in ISO 8601 UTC |
| `tx_hash` | Transaction hash |
| `wallet` | Trader wallet address |
| `token_id` | CLOB token ID traded (critical for market matching) |
| `side` | `BUY` or `SELL` from trader perspective |
| `tokens` | Number of outcome tokens traded |
| `price` | Price per outcome token |
| `total_usdc` | Total USDC amount for that fill |

### How matching works (token-based mapping)

The matching step uses token IDs to connect each trade row to the correct market side:

1. Load all markets from `all_markets_metadata.json`.
2. Parse each market's `clobTokenIds` and build a lookup table:
   - `yes_token_id -> (market, "yes")`
   - `no_token_id -> (market, "no")`
3. Stream all trade CSV rows from `datasets/trades/*.csv`.
4. For each trade row, read `token_id` and look up `(market, side)` from the table.
5. Append the trade into that market's `yes_trades` or `no_trades`, and increment:
   - `trade_count`
   - `yes_trade_count`
   - `no_trade_count`
6. Keep only markets with `trade_count > trade_count_threshold` (default threshold is `1`).
7. Sort `yes_trades` and `no_trades` by timestamp, then write files into `datasets/mapped_markets`.

This token-based mapping is what correctly links one raw trade record to the market's YES or NO side.

## `mapped_markets` Output Structure

After `python -m preprocessing.cli match`, output structure is:

```text
datasets/mapped_markets/
├── <market_id>/
│   ├── metadata.json
│   ├── yes.csv
│   └── no.csv
└── ...
```

After `python -m preprocessing.cli visualize`, additional files are generated:

```text
datasets/mapped_markets/
├── <market_id>/
│   ├── yes_price_history_final.png
│   ├── metadata.json
│   ├── yes.csv
│   └── no.csv
└── yes_trade_count_distribution.png
```

### `metadata.json` in each market folder

- Contains the full original market metadata object (all Gamma API fields).
- Excludes in-memory arrays `yes_trades` and `no_trades` to keep file size manageable.
- Includes pipeline-added counters:
  - `trade_count`
  - `yes_trade_count`
  - `no_trade_count`
- Usually includes `outcome` (added during fetch post-processing).

### `yes.csv` and `no.csv` format

Both files use the same schema:

| Column | Meaning |
| --- | --- |
| `block_number` | Polygon block number |
| `timestamp` | Trade timestamp |
| `tx_hash` | Transaction hash |
| `wallet` | Trader wallet |
| `side` | `BUY` or `SELL` |
| `tokens` | Quantity of outcome tokens |
| `price` | Price per token |
| `total_usdc` | Total USDC traded |

Notes:

- `yes.csv` contains trades whose `token_id` matched that market's YES token.
- `no.csv` contains trades whose `token_id` matched that market's NO token.
- `token_id` is not written into these files because side-specific splitting is already done.

## Visualization

Generate visualization outputs from mapped markets:

```bash
source .venv/bin/activate
python -m preprocessing.cli visualize
```

Outputs:

- Per market: `datasets/mapped_markets/<market_id>/yes_price_history_final.png`
- Global distribution: `datasets/mapped_markets/yes_trade_count_distribution.png`

`yes_price_history_final.png` details:

- Built from `yes.csv` (not `no.csv`).
- Uses filtered YES trades (`BUY`, `price < 0.98`, `total_usdc > 2.0`) in visualization code.
- Generated only for markets that pass market filtering (`yes_trade_count > 500`), so many market folders may not have this PNG.
- The line plot is ordered by trade time, and shows the YES price trajectory for that market.

Why only YES is plotted:

- For binary Polymarket markets, YES and NO encode the same underlying event from opposite sides.
- Their information is largely mirrored/complementary, so plotting both is usually redundant.
- Using YES only is simpler and more intuitive for fast inspection and downstream analysis.

Selected market quick tip:

- Pick any market ID folder under `datasets/mapped_markets`, then open `yes_price_history_final.png` in that folder. If there is no `yes_price_history_final.png`, that market was filtered out in visualization (for example `yes_trade_count <= 500`).
