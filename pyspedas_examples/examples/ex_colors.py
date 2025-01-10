"""
Example of use of line colors with pyspedas
"""
from pyspedas import tplot, options
from pyspedas.projects.themis import state


def ex_colors(plot=True):
    """Get state data for THEMIS

    Load position and velocity from THEMIS and plot with different colors.

    Notes
    -----
    IDL SPEDAS contains a more extended example: crib_colors.pro
    """
    trange = ['2017-06-23/00:00:00', '2017-06-23/23:59:59']
    probe = 'a'
    state(probe=probe, trange=trange)

    # Create line plot with area under the line filled in
    print('Example of line plot')
    tplot(['tha_pos', 'tha_vel', ])

    # choose line colors
    options('tha_pos', 'color', ['black', 'magenta', 'cyan'])
    if plot:
        tplot(['tha_pos', 'tha_vel', ])

   # Return 1 as indication that the example finished without problems.
    return 1


# Run the example code
if __name__ == '__main__':
    ex_colors()
