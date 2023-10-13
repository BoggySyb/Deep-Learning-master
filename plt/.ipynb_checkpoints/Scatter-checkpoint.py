import matplotlib.pyplot as plt

# 散点图绘制
class Scatter:


    def show(self, x, y, xlabel="X", ylabel="Y", title=""):
        # Plot the data points
        plt.scatter(x, y)
        # Set the title
        plt.title(title)
        # Set the y-axis label
        plt.ylabel(ylabel)
        # Set the x-axis label
        plt.xlabel(xlabel)
        plt.show()