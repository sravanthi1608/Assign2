import numpy as np
from scipy.stats import binom

# Simulating the experiment
np.random.seed(42)  # For reproducibility
sample_size = 10
prob_right_handed = 0.9
simulated_results = np.random.rand(sample_size) < prob_right_handed
num_right_handed_simulated = np.sum(simulated_results)

# Simulated probability
simulated_prob = num_right_handed_simulated / sample_size

# Theoretical probability using binomial distribution
k_values = np.arange(0, 7)  # At most 6 right-handed people
theoretical_prob = sum(binom.pmf(k, sample_size, prob_right_handed) for k in k_values)

# Compare simulated and theoretical probabilities
print("Simulated Probability:", simulated_prob)
print("Theoretical Probability:", theoretical_prob)

