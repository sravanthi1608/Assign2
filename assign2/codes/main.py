import scipy.special

def bernoulli_probability(n, k, p):
    q = 1 - p
    binomial_coefficient = scipy.special.comb(n, k)
    probability = binomial_coefficient * (p ** k) * (q ** (n - k))
    return probability

n = 10  # Sample size
p = 0.90  # Probability of right-handedness

total_probability = 0
for k in range(7):  # k ranges from 0 to 6 (at most 6)
    total_probability += bernoulli_probability(n, k, p)

print(f"Probability of at most 6 of a random sample of 10 people are right-handed: {total_probability:.4f}")

