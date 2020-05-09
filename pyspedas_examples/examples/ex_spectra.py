"""
Example of plotting a spectrogram.

Download THEMIS data and plot two panels, one with line plot and
one with a spectrogram.

"""

import pyspedas
import pytplot


def ex_spectra(plot=True):
    """Download THEMIS data and create a plot."""
    # Delete any existing pytplot variables
    pytplot.del_data()

    # Download THEMIS data for 2015-12-31
    # pyspedas.load_data('themis', ['2015-12-31'], ['tha'], 'state', 'l1')
    # pyspedas.load_data('themis', ['2015-12-31'], ['tha'], 'sst', 'l2')
    time_range = ['2015-12-31 00:00:00', '2015-12-31 23:59:59']
    pyspedas.themis.state(probe='a', trange=time_range)
    pyspedas.themis.sst(probe='a', trange=time_range,
                        varnames=['tha_psif_en_eflux'])

    # Specify options
    pytplot.ylim('tha_pos', -23000.0, 81000.0)
    pytplot.ylim('tha_psif_en_eflux', 10000.0, 4000000.0)
    pytplot.options('tha_psif_en_eflux', 'colormap', 'jet')
    pytplot.tplot_options('title', 'tha 2015-12-31')

    # Plot line and spectrogram
    if plot:
        pytplot.tplot(['tha_pos', 'tha_psif_en_eflux'])

    # Return 1 as indication that the example finished without problems.
    return 1

# Run the example code
# ex_spectra()
