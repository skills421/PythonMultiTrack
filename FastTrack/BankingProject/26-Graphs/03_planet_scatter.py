from matplotlib import pyplot as plt

planets = [
       ("Mercury", 57.91e+6, 2439.7), ("Venus", 108.2e+6, 6051.8), ("Earth", 149.6e+6, 6371),
       ("Mars", 227.9e+6, 3389.5), ("Jupiter", 778.5e+6, 69911), ("Saturn", 1.434e+9, 58232),
       ("Uranus", 2.871e+9, 25362), ("Neptune", 4.495e+9, 24622)
]

#
# extract data to plot
#

names = [planet[0] for planet in planets]
distance_from_sun = [planet[1] for planet in planets]
radius = [planet[2] for planet in planets]
size = [radius/50 for radius in radius]
color = ["red", "orange", "blue", "green", "yellow", "indigo", "violet", "purple"]

#
# plot
#

plt.scatter(distance_from_sun, radius, s=size, c=color)

#
# labels
#

for idx in range(0, len(planets)):
    plt.scatter([], [], c=color[idx], s=size[0], label=names[idx])

plt.legend()

plt.title('Scatter graph of planets radius against distance from sun')
plt.ylabel('radius (km)')
plt.xlabel('distance from sun (bn km)')

plt.show()