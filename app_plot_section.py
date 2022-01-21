#!/usr/bin/env python3                                                                                                    

import matplotlib.pyplot as plt
import numpy as np
from BoundingBox import BoundingBox
from fibonacci_sphere import fibonacci_sphere_section
from mpl_toolkits.mplot3d import Axes3D

# initialize bounding box
bbox_full = np.array([-90.0, 90.0, -180.0, 180.0])
bbox_full = np.deg2rad(bbox_full) # convert from degrees to radians
bbox_full = BoundingBox(bbox_full[0], bbox_full[1], bbox_full[2], bbox_full[3])

lat_min, lat_max, lon_min, lon_max = 10.0, 40.0, 30.0, 60.0
bbox = np.array([lat_min, lat_max, lon_min, lon_max])
bbox = np.deg2rad(bbox) # convert from degrees to radians
bbox = BoundingBox(bbox[0], bbox[1], bbox[2], bbox[3])

# fibonacci sphere
num_points = 1000
xf, yf, zf = fibonacci_sphere_section(num_points, bbox_full)
x, y, z = fibonacci_sphere_section(num_points*10, bbox)

# Display points in a scatter plot                                                                                       
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_title("min lat: {:.0f}°, max lat: {:.0f}°, min lon: {:.0f}°, min lon: {:.0f}°\n {} points with density of a {} points sphere".format(lat_min, lat_max, lon_min, lon_max, x.size, num_points*10))
ax.scatter(xf, yf, zf, alpha=0.5)
ax.scatter(x, y, z, color="red")

ax.set_box_aspect([1,1,1])

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()