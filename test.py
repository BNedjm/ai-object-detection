import numpy as np
import matplotlib.pyplot as plt

# Example depth map (replace this with your actual depth map)
depth_map = np.random.rand(10, 10)

# Example camera parameters (replace these with your actual camera parameters)
focal_length = 1000  # in pixels
principal_point = (5, 5)  # (x, y) in pixels

# Generate 2D reconstruction
y, x = np.indices(depth_map.shape)

# Perspective projection
world_coordinates = np.stack([x, y, np.ones_like(depth_map)], axis=-1)
image_coordinates = world_coordinates[:, :, :2] * depth_map[:, :, np.newaxis] / focal_length + principal_point

# Display the 2D reconstruction
plt.scatter(image_coordinates[:, :, 0], image_coordinates[:, :, 1], c=depth_map, cmap='viridis')
plt.colorbar()
plt.show()
