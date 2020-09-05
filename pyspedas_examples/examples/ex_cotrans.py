"""Coordinate transformations.

See also: http://spedas.org/wiki/index.php?title=Cotrans
"""

import pyspedas
import pytplot
from pyspedas.utilities.cotrans import cotrans
from pyspedas.utilities.cotrans_lib import submag2geo


def ex_cotrans():
    """Transform state data for THEMIS from GEI to GSE.

    Load position and velocity from THEMIS.
    Transform the coordinates to GSE and plot.

    Notes
    -----
    IDL SPEDAS contains a more extended example: thm_crib_contrans.pro
    """
    trange = ['2007-06-23/00:00:00', '2007-06-23/23:59:59']
    probe = 'a'
    pos_in = "tha_pos"
    pos_out = "tha_pos_gse"
    vel_in = "tha_vel"
    vel_out = "tha_vel_gse"
    pyspedas.themis.state(probe=probe, trange=trange, time_clip=True,
                          varnames=[pos_in, vel_in])

    # Coordinate transformation.
    cotrans(name_in=pos_in, name_out=pos_out, coord_in="gei", coord_out="gse")
    cotrans(name_in=vel_in, name_out=vel_out, coord_in="gei", coord_out="gse")

    # Plot.
    pytplot.tplot_options('title', 'Themis pos and vel in GEI and GSE')
    pytplot.options(pos_in, 'ytitle', pos_in)
    pytplot.options(pos_out, 'ytitle', pos_out)
    pytplot.options(vel_in, 'ytitle', vel_in)
    pytplot.options(vel_out, 'ytitle', vel_out)
    pytplot.tplot([pos_in, vel_in, pos_out, vel_out])

    # Return 1 as indication that the example finished without problems.
    return 1


def ex_cotrans1():
    """Define data and times and apply submag2geo.

    Notes
    -----
    To compare with IDL SPEDAS, use the following IDL code:

    cotrans_lib
    d = [[245.0, -102.0, 251.0], [775.0, 10.0, -10], $
         [121.0, 545.0, -1.0], [304.65, -205.3, 856.1], $
         [464.34, -561.55, -356.22]]
    data_in = transpose(d)
    t = [1577112800, 1577308800, 1577598800, 1577608800, 1577998800]
    t1 = time_struct(t)
    subMAG2GEO, t1, data_in, dout
    print, transpose(dout)
    """
    # Define data and times.
    d = [[245.0, -102.0, 251.0], [775.0, 10.0, -10],
         [121.0, 545.0, -1.0], [304.65, -205.3, 856.1],
         [464.34, -561.55, -356.22]]
    print("Input data (MAG):")
    print(d)
    t = [1577112800, 1577308800, 1577598800, 1577608800, 1577998800]
    # Coordinate transformation MAG to GEO.
    geo = submag2geo(t, d)
    print("Input data (GEO):")
    print(geo)

    # Return 1 as indication that the example finished without problems.
    return 1


# Run the example code
# ex_cotrans()
