'''A prism is an important member of the polyhedron family that
 has congruent polygons at the base and top.
 The other faces of a prism are parallelograms are called lateral faces. 
 It means that a prism does not have a curved face. 
 A prism has the same cross-section all along its length. 
 The prisms are named depending upon their cross-sections. 
 The most common example of a prism is a metallic nut.
'''
'''
There are different types of prisms based on the shape of the base of a prism: 

Triangular prisms,
Square prisms, 
Rectangular prisms, 
Pentagonal prisms, 
Hexagonal prisms, etc.
Trapezoidal prism
A square prism is a prism that has a square base.
All the cubes are actually square prisms






'''
# Import libraries
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


# Create axis
axes = [1, 1, 4]

# Create Data
data = np.ones(axes)

# Control Transparency
alpha = 0.9

# Control colour
colors = np.empty(axes + [4], dtype=np.float32)

colors[:] = [1, 0, 0, alpha] # red

# Plot figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Voxels is used to customizations of the
# sizes, positions and colors.
ax.voxels(data, facecolors=colors)

plt.show()