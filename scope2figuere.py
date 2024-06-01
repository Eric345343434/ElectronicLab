from numpy import genfromtxt
import matplotlib.pyplot as plt


# Read the CSV data
def plot_data_3(Data):
    my_data = genfromtxt(Data, delimiter=",", skip_header=1)

    plt.plot(my_data[:,0], my_data[:,1])
    plt.plot(my_data[:,0], my_data[:,2])
    plt.plot(my_data[:,0], my_data[:,3])
    plt.ylabel("U / V")
    plt.xlabel("t / s")
    plt.show()


def plot_data_2(Data):
    my_data = genfromtxt(Data, delimiter=",", skip_header=1)

    plt.plot(my_data[:,0], my_data[:,1])
    plt.plot(my_data[:,0], my_data[:,2])
    plt.ylabel("U / V")
    plt.xlabel("t / s")
    plt.show()



