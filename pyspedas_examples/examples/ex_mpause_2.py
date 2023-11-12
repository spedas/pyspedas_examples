"""
This example generates a plot of the magnetopause locations using the mpause_2 function from the pyspedas.utilities module.
The plot includes grid, labels, and title. The x-axis is inverted to match the IDL behavior.

This is similar to the IDL example crib_magnetopause.pro (first part).
"""

import matplotlib.pyplot as plt
from pyspedas.utilities.mpause_2 import mpause_2


def ex_mpause_2():

    # Call the function without parameters to use default values
    xmp, ymp = mpause_2()

    # Set the range for the axes
    x_limits = (-300, 100)
    y_limits = (-100, 100)

    # Create the plot
    plt.figure()
    plt.plot(xmp, ymp)

    # Set the limits of x and y axes
    plt.xlim(x_limits)
    plt.ylim(y_limits)

    # Invert the x-axis to match the IDL behavior
    plt.gca().invert_xaxis()

    # Add grid, labels, and title
    plt.grid(True)
    plt.xlabel("XMP")
    plt.ylabel("YMP")
    plt.title("Magnetopause Locations")

    # Display the plot
    plt.show()


# To run this function, uncomment the following line:
ex_mpause_2()
