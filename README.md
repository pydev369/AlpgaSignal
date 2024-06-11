# AlpgaSignal


# Quant Alpha Signal Generation

## Overview
This project generates alpha signals based on OHLCV data and option chain data for market regime detection. It includes data collection, feature engineering, signal generation, and backtesting.

## Setup

1. Clone the repository:
    ```
    git clone https://github.com/your_username/quant_alpha_signal.git
    cd quant_alpha_signal
    ```

2. Install the dependencies:
    ```
    pip install -r requirements.txt
    ```

## Usage

1. Update `ALPHA_VANTAGE_API_KEY` in `scripts/data_collection.py` with your Alpha Vantage API key.
2. Run the main script:
    ```
    python scripts/main.py
    ```

## Project Structure

- `data/`: Contains example data.
- `scripts/`: Contains Python scripts for data collection, feature engineering, signal generation, and backtesting.
- `notebooks/`: Contains Jupyter notebooks for demonstrations.
- `requirements.txt`: Lists project dependencies.

## Example

An example Jupyter notebook demonstrating the usage and results is included in the `notebooks/` directory.
