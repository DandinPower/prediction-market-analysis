rm -rf markets
rm -rf mapped_markets
rm -rf visualization_output

source .venv/bin/activate && python fetch_all_finished_markets.py
source .venv/bin/activate && python match_markets_and_trades.py
source .venv/bin/activate && python visualize_price_history.py
source .venv/bin/activate && python strategies_gru.py