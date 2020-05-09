"""
Creates a new pytplot object and applies analysis functions.

Create new pytplot variable from your data, and apply analysis functions.
"""

import pyspedas
import pytplot
import numpy
from pyspedas.utilities.time_double import time_float


def ex_create(plot=True):
    """Show how to create and plot pytplot variables."""
    # Delete any existing pytplot variables
    pytplot.del_data()

    # Create a sin wave plot
    a = list(range(0, 101))
    b = [2.0 / 100.0 * numpy.pi * s for s in a]
    c = time_float('2017-01-01')
    x = list()
    y = list()
    for i in range(len(b)):
        x.append(c + 60.0 / (2 * numpy.pi) * 60.0 * b[i])
        y.append(1000.0 * numpy.sin(b[i]))

    # Store data
    pytplot.store_data('sinx', data={'x': x, 'y': y})

    # Apply yclip
    pyspedas.yclip('sinx', -800.0, 800.0)

    # Remove NaN values
    pyspedas.tdeflag('sinx-clip')

    # Interpolate
    pyspedas.tinterpol(['sinx-clip-deflag'], 'sinx', 'quadratic')

    # Plot
    pytplot.ylim('sinx', -1100.0, 1100.0)
    pytplot.ylim('sinx-clip', -1100.0, 1100.0)
    pytplot.ylim('sinx-clip-deflag', -1100.0, 1100.0)
    pytplot.ylim('sinx-clip-deflag-itrp', -1100.0, 1100.0)
    pytplot.tplot_options('title', 'Interpolation example')

    if plot:
        pytplot.tplot(['sinx', 'sinx-clip', 'sinx-clip-deflag',
                       'sinx-clip-deflag-itrp'])

    # Return 1 as indication that the example finished without problems.
    return 1

# Run the example code
# ex_create()
