"""
Contains unsupervised learning functions to enable image_segmentation.
"""

# Author: Viraj Vaitha

# Import Libaries
import sklearn
from sklearn.cluster import KMeans
import numpy as np

def cluster_image(n_clusters:int ,input_array: np.array) -> np.array:
    X = input_array.reshape(-1, 3)

    # training kmeans model
    kmeans = KMeans(n_clusters= n_clusters, random_state=42).fit(X)
    
    # Replace pixel rgb values with the rgb value of it's closest centroid
    segmented_img = kmeans.cluster_centers_[kmeans.labels_]
    segmented_img = segmented_img.reshape(input_array.shape)
    return segmented_img
