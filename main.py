from dcf_calculations import calculate_discounted_cash_flow, calculate_terminal_value, calculate_enterprise_value, calculate_equity_value
from sensitivity_analysis import sensitivity_analysis
from monte_carlo_simulation import monte_carlo_simulation
from visualization import plot_cash_flows_vs_discounted_cash_flows
from config import DEBT, CASH, PROJECTED_CASH_FLOWS
import numpy as np

def main():
    # Calculate discounted cash flows and terminal value
    discounted_cash_flows = calculate_discounted_cash_flow()
    terminal_value = calculate_terminal_value()
    
    # Calculate enterprise value and equity value
    enterprise_value = calculate_enterprise_value(discounted_cash_flows, terminal_value)
    equity_value = calculate_equity_value(enterprise_value, DEBT, CASH)
    
    # Print results
    print(f"Enterprise Value: ${enterprise_value:.2f} million")
    print(f"Equity Value: ${equity_value:.2f} million")
    
    # Visualize the cash flows vs discounted cash flows
    plot_cash_flows_vs_discounted_cash_flows(discounted_cash_flows)
    
    # Perform Sensitivity Analysis
    print("Performing Sensitivity Analysis...")
    sensitivity_analysis(np.arange(0.08, 0.15, 0.01), np.arange(0.01, 0.06, 0.01))
    
    # Run Monte Carlo Simulation
    print("Running Monte Carlo Simulation...")
    monte_carlo_simulation()

if __name__ == "__main__":
    main()
