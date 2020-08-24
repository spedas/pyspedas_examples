"""
Applies cotrans transformations.

The same code is also provided for the IDL spedas.
"""

from pyspedas.utilities.cotrans_lib import submag2geo


def ex_cotrans():
    """Define data and times and apply submag2geo.

    Notes
    -----
    To compare with IDL, use the following:

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
    d = [[245.0, -102.0, 251.0], [775.0, 10.0, -10],
         [121.0, 545.0, -1.0], [304.65, -205.3, 856.1],
         [464.34, -561.55, -356.22]]
    print("Input data (MAG):")
    print(d)
    t = [1577112800, 1577308800, 1577598800, 1577608800, 1577998800]
    geo = submag2geo(t, d)
    print("Input data (GEO):")
    print(geo)
    # Return 1 as indication that the example finished without problems.
    return 1


# Run the example code
# ex_cotrans()
