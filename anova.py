import scipy.stats as stats

# Group by income level
groups = [group['Purchase_Amount'].values for name, group in data.groupby('Income_Level')]

# Perform ANOVA
f_stat, p_value = stats.f_oneway(*groups)

if p_value < 0.05:
    print("Reject the null hypothesis: Income level affects purchase amount.")
else:
    print("Fail to reject the null hypothesis: No effect of income level on purchase amount.")