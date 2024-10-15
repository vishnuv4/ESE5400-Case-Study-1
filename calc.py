# DRIVER LAYER

def debtvalue_from_de_ratio(de_ratio):
    l = de_ratio / (de_ratio + 1)
    return l

def wacc(tax, debt_value, cost_of_equity, cost_of_debt):
    wacc = (debt_value * (1 - tax) * cost_of_debt) + ((1 - debt_value) * cost_of_equity)
    return wacc

def asset_beta(debt_value, b_equity):
    b_asset = (1 - debt_value) * b_equity
    return b_asset

def cost_of_equity(beta, emrp, rf):
    return (rf + (beta * emrp))

def unlevered_asset_beta(debt_value, beta_equity):
    return ((1 - debt_value) * beta_equity)

def relevered_equity_beta(debt_value_2, beta_asset):
    return ((1/(1 - debt_value_2)) * beta_asset)

# APPLICATION LAYER

def average_tax_rate(print_output=False):
    tax = {}
    tax["2004"] = 7414/17910
    tax["2005"] = 12830/32723
    tax["2006"] = 11747/30447
    if print_output:
        print()
        for i in tax.keys():
            print(f"Tax rate in year {i}: {tax[i]}")

    avg_tax_rate = (tax["2004"] + tax["2005"] + tax["2006"]) / 3
    if print_output:
        print(f"Q3: Average tax rate = {avg_tax_rate}")
        print()
    return avg_tax_rate


def midland_cost_of_equity(print_output=False):
    rf = 0.0466
    beta = 1.25
    emrp = 0.05
    re = cost_of_equity(beta, emrp, rf)
    if print_output:
        print(f"Q5: Midland's consolidated cost of equity = {re}")
    return re

def midland_wacc_2006():
    de_ratio = 0.593
    l = debtvalue_from_de_ratio(de_ratio)
    rd = 0.0628
    re = midland_cost_of_equity()
    t = average_tax_rate()
    wacc_2006 = wacc(t, l, re, rd)
    print()
    print(f"Q6: WACC in 2006 = {wacc_2006}")

def unlevered_asset_beta_2006(print_output=False):
    de_ratio = 0.593
    beta_equity = 1.25
    debt_value = debtvalue_from_de_ratio(de_ratio)
    beta_asset = unlevered_asset_beta(debt_value, beta_equity)
    if print_output:
        print()
        print(f"Q7: Unlevered asset beta in 2006 = {beta_asset}")

    return beta_asset

def relevered_beta_equity_2007(print_output=False):
    debt_value_2007 = 0.422
    beta_asset = unlevered_asset_beta_2006()
    beta_equity_2007 = relevered_equity_beta(debt_value_2007, beta_asset)
    if print_output:
        print()
        print(f"Beta equity for 2007: {beta_equity_2007}")
    return beta_equity_2007

def future_cost_of_equity_2007(print_output=False):
    rf = 0.0466
    emrp = 0.05
    beta = relevered_beta_equity_2007()
    re = cost_of_equity(beta, emrp, rf)
    if print_output:
        print(f"Q8: Cost of equity = {re}")
    return re

def future_wacc_2007(print_output=False):
    l2 = 0.422
    rd = 0.0628
    t = average_tax_rate()
    re = future_cost_of_equity_2007()
    wacc_2007 = wacc(t, l2, re, rd)
    if print_output:
        print(f"Q8: WACC in 2007 = {wacc_2007}")

if __name__ == "__main__":
    average_tax_rate(print_output=True)
    midland_cost_of_equity(print_output=True)
    midland_wacc_2006()
    unlevered_asset_beta_2006(print_output=True)
    relevered_beta_equity_2007(print_output=True)
    future_cost_of_equity_2007(print_output=True)
    future_wacc_2007(print_output=True)