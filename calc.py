import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# DRIVER LAYER (FUNDAMENTAL FORMULAE)

def dv_ratio_from_de_ratio(de_ratio):
    l = de_ratio / (de_ratio + 1)
    return l

def wacc(tax, debt_fraction, cost_of_equity, cost_of_debt):
    wacc = (debt_fraction * (1 - tax) * cost_of_debt) + ((1 - debt_fraction) * cost_of_equity)
    return wacc

def asset_beta(debt_fraction, b_equity):
    b_asset = (1 - debt_fraction) * b_equity
    return b_asset

def cost_of_equity(beta, emrp, rf):
    return (rf + (beta * emrp))

def unlevered_asset_beta(debt_fraction, beta_equity):
    return ((1 - debt_fraction) * beta_equity)

def relevered_equity_beta(debt_fraction_2, beta_asset):
    return ((1/(1 - debt_fraction_2)) * beta_asset)

# APPLICATION LAYER

def q3_tax_rate(print_output=False):
    tax_2006 = 11747/30447
    if print_output:
        print()
        print(f"Q3: Tax rate in year 2006 = {tax_2006}")

    return tax_2006


def q5_midland_cost_of_equity(print_output=False):
    rf = 0.0466
    beta = 1.25
    emrp = 0.05
    re = cost_of_equity(beta, emrp, rf)
    if print_output:
        print(f"Q5: Midland's consolidated cost of equity = {re}")
    return re

def q6_midland_wacc_2006():
    de_ratio = 0.593
    l = dv_ratio_from_de_ratio(de_ratio)
    rd = 0.0628
    re = q5_midland_cost_of_equity()
    t = q3_tax_rate()
    wacc_2006 = wacc(t, l, re, rd)
    print()
    print(f"Q6: WACC in 2006 = {wacc_2006}")

def q7_unlevered_asset_beta_2006(print_output=False):
    de_ratio = 0.593
    beta_equity = 1.25
    debt_fraction = dv_ratio_from_de_ratio(de_ratio)
    beta_asset = unlevered_asset_beta(debt_fraction, beta_equity)
    if print_output:
        print()
        print(f"Q7: Unlevered asset beta in 2006 = {beta_asset}")

    return beta_asset

def relevered_beta_equity_2007(print_output=False):
    debt_fraction_2007 = 0.422
    beta_asset = q7_unlevered_asset_beta_2006()
    beta_equity_2007 = relevered_equity_beta(debt_fraction_2007, beta_asset)
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

def q8_future_wacc_2007(print_output=False):
    l2 = 0.422
    rd = 0.0628
    t = q3_tax_rate()
    re = future_cost_of_equity_2007()
    wacc_2007 = wacc(t, l2, re, rd)
    if print_output:
        print(f"Q8: WACC in 2007 = {wacc_2007}")

def q9_graphs():
    rf = 0.0466
    rd = 0.0628
    emrp = 0.05
    t = q3_tax_rate()
    l_values = np.arange(0, 1., 0.01)
    re_data = []
    wacc_data = []
    for l in l_values:
        beta = relevered_equity_beta(l, unlevered_asset_beta(dv_ratio_from_de_ratio(0.593), 1.25))
        re_value = cost_of_equity(beta, emrp, rf)
        re_data.append(re_value)
        wacc_value = wacc(t, l, re_value, rd)
        wacc_data.append(wacc_value)

    plt.figure()
    plt.plot(l_values, np.array(re_data) * 100, label='Cost of Equity', color='blue')
    plt.xlabel('Debt fraction')
    plt.ylabel('Cost of equity (%)')
    plt.title('Cost of Equity vs. Debt Fraction')
    plt.grid(True)
    plt.legend()
    plt.savefig(Path(__file__).parent / "images" / "cost_of_equity.png")

    plt.figure()
    plt.plot(l_values, np.array(wacc_data) * 100, label='WACC', color='green')
    plt.xlabel('Debt fraction')
    plt.ylabel('WACC (%)')
    plt.title('WACC vs. Debt fraction')
    plt.grid(True)
    plt.legend()
    plt.savefig(Path(__file__).parent / "images" / "wacc.png")

def q10_company_segment_betas():
    print("Q10")
    e_and_p_equity_betas = {
        "Jackson": 0.89,
        "Wide Plain": 1.21,
        "Corsicana": 1.11,
        "Worthington": 1.39
    }
    e_and_p_de_ratios = {
        "Jackson": 0.112,
        "Wide Plain": 0.854,
        "Corsicana": 0.152,
        "Worthington": 0.475
    }
    r_and_m_equity_betas = {
        "Bexar": 1.70,
        "Kirk": 0.94,
        "White Point": 1.78,
        # Petrarch is the outlier
        "Arkana": 1.25,
        "Beaumont": 1.04,
        "Dameron": 1.42
    }
    r_and_m_de_ratios = {
        "Bexar": 0.103,
        "Kirk": 0.194,
        "White Point": 0.209,
        # Petrarch is the outlier
        "Arkana": 0.323,
        "Beaumont": 0.206,
        "Dameron": 0.503
    }

    e_and_p_asset_betas = {}
    for i in e_and_p_equity_betas.keys():
        e_and_p_asset_betas[i] = asset_beta(dv_ratio_from_de_ratio(e_and_p_de_ratios[i]), e_and_p_equity_betas[i])
    
    for k, v in e_and_p_asset_betas.items():
        print(f"Asset beta for {k}: {v}")

    r_and_m_asset_betas = {}
    for i in r_and_m_equity_betas.keys():
        r_and_m_asset_betas[i] = asset_beta(dv_ratio_from_de_ratio(r_and_m_de_ratios[i]), r_and_m_equity_betas[i])

    for k, v in r_and_m_asset_betas.items():
        print(f"Asset beta for {k}: {v}")

    print()

    e_and_p_avg_asset_beta = sum(e_and_p_asset_betas.values()) / len(e_and_p_asset_betas)
    print(f"Average asset beta for exploration and marketing: {e_and_p_avg_asset_beta}")

    r_and_m_avg_asset_beta = sum(r_and_m_asset_betas.values()) / len(r_and_m_asset_betas)
    print(f"Average asset beta for refining and marketing: {r_and_m_avg_asset_beta}")

    e_and_p_dv_midland = 0.46
    r_and_m_dv_midland = 0.31
    e_and_p_rd_midland = 0.0626
    r_and_m_rd_midland = 0.0646
    rf = 0.0466
    emrp = 0.05
    t = q3_tax_rate()


    e_and_p_equity_beta_midland = relevered_equity_beta(e_and_p_dv_midland, e_and_p_avg_asset_beta)
    r_and_m_equity_beta_midland = relevered_equity_beta(r_and_m_dv_midland, r_and_m_avg_asset_beta)

    e_and_p_cost_of_equity_midland = cost_of_equity(e_and_p_equity_beta_midland, emrp, rf)
    r_and_m_cost_of_equity_midland = cost_of_equity(r_and_m_equity_beta_midland, emrp, rf)

    e_and_p_wacc = wacc(t, e_and_p_dv_midland, e_and_p_cost_of_equity_midland, e_and_p_rd_midland)
    r_and_m_wacc = wacc(t, r_and_m_dv_midland, r_and_m_cost_of_equity_midland, r_and_m_rd_midland)

    print(f"Midland's equity beta for Exploration and Production: {e_and_p_equity_beta_midland}")
    print(f"Midland's equity beta for Refining and Marketing: {r_and_m_equity_beta_midland}")

    print(f"Midland's cost of equity for Exploration and Production: {e_and_p_cost_of_equity_midland}")
    print(f"Midland's cost of equity for Refining and Marketing: {r_and_m_cost_of_equity_midland}")

    print(f"Midland's WACC for Exploration and Production: {e_and_p_wacc}")
    print(f"Midland's WACC for Refining and Marketing: {r_and_m_wacc}")


if __name__ == "__main__":
    # q3_tax_rate(print_output=True)
    # q5_midland_cost_of_equity(print_output=True)
    # q6_midland_wacc_2006()
    # q7_unlevered_asset_beta_2006(print_output=True)
    # relevered_beta_equity_2007(print_output=True)
    # future_cost_of_equity_2007(print_output=True)
    # q8_future_wacc_2007(print_output=True)
    # q9_graphs()
    q10_company_segment_betas();