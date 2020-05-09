"""
Download and plot THEMIS GMAG data.

Shows how to get the names of GMAG stations and how to download GMAG data
either from a single station or gram a GMAG group.

"""
import pyspedas
import pytplot


def ex_gmag(plot=True):
    """Demonstrate how to use gmag functions."""
    # Delete any existing pytplot variables
    pytplot.del_data()

    # Define a time rage as a list
    trange = ['2015-12-31', '2015-12-31']

    # Get a list of EPO gmag stations
    sites = pyspedas.themis.ground.gmag.gmag_list('epo')

    # Download gmag files and load data into pytplot variables
    pyspedas.themis.gmag(sites=sites, trange=trange)

    # Get a list of loaded sites
    sites_loaded = pyspedas.tnames()

    # Subtract mean values
    pyspedas.subtract_average(sites_loaded, '')

    # Download AE index data
    # pyspedas.load_data('gmag', time_list, ['idx'], '', '')
    pyspedas.themis.gmag(sites='idx', trange=trange)

    # Plot
    sites_loaded = pyspedas.tplot_names()
    pytplot.tplot_options('title', 'EPO GMAG 2015-12-31')

    if plot:
        pytplot.tplot(sites_loaded)

    # Return 1 as indication that the example finished without problems.
    return 1

# Run the example code
# ex_gmag()
