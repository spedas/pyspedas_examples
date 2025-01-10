"""
Example of plotting a spectrogram.

Download THEMIS data and plot two panels, one with line plot and
one with a spectrogram.

"""

from pyspedas import del_data, options, tplot_options, ylim, tplot
from pyspedas.projects.themis import state, sst


def ex_spectra(plot=True):
    """Download THEMIS data and create a plot."""
    # Delete any existing tplot variables
    del_data()

    # Download THEMIS data for 2015-12-31
    time_range = ['2015-12-31 00:00:00', '2015-12-31 23:59:59']
    state(probe='a', trange=time_range)
    sst(probe='a', trange=time_range, varnames=['tha_psif_en_eflux'])

    # Specify options
    ylim('tha_pos', -23000.0, 81000.0)
    ylim('tha_psif_en_eflux', 10000.0, 4000000.0)
    options('tha_psif_en_eflux', 'colormap', 'jet')
    tplot_options('title', 'tha 2015-12-31')

    # Plot line and spectrogram
    if plot:
        tplot(['tha_pos', 'tha_psif_en_eflux'])

    # Return 1 as indication that the example finished without problems.
    return 1


# Run the example code
if __name__ == '__main__':
    ex_spectra()
