# Valuation Toolkit

This project is a financial valuation toolkit developed as a learning tool to help understand the concepts and calculations used in discounted cash flow (DCF) analysis, sensitivity analysis, and Monte Carlo simulation. It provides functions to calculate enterprise value, equity value, and visualize cash flows, among other tools.

## Features

-   **Discounted Cash Flow (DCF)**: Calculate discounted cash flows based on projected cash flows and discount rates.
-   **Terminal Value Calculation**: Compute the terminal value based on growth rates and discount rates.
-   **Enterprise & Equity Value Calculation**: Calculate the enterprise and equity values using the DCF and terminal value.
-   **Sensitivity Analysis**: Perform sensitivity analysis to understand the impact of varying discount and growth rates on enterprise value.
-   **Monte Carlo Simulation**: Run simulations to estimate the probability distribution of enterprise values based on random variations in discount and growth rates.
-   **Visualizations**: Plot projected cash flows vs discounted cash flows and visualize sensitivity analysis results.

## Modules

1.  **`dcf_calculations.py`**: Functions to calculate discounted cash flows, terminal value, enterprise value, and equity value.
2.  **`monte_carlo_simulation.py`**: Implements Monte Carlo simulations to simulate variations in enterprise value.
3.  **`sensitivity_analysis.py`**: Performs sensitivity analysis and visualizes results.
4.  **`visualization.py`**: Contains plotting functions for visualizing cash flows, discounted cash flows, and sensitivity analysis results.

## Usage

-   The `main.py` file demonstrates how to use the toolkit by calling functions to calculate discounted cash flows, terminal value, enterprise value, equity value, and running Monte Carlo simulations.
-   You can modify the `PROJECTED_CASH_FLOWS`, `DISCOUNT_RATE`, `GROWTH_RATE`, `DEBT`, and `CASH` variables in the `config.py` file to adjust the assumptions for the valuation.

## License

[MIT](LICENSE) License.