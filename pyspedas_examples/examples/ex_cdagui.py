"""
Instructions on using the cdagui for downloading data from CDAWeb.

Since this is a GUI, only the instructions are printed.
You have to follow these instructions using a python command line.
"""


def ex_cdagui():
    """Instructions on how to use cdagui to download data."""
    # Import pyspedas
    # Run the following import command in a python command line:
    #     from pyspedasimport cdagui
    print("--- In a command line, type the following import command:")
    print("from pyspedas import cdagui")
    # Open the cdagui by typing
    #     x = cdagui()
    print("x = cdagui()")
    # In the GUI window, do the following:
    # Select 'ARTEMIS', select 'Electric Fields (space)'
    # Click the button '1. Find Datasets' and a list of datasets shoulw appear.
    print("--- The cda GUI window should open.")
    print("--- Select 'ARTEMIS', 'Electric Fields (space)'\
 and click '1. Find Datasets'.")
    # Select 'THB_L2_FIT' and click the button '2. Get File List'
    print("--- Select 'THB_L2_FIT' and click '2. Get File List'.")
    # Select the filename, unselect 'Download Only'
    # and click the button '3. Get Data'
    print("--- Select the proper filename, unselect 'Download Only'\
 and click '3. Get Data'.")
    # Click 'Exit' to close the GUI
    print("--- Click 'Exit' to close the GUI.")
    # Type the following on the python command line and press Shift+Enter
    #   import pyspedas
    #   pyspedas.tplot_names()
    # You should get a list of tplot variables loaded.
    print("--- Type the following on the python command line\
 and press Shift+Enter.")
    print("import pyspedas")
    print("pyspedas.tplot_names()")
    print("--- You should get the list of loaded tplot variables.")
    # Type the following to create a plot:
    #   pyspedas.tplot('thb_fgs_dsl')
    print("--- Type the following to create a plot:")
    print("pyspedas.tplot('thb_fgs_dsl')")

    # Return 1 as indication that the example finished without problems.
    return 1


# Run the example code
if __name__ == '__main__':
    ex_cdagui()
