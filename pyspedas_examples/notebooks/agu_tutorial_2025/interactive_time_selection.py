def ctime_example():
    import pyspedas
    from pyspedas import tplot, ctime, time_string

    # Load some data to plot

    pyspedas.projects.themis.state(probe='a',trange=['2007-03-23','2007-03-30'])

    # Plot the data, saving the matplotlib fig and axes objects

    # ctime works best if display is set to false in the tplot call.  Use an explicit call to fig.show()
    # after tplot returns the plot objects, then call ctime to start the interactive loop.

    fig,axes = tplot('tha_pos tha_vel',return_plot_objects=True, display=False)
    fig.show()
    selected_times = ctime(fig)

    print(selected_times)
    print(time_string(selected_times))

if __name__ == "__main__":
    ctime_example()
