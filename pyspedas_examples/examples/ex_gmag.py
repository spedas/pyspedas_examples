"""
Download and plot THEMIS GMAG data.

Shows how to get the names of GMAG stations and how to download GMAG data
either from a single station or a GMAG group.

"""
from pyspedas import del_data, tplot_options, tplot, tplot_names
from pyspedas import subtract_average, tnames
from pyspedas.themis.ground.gmag import gmag, gmag_list


def ex_gmag(plot=True):
    """Demonstrate how to use gmag functions."""
    # Delete any existing tplot variables
    del_data()

    # Define a time rage as a list
    trange = ['2015-12-31', '2015-12-31']

    # Get a list of EPO gmag stations
    sites = gmag_list('epo')

    # Download gmag files and load data into tplot variables
    gmag(sites=sites, trange=trange)

    # Get a list of loaded sites
    sites_loaded = tnames()

    # Subtract mean values
    subtract_average(sites_loaded, '')

    # Download AE index data
    # pyspedas.load_data('gmag', time_list, ['idx'], '', '')
    gmag(sites='idx', trange=trange)

    # Plot
    sites_loaded = tplot_names()
    tplot_options('title', 'EPO GMAG 2015-12-31')

    if plot:
        tplot(sites_loaded)

    # Return 1 as indication that the example finished without problems.
    return 1


# Run the example code
if __name__ == '__main__':
    ex_gmag()
