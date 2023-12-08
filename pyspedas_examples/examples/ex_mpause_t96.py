"""
This example loads position data for THEMIS thd probe for a specified time range,
converts the position data from GEI to GSM coordinates,
calls the mpause_t96 function with the position data, and plots the magnetopause.

This is similar to the IDL example crib_magnetopause.pro (second part).
"""

from pyspedas.themis import state
from pyspedas.cotrans.cotrans import cotrans
from pyspedas.utilities.mpause_t96 import mpause_t96
import matplotlib.pyplot as plt
from pytplot import get_data


def ex_mpause_t96():

    # Set the date and load one day of data
    date_start = '2019-01-05/00:00:00'
    date_end = '2019-01-06/00:00:00'

    # Load position data for THEMIS thd probe for the specified time range
    state(trange=[date_start, date_end], probe='d', get_support_data=True)

    # Transform the position data from GEI to GSM coordinates
    cotrans(name_in='thd_pos', name_out='thd_pos_gsm',
            coord_in='gei', coord_out='gsm')

    # Get the position data in GSM coordinates
    pos_gsm_data = get_data('thd_pos_gsm')

    # Convert position from kilometers to Earth radii
    pos_gsm = pos_gsm_data.y / 6378.0

    # Define solar wind dynamic pressure
    dynp = 2.0

    # Call the mpause_t96 function with the position data
    xmgnp, ymgnp, zmgnp, id, distan = mpause_t96(
        pd=dynp, xgsm=pos_gsm[:, 0], ygsm=pos_gsm[:, 1], zgsm=pos_gsm[:, 2])

    # Plot xmgnp vs ymgnp
    plt.figure()
    plt.plot(xmgnp, ymgnp)
    plt.xlim(20, -60)
    plt.ylim(-30, 30)
    plt.xlabel('X (Re)')
    plt.ylabel('Y (Re)')
    plt.title('Magnetopause Boundary')
    plt.grid(True)
    plt.show()

# To run this function, uncomment the following line:
# ex_mpause_t96()
