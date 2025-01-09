from config import DISCOUNT_RATE, GROWTH_RATE, PROJECTED_CASH_FLOWS, LAST_YEAR_CF, DEBT, CASH

def calculate_discounted_cash_flow():
    discounted_cash_flows = {}
    for year, cash_flow in PROJECTED_CASH_FLOWS.items():
        discounted_cash_flows[year] = cash_flow / (1 + DISCOUNT_RATE) ** year
    return discounted_cash_flows

def calculate_terminal_value():
    terminal_value = LAST_YEAR_CF * (1 + GROWTH_RATE) / (DISCOUNT_RATE - GROWTH_RATE)
    return terminal_value

def calculate_enterprise_value(discounted_cash_flows, terminal_value):
    enterprise_value = sum(discounted_cash_flows.values()) + terminal_value
    return enterprise_value

def calculate_equity_value(enterprise_value, debt, cash):
    equity_value = enterprise_value - (debt - cash)
    return equity_value
