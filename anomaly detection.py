import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# Generate synthetic data with anomalies
np.random.seed(0)
normal_data = np.random.normal(0, 1, size=(1000, 10))  # Normal data
anomalous_data = np.random.normal(5, 2, size=(50, 10))   # Anomalous data

# Combine normal and anomalous data
data = np.vstack((normal_data, anomalous_data))

# Shuffle the data
np.random.shuffle(data)

# Split the data into training and testing sets
train_data = data[:900]
test_data = data[900:]

# Build a simple autoencoder
input_dim = 10
encoding_dim = 5

autoencoder = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(input_dim,)),
    tf.keras.layers.Dense(encoding_dim, activation='relu'),
    tf.keras.layers.Dense(input_dim, activation='sigmoid')
])

autoencoder.compile(optimizer='adam', loss='mse')

# Train the autoencoder
autoencoder.fit(train_data, train_data, epochs=50, batch_size=32, validation_data=(test_data, test_data))

# Calculate reconstruction errors for test data
reconstructed_data = autoencoder.predict(test_data)
mse = np.mean(np.square(test_data - reconstructed_data), axis=-1)

# Set an anomaly threshold
mean_error = np.mean(mse)
std_error = np.std(mse)
threshold = mean_error + 2 * std_error  # Adjust the multiplier as needed

# Detect anomalies using the chosen threshold
anomalies = mse > threshold

# Print the indices of anomalous data points
print("Anomalous data indices:")
print(np.where(anomalies))

# Plot the reconstruction errors
plt.figure(figsize=(12, 6))
plt.plot(mse, marker='o', linestyle='')
plt.axhline(y=threshold, color='r', linestyle='--', label='Threshold')
plt.title('Reconstruction Errors')
plt.xlabel('Data Point Index')
plt.ylabel('Mean Squared Error')
plt.legend()
plt.show()
