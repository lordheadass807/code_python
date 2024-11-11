import random

def montecarlo(num_samples: int):
    circle = 0  # Counter for points that fall inside the circle

    # Generate 'num_samples' random points and check if they fall within the unit circle
    for i in range(num_samples):
        x = random.uniform(-1, 1)  # Random x coordinate
        y = random.uniform(-1, 1)  # Random y coordinate

        # Check if the point (x, y) lies within the unit circle
        if x**2 + y**2 <= 1:
            circle += 1  # Count points inside the circle

    # Estimate of π based on the ratio of points inside the circle to total points
    pi_estimate = (circle / num_samples) * 4
    return pi_estimate

num_samples = 1000000  # Number of random points checked w/ montecarlo
pi_approximation = montecarlo(num_samples)
print(f"Estimated value of π with {num_samples} samples: {pi_approximation}")