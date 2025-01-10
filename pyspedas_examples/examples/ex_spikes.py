"""
Example of removing spikes from data.

This module demonstrates how to use the function clean_spikes.

"""
import random
import pyspedas
from pyspedas import clean_spikes, del_data, tplot_options, data_quants, tplot, tplot_names
from pyspedas.themis import gmag


def ex_spikes(plot=True):
    """Load GMAG data and show how to remove spikes."""
    # Delete any existing tplot variables.
    del_data()

    # Define a time rage as a list
    trange = ['2007-03-23', '2007-03-23']

    # Download gmag files and load data into tplot variables.
    sites = ['ccnv']
    var = 'thg_mag_ccnv'
    gmag(sites=sites, trange=trange, varnames=[var])
    tplot_options('title', 'GMAG data, thg_mag_ccnv, 2007-03-23')

    # Add spikes to data.
    data = pyspedas.data_quants[var].values
    dlen = len(data)
    for i in range(1, 16):
        s = (1 if random.random() < 0.5 else -1)
        p1 = int(i*dlen/16)
        data[p1, 0] = s * i * 40000
        data[p1+2000, 1] = s * i * 30000
        data[p1+4000, 2] = s * i * 20000

    pyspedas.data_quants[var].values = data

    # Clean spikes.
    clean_spikes(var, sub_avg=True)

    # Plot all variables.
    if plot:
        tplot(tplot_names())

    # Return 1 as indication that the example finished without problems.
    return 1


# Run the example code
if __name__ == '__main__':
    ex_spikes()
