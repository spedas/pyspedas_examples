"""
Applies the tsmooth function using pytplot only.

This can be compared to the similar IDL function.

"""

from pytplot import store_data, get_data, tplot, tsmooth, options


def ex_smooth(plot=True):
    """Smooth data."""
    t = [1., 2., 3., 4., 5., 6., 7., 8., 9., 10., 11., 12.]
    y = [3., 5., 8., 15., 20., 1., 2., 3., 4., 5., 6., 4.]

    store_data('original', data={'x': t, 'y': y})
    tsmooth('original', width=5, new_names='smooth', preserve_nans=1)
    options('smooth', 'ytitle', 'smooth')

    if plot:
        tplot(['original', 'smooth'])

    d0 = get_data('original')
    print('Original data: ', d0[1])
    d = get_data('smooth')
    print('Smooth data: ', d[1])

    """
    Results:
    Original data:[ 3., 5., 8.,   15., 20., 1.,  2., 3., 4., 5.,  6.,  4.]
    Smooth data:  [ 3., 5., 10.2, 9.8, 9.2, 8.2  6., 3., 4., 4.4, 6.,  4.]
    """
    # Return 1 as indication that the example finished without problems.
    return 1


# Run the example code
if __name__ == '__main__':
    ex_smooth()
