"""
Example of using analysis functions.

Download THEMIS data, subtract average, and plot it.

"""

from pyspedas import del_data, subtract_average, subtract_median, tplot
from pyspedas.themis import state


def ex_analysis(plot=True):
    """Create a plot with THEMIS data."""
    # Delete any existing tplot variables
    del_data()

    # Download THEMIS state data for 2015-12-31
    time_range = ['2015-12-31 00:00:00', '2015-12-31 23:59:59']
    state(probe='a', trange=time_range)

    # Use some analysis functions on tplot variables
    subtract_average('tha_pos')
    subtract_median('tha_pos')

    # Plot
    if plot:
        tplot(["tha_pos", "tha_pos-d", "tha_pos-m"])

    # Return 1 as indication that the example finished without problems.
    return 1


# Run the example code
if __name__ == '__main__':
    ex_analysis()
