#!/usr/bin/env python3                                                                                                    

import argparse
import matplotlib.pyplot as plt
import numpy as np
from BoundingBox import BoundingBox
from fibonacci_sphere import fibonacci_sphere_section

# parse command line arguments
parser = argparse.ArgumentParser(description = 'fibonacci sphere')                       
parser.add_argument('numpts', type=int, help='number of points/2 to distribute across spherical cap')
parser.add_argument('latmin', type=float, help='minimum latitude in deg')
parser.add_argument('latmax', type=float, help='maximum latitude in deg')
parser.add_argument('lonmin', type=float, help='minimum longitude in deg')
parser.add_argument('lonmax', type=float, help='maximum longitude in deg')
args = parser.parse_args()

# initialize bounding box
bbox = np.array([args.latmin, args.latmax, args.lonmin, args.lonmax])
bbox = np.deg2rad(bbox) # convert from degrees to radians
bbox = BoundingBox(bbox[0], bbox[1], bbox[2], bbox[3])

# fibonacci sphere
x, y, z = fibonacci_sphere_section(args.numpts, bbox)

# Display points in a scatter plot                                                                                       
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_title("min lat: {:.3f}°, max lat: {:.3f}°, min lon: {:.3f}°, min lon: {:.3f}°\n {} points; the whole sphere has {}".format(args.latmin, args.latmax, args.lonmin, args.lonmax, x.size, args.numpts))
ax.scatter(x, y, z, color="red")

# uncomment if you want to fix limits of the axis
#ax.set_xlim(-1, 1)
#ax.set_ylim(-1, 1)
#ax.set_zlim(-1, 1)

ax.set_box_aspect([1,1,1])

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.tight_layout()

plt.show()