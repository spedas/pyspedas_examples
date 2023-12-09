"""Wavelet example."""

import numpy as np
import pytplot
from pyspedas import time_float
from pyspedas.analysis.wavelet import wavelet


def ex_wavelet(plot=True):
    """Demonstrates how to use wavelets with pyspedas."""
    # Delete any existing pytplot variables
    pytplot.del_data()

    # Create a pytplot variable.
    t = np.arange(4000.)
    y = np.sin(2*np.pi*t/32.)
    y2 = np.sin(2*np.pi*t/64.)
    y[1000:3000] = y2[1000:3000]
    var = 'sin_wav'
    time = time_float('2010-01-01') + 10*t
    pytplot.store_data(var, data={'x': time, 'y': y})

    # Complex wavelet transformation.
    powervar = wavelet(var, wavename='cmorl0.5-1.0')
    # Also try the following and compare:
    # powervar = wavelet(var, wavename='gaus1')
    pvar = powervar[0]

    # Plot.
    if plot:
        pytplot.tplot([var, pvar])

    return 1


# Run the example code
if __name__ == '__main__':
    ex_wavelet()
