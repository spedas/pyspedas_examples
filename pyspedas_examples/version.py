"""
    pySPEDAS and examples version numbers.

Returns
-------
    The version number for the current installation.
"""


def version():
    """Versions of main packages."""

    import pkg_resources

    try:
        ver = pkg_resources.get_distribution("pyspedas_examples").version
        print("pyspedas_examples version: " + ver)
    except pkg_resources.DistributionNotFound:
        print("pyspedas_examples is not installed as a package, version info not available")

    try:
        verp = pkg_resources.get_distribution("pyspedas").version
        print("pyspedas version: " + verp)
    except pkg_resources.DistributionNotFound:
        print("pyspedas is not installed as a package, version info not available")

    try:
        vern = pkg_resources.get_distribution("pytplot-mpl-temp").version
        print("pytplot-mpl-temp version: " + vern)
    except pkg_resources.DistributionNotFound:
        print("pytplot-mpl-temp is not installed as a package, version info not available")

    try:
        vero = pkg_resources.get_distribution("pytplot").version
        print("pytplot (original) version: " + vero)
    except pkg_resources.DistributionNotFound:
        print(
            "pytplot (original) is not installed as a package, version info not available")


# Run the version function directly
if __name__ == '__main__':
    version()
