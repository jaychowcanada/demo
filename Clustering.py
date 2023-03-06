import numpy as np
from sklearn.cluster import KMeans

# Load dataset
X = np.array([[1, 2], [1, 4], [1, 0],
              [4, 2], [4, 4], [4, 0]])

# Define number of clusters
kmeans = KMeans(n_clusters=2)

# Fit model to data
kmeans.fit(X)

# Predict clusters for data points
y_pred = kmeans.predict(X)

# Print predicted cluster labels
print(y_pred)