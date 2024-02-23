import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

def plot(func, generations, range_x, range_y):
    x = np.linspace(*range_x, 1000)
    y = np.linspace(*range_y, 1000)
    X, Y = np.meshgrid(x, y)
    Z = func(X, Y)

    points_lists = []
    for generation in generations:
        x_values = [individual[0] for individual in generation]
        y_values = [individual[1] for individual in generation]
        z_values = [func(x, y) for x, y in zip(x_values, y_values)]
        points_lists.append((x_values, y_values, z_values))
        

    fig = plt.figure(figsize=(10,10))
    ax = fig.add_subplot(111, projection='3d')

    function_surface = ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.6)

    scatter_plots = []
    for points_x, points_y, points_z in points_lists:
        scatter_plot = ax.scatter(points_x, points_y, points_z, color='blue')
        scatter_plots.append(scatter_plot)
        scatter_plot.set_visible(False)

    def animate(frame):
        ax.set_title(f'Generation {frame + 1}')
        if frame > 0:
            scatter_plots[frame - 1].set_visible(False)
        scatter_plots[frame].set_visible(True)
        return scatter_plots

    ani = FuncAnimation(fig, animate, frames=len(scatter_plots), interval=1000)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    plt.show()