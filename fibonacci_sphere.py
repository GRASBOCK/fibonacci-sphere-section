from math import ceil, floor
import numpy as np
from BoundingBox import BoundingBox

def fibonacci_sphere_section(num_points_whole_sphere: int, bbox: BoundingBox):
    lat_min, lat_max, lon_min, lon_max = bbox.lat_min, bbox.lat_max, bbox.lon_min, bbox.lon_max
    #print("lat_min: {}, lat_max: {}, lon_min: {}, lon_max: {}".format(lat_min, lat_max, lon_min, lon_max))

    ga = (3 - np.sqrt(5)) * np.pi # golden angle

    repeat = np.pi*2/ga # after how many indices the 2 pi is reached

    z_step = 2.0/num_points_whole_sphere
    z_min_bound = z_step-1.0 # minimum z
    z_max_bound = 1.0 - z_step # maximum z

    z_min = np.sin(lat_min) 
    z_max = np.sin(lat_max)

    if z_min < z_min_bound:
        z_min = z_min_bound
    if z_max > z_max_bound:
        z_max = z_max_bound
    
    # linear interpolation
    linInterp = lambda x1, x2, y1, y2, x: (y2-y1)/(x2-x1)*(x-x1)

    i_min = linInterp(z_min_bound, z_max_bound, 0.0, float(num_points_whole_sphere), z_min) # smallest i where z is within bounding box latitude
    i_max = linInterp(z_min_bound, z_max_bound, 0.0, float(num_points_whole_sphere), z_max) # biggest i where z is within bounding box latitude

    circulations = ceil((i_max - i_min)/repeat) # number of circulations
    
    relative_begin = linInterp(0.0, np.pi*2, 0.0, repeat, lon_min) # relative index to start of bounding box longitude
    relative_end = linInterp(0.0, np.pi*2, 0.0, repeat, lon_max) # relative index to end of bounding box longitude

    theta_offset = i_min*ga # this is needed, otherwise the origin jumps with the number of points
    theta = []
    z = []
    for r in range(circulations):
        offset = repeat*r + i_min

        i_start = ceil(offset + relative_begin)
        i_end = int(offset + relative_end)

        if i_end >= num_points_whole_sphere: # prevent overflow
            i_end = num_points_whole_sphere -1

        indices = range(i_start, i_end+1) # all indices within the bounding box for the current circulation. can be empty

        #print("r: {r:4d}, o: {o:.3f}, s: {s:.3f}, e: {e:.3f}".format(r=r, o=offset, s=offset + relative_begin, e=offset + relative_end), indices, list(indices))
        
        for i in indices:
            theta.append(ga*i-theta_offset)
            z.append(z_step-1.0 + z_step*i)

    theta = np.array(theta)
    z = np.array(z)

    # a list of the radii at each height step of the unit circle 
    radius = np.sqrt(1 - z * z)

    # Determine where xy fall on the sphere, given the azimuthal and polar angles 
    y = radius * np.sin(theta)
    x = radius * np.cos(theta)

    return x, y, z