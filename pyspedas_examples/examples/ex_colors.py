"""Colors.

Example of use of colors with pytplot

Download THEMIS data and plot
.
"""

import pyspedas
import pytplot
from pyspedas.utilities.cotrans import cotrans
from pyspedas.utilities.cotrans_lib import submag2geo


def ex_colors():
    """Get state data for THEMIS

    Load position and velocity from THEMIS and plot with different colors.

    Notes
    -----
    IDL SPEDAS contains a more extended example: crib_colors.pro
    """
    trange = ['2007-06-23/00:00:00', '2007-06-23/23:59:59']
    probe = 'a'
    pyspedas.themis.state(probe=probe, trange=trange, time_clip=True)

    # Create line plot with area under the line filled in
    print('Example of line plot')
    pytplot.tplot(['tha_state_pos', 'tha_state_vel', ])

    # Choose a colormap
    #  For list of color maps
    #       https://matplotlib.org/2.0.2/examples/color/colormaps_reference.html
    pytplot.options('tha_state_pos', 'colormap', 'jet')
    # choose colors
    pytplot.options('tha_state_pos', 'colors', ['red', 'green', 'blue'])
    pytplot.tplot(['tha_state_pos'])

   # Return 1 as indication that the example finished without problems.
    return 1

# Run the example code
# ex_gmag()
