import numpy as np
print("Avinash Pandey-21BCT0179")
# Define the conditional probabilities
P_Cloudy = 0.5
P_Sprinkler_given_Cloudy = {True: 0.1, False: 0.5}  # P(Sprinkler | Cloudy)
P_Rain_given_Cloudy = {True: 0.8, False: 0.2}       # P(Rain | Cloudy)
P_WetGrass_given_Sprinkler_Rain = {                # P(WetGrass | Sprinkler, Rain)
    (True, True): 0.99,
    (True, False): 0.90,
    (False, True): 0.80,
    (False, False): 0.00
}

# Monte Carlo simulation to estimate P(WetGrass=True | Rain=True)
def monte_carlo_simulation(num_samples=10000):
    count_wet_grass_given_rain = 0  # Count of samples where WetGrass=True and Rain=True
    count_rain = 0                 # Count of samples where Rain=True
    
    for _ in range(num_samples):
        # Sample Cloudy
        cloudy = np.random.rand() < P_Cloudy

        # Sample Sprinkler given Cloudy
        sprinkler = np.random.rand() < P_Sprinkler_given_Cloudy[cloudy]

        # Sample Rain given Cloudy
        rain = np.random.rand() < P_Rain_given_Cloudy[cloudy]

        # Sample WetGrass given Sprinkler and Rain
        wet_grass = np.random.rand() < P_WetGrass_given_Sprinkler_Rain[(sprinkler, rain)]

        # Accumulate counts if Rain is True
        if rain:
            count_rain += 1
            if wet_grass:
                count_wet_grass_given_rain += 1

    # Calculate conditional probability
    if count_rain == 0:  # Avoid division by zero
        return 0
    return count_wet_grass_given_rain / count_rain

# Run simulation
estimated_probability = monte_carlo_simulation(num_samples=10000)
print(f"Estimated P(WetGrass=True | Rain=True): {estimated_probability}")
print("Avinash Pandey -21BCT0179")
