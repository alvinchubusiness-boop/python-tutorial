import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import numpy as np

# 1. Reading the image (PNGs usually load as floats 0.0 to 1.0)
image = plt.imread('cat.png')
h, w, d = image.shape

# 2. Re-organize pixels as 2D array
# If the PNG has 4 channels (RGBA), we slice it to keep only 3 (RGB)
pixels = image.reshape(-1, d)[:, :3]

# 3. Clustering (k=10)
# This finds the 10 most prominent colors in the image
kmeans = KMeans(n_clusters=10, random_state=42, n_init=10)
labels = kmeans.fit_predict(pixels)
centers = kmeans.cluster_centers_

# 4. Reconstruct the image using cluster centers
compressed_pixels = centers[labels]
compressed_image = compressed_pixels.reshape(h, w, 3)

# 5. Save the image
plt.imsave('compressed.png', compressed_image)

# Optional: Display the results
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1); plt.imshow(image); plt.title('Original')
plt.subplot(1, 2, 2); plt.imshow(compressed_image); plt.title('Compressed (k=10)')
plt.show()