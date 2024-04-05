import numpy as np
import matplotlib.pyplot as plt

# Parameters
t = np.linspace(0, 2 * np.pi, 360)  # Parameter t going from 0 to 2*pi
longitudes = np.linspace(-180, 180, 360)  # Generate 360 longitudes from -180 to 180
amplitude = 45  # Max amplitude of the sine wave, keeping latitudes within [-90, 90]
lon_amplitude = 180  # Amplitude for longitude, adjusted to span across the globe
frequency = 2  # Frequency of the sine wave

# Generate latitudes using the sine function
latitudes = amplitude * np.sin(np.radians(longitudes) * frequency)
longitudes = lon_amplitude * np.cos(t * frequency)

# Plotting for visualization
plt.figure(figsize=(10, 5))
plt.scatter(longitudes, latitudes, c=t, cmap='viridis', label='Wave-like Path')  # Color mapped by parameter t
plt.colorbar(label='Parameter t')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Wave-like Path Across Globe')
plt.grid(True)
plt.axhline(0, color='black', lw=0.5)
plt.axvline(0, color='black', lw=0.5)
plt.legend()
plt.show()
