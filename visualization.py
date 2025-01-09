import matplotlib.pyplot as plt
import numpy as np
from config import PROJECTED_CASH_FLOWS


def plot_cash_flows_vs_discounted_cash_flows(discounted_cash_flows):
    years = list(discounted_cash_flows.keys())
    cash_flows = list(PROJECTED_CASH_FLOWS.values())
    
    plt.figure(figsize=(10, 6))
    plt.bar(years, cash_flows, label="Projected Cash Flows", color='blue', alpha=0.6)
    plt.bar(years, list(discounted_cash_flows.values()), label="Discounted Cash Flows", color='red', alpha=0.6)
    plt.xlabel("Year")
    plt.ylabel("Cash Flow (in millions)")
    plt.title("Projected Cash Flows vs Discounted Cash Flows")
    plt.legend()
    plt.show()

def plot_sensitivity_analysis(sensitivity_results):
    # Assuming sensitivity_results is a matrix or DataFrame of results from sensitivity analysis
    fig, ax = plt.subplots()
    ax.plot(sensitivity_results)
    ax.set_xlabel('Discount Rate / Growth Rate')
    ax.set_ylabel('Enterprise Value')
    ax.set_title('Sensitivity Analysis Results')
    plt.show()
