"""
Example of deriv_data.

One example with GMAG variables, and one example with sinx variable.

"""
import numpy as np
import pyspedas
import pyspedas
from pyspedas.analysis.deriv_data import deriv_data


def ex_deriv(plot=True):
    """Find the derivative of a GMAG variable."""
    # Derivative of data
    pyspedas.del_data()

    # Define a time rage as a list
    trange = ['2007-03-23', '2007-03-23']

    # Download gmag files and load data into pyspedas variables
    sites = ['ccnv']
    var = 'thg_mag_ccnv'
    pyspedas.themis.gmag(sites=sites, trange=trange, varnames=[var])
    # pyspedas.tplot_options('title', 'GMAG data, thg_mag_ccnv 2007-03-23')
    pyspedas.subtract_average(var, median=1)
    var += '-m'

    # Five minute average
    deriv_data(var)
    # pyspedas.options(var, 'ytitle', var)
    # pyspedas.options(var + '-der', 'ytitle', var + '-der')
    if plot:
        pyspedas.tplot([var, var + '-der'])

    # Return 1 as indication that the example finished without problems.
    return 1


def ex_deriv1(plot=True):
    """Find the derivative of sinx."""
    # Delete any existing tplot variables
    pyspedas.del_data()

    # Create a sin wave plot
    a = list(range(0, 101))
    b = [2.0 / 100.0 * np.pi * s for s in a]
    c = pyspedas.time_float('2017-01-01')
    x = list()
    y = list()
    for i in range(len(b)):
        x.append(c + 60.0 / (2 * np.pi) * 60.0 * b[i])
        y.append(1000.0 * np.sin(b[i]))

    # Store data
    pyspedas.store_data('sinx', data={'x': x, 'y': y})

    var = 'sinx'
    deriv_data(var)
    if plot:
        pyspedas.tplot([var, var + '-der'])

    return 1


# Run the example code
if __name__ == '__main__':
    ex_deriv()
    ex_deriv1()
