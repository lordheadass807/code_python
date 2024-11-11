import random

def montecarlo(num_samples: int):
    circle = 0  

    for i in range(num_samples):
        x = random.uniform(-1, 1)  
        y = random.uniform(-1, 1)  

        if x**2 + y**2 <= 1:
            circle += 1  

    pi_estimate = (circle / num_samples) * 4
    return pi_estimate

num_samples = 1000000  
pi_approximation = montecarlo(num_samples)
print(f"Estimated value of π with {num_samples} samples: {pi_approximation}")