import numpy as np
import pandas as pd

# Define the number of samples
num_samples = 1000

# Generate random data for each column
weather_conditions = np.random.randint(1, 4, size=num_samples)  # Assuming 1: sunny, 2: rainy, 3: snowy
road_type = np.random.randint(1, 3, size=num_samples)  # Assuming 1: highway, 2: local road
time_of_day = np.random.randint(1, 4, size=num_samples)  # Assuming 1: morning, 2: afternoon, 3: night
vehicle_speed = np.random.randint(30, 100, size=num_samples)  # Assuming speed in km/h
accident_severity = np.random.randint(1, 4, size=num_samples)  # Assuming 1: minor, 2: moderate, 3: severe

# Create a DataFrame using the generated data
data = pd.DataFrame({
    'weather': weather_conditions,
    'road_type': road_type,
    'time_of_day': time_of_day,
    'vehicle_speed': vehicle_speed,
    'accident_severity': accident_severity
})

# Save the DataFrame to a CSV file
data.to_csv('accident_data.csv', index=False)

# Display the first few rows of the dataset
print(data.head())
