from matplotlib import pyplot as plt

planets = [
       ("Mercury", 57.91e+6, 2439.7), ("Venus", 108.2e+6, 6051.8), ("Earth", 149.6e+6, 6371),
       ("Mars", 227.9e+6, 3389.5), ("Jupiter", 778.5e+6, 69911), ("Saturn", 1.434e+9, 58232),
       ("Uranus", 2.871e+9, 25362), ("Neptune", 4.495e+9, 24622)
]

#
# - extract plot data
#

radius = [planet[2] for planet in planets]
names = [planet[0] for planet in planets]
color = ["red", "orange", "blue", "green", "yellow", "indigo", "violet", "purple"]

#
# plot
#

plt.pie(radius, colors=color, startangle=90, shadow=True, explode=(0, 0, 0.1, 0, 0, 0, 0, 0))

for idx in (range(0, len(planets))):
    plt.scatter([], [], c=color[idx], s=100, label=names[idx])

plt.legend(loc=(1, .6))

plt.title('Planet Radius')
plt.show()