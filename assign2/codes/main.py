from scipy.stats import binom

# Parameters
n = 10  # number of trials (sample size)
p = 0.9  # probability of success (right-handed)
k_max = 6  # maximum number of right-handed individuals

# Calculate the probability using the cumulative distribution function (CDF)
probability_at_most_6 = binom.cdf(k_max, n, p)

formatted_probability = "{:.4f}".format(probability_at_most_6)

print("Probability that at most 6 out of 10 people are right-handed:", formatted_probability)

