import matplotlib.pyplot as plt
from random_walk import RandomWalk

# Keep making new walks, as long as the program is acitve
while True:
    # Make a random walk
    rw = RandomWalk()
    rw.fill_walk()

    plt.style.use("dark_background")
    fig, ax = plt.subplots()
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
               edgecolors="none", s=15)
    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == "n":
        break

# x_values = range(1, 1001)
# y_values = [x**2 for x in x_values]
#
# plt.style.use('dark_background')
# fig, ax = plt.subplots()
# ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)
#
#
# # Set chart title and label axes.
# ax.set_title("Square Numbers", fontsize=24)
# ax.set_xlabel("Value", fontsize=14)
# ax.set_ylabel("Square of Value", fontsize=14)
#
# # Set size of thick labels.
# ax.tick_params(axis="both", which="major", labelsize=14)
#
# # Set the range for each axis
# ax.axis([0, 1100, 0, 1100000])
# # ax.plot(squares)
# plt.savefig("square_plot.png", bbox_inches="tight")