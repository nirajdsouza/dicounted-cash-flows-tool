# cash_flow.py
from config import DISCOUNT_RATE, PROJECTED_CASH_FLOWS, TERMINAL_GROWTH_RATE, LAST_YEAR_CF

# Function to calculate the Present Value (PV) of cash flows for each year
def calculate_discounted_cash_flow():
    discounted_cash_flows = {}
    
    for year, cash_flow in PROJECTED_CASH_FLOWS.items():
        discounted_cash_flows[year] = cash_flow / (1 + DISCOUNT_RATE) ** year
    
    return discounted_cash_flows

# Function to calculate the Terminal Value (TV) based on the last projected cash flow and terminal growth rate
def calculate_terminal_value():
    terminal_value = LAST_YEAR_CF * (1 + TERMINAL_GROWTH_RATE) / (DISCOUNT_RATE - TERMINAL_GROWTH_RATE)
    return terminal_value

# Function to calculate the total Enterprise Value (EV) based on discounted cash flows and terminal value
def calculate_enterprise_value(discounted_cash_flows, terminal_value):
    total_discounted_cash_flows = sum(discounted_cash_flows.values())
    enterprise_value = total_discounted_cash_flows + terminal_value
    return enterprise_value
