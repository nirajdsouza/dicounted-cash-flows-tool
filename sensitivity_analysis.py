import numpy as np
import matplotlib.pyplot as plt
from dcf_calculations import calculate_discounted_cash_flow, calculate_enterprise_value, calculate_terminal_value
from config import LAST_YEAR_CF

def sensitivity_analysis(discount_rate_range, growth_rate_range):
    ev_matrix = np.zeros((len(discount_rate_range), len(growth_rate_range)))
    
    for i, discount_rate in enumerate(discount_rate_range):
        for j, growth_rate in enumerate(growth_rate_range):
            terminal_value = LAST_YEAR_CF * (1 + growth_rate) / (discount_rate - growth_rate)
            discounted_cash_flows = calculate_discounted_cash_flow()
            ev_matrix[i, j] = calculate_enterprise_value(discounted_cash_flows, terminal_value)
    
    # Plotting
    X, Y = np.meshgrid(growth_rate_range, discount_rate_range)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, ev_matrix, cmap='viridis')
    ax.set_xlabel('Growth Rate')
    ax.set_ylabel('Discount Rate')
    ax.set_zlabel('Enterprise Value')
    plt.title("Sensitivity Analysis (Discount Rate vs Growth Rate)")
    plt.show()
