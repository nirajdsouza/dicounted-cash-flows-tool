import random
import matplotlib.pyplot as plt
from dcf_calculations import calculate_discounted_cash_flow, calculate_enterprise_value, calculate_terminal_value
from config import LAST_YEAR_CF

def monte_carlo_simulation(num_simulations=1000):
    simulations = []
    for _ in range(num_simulations):
        discount_rate_sim = random.uniform(0.08, 0.12)  # Simulate within a range
        growth_rate_sim = random.uniform(0.01, 0.05)  # Simulate within a range
        
        terminal_value = LAST_YEAR_CF * (1 + growth_rate_sim) / (discount_rate_sim - growth_rate_sim)
        discounted_cash_flows = calculate_discounted_cash_flow()
        enterprise_value = calculate_enterprise_value(discounted_cash_flows, terminal_value)
        simulations.append(enterprise_value)
    
    # Plot histogram of results
    plt.hist(simulations, bins=50, color='blue', edgecolor='black')
    plt.xlabel('Enterprise Value (in millions)')
    plt.ylabel('Frequency')
    plt.title('Monte Carlo Simulation - Enterprise Value Distribution')
    plt.show()
