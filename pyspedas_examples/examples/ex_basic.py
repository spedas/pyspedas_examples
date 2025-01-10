"""
Basic example to verify that the installation works correctly.

Download THEMIS data and plot it.
"""

from pyspedas import del_data, get_data, store_data, tplot, tplot_options, options, ylim
from pyspedas.themis import state


def ex_basic(plot=True):
    """Download and plot THEMIS data."""
    # Delete any existing tplot variables
    del_data()

    # Download THEMIS state data for 2015-12-31
    time_range = ['2015-12-31 00:00:00', '2016-01-01 12:00:00']
    state(probe='a', trange=time_range, time_clip=True)

    # Get data into python variables
    alldata = get_data("tha_pos")
    time = alldata[0]
    data = alldata[1]

    # Here we could work on the data before saving a new tplot variable.
    # For example, we could convert the data to km:
    data = data / 1000.0

    # Store a new tplot variable
    store_data("tha_position", data={'x': time, 'y': data})

    # Define the y-axis limits
    options('tha_pos', 'yrange', [-100000.0, 100000.0])
    options('tha_vel', 'yrange', [-8.0, 12.0])

    # Give a title to the plot and labels for the y-axis panels.
    tplot_options('title', 'tha position and velocity, 2015-12-31')
    options('tha_pos', 'ytitle', 'Position')
    options('tha_vel', 'ytitle', 'Velocity')
    options('tha_position', 'ytitle', 'Position')
    options('tha_position', 'ysubtitle', '[km]')

    # Plot position and velocity using the matplotlib library
    if plot:
        tplot(["tha_pos", "tha_position", "tha_vel"])

    # Return 1 as indication that the example finished without problems.
    return 1


# Run the example code
if __name__ == '__main__':
    ex_basic()
