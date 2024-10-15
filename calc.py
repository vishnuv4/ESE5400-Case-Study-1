def tax_rate():
    tax = {}
    tax["2004"] = 7414/17910
    tax["2005"] = 12830/32723
    tax["2006"] = 11747/30447
    for i in tax.keys():
        print(f"Tax rate in year {i}: {tax[i]}")

    avg_tax_rate = (tax["2004"] + tax["2005"] + tax["2006"]) / 3
    print(f"Average tax rate: {avg_tax_rate}")
    return avg_tax_rate

def debtvalue():
    de_ratio = 0.593
    l = de_ratio / (de_ratio + 1)
    print(f"Debt value: {l}")
    return l

def wacc(t, l):
    rd = 0.0628
    re = 0.1091
    wacc = (l * (1 - t) * rd) + ((1 - l) * re)
    print(f"WACC: {wacc}")

def asset_beta(l):
    b_equity = 1.25
    b_asset = (1 - l) * b_equity
    print(f"Asset beta: {b_asset}")

if __name__ == "__main__":
    l = debtvalue()
    t = tax_rate()
    wacc(t, l)
    asset_beta(l)