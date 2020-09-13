"""
    pySPEDAS and examples version numbers.

Returns
-------
    The version number for the current installation.
"""


def version():
    """Versions of main packages."""
    import pkg_resources
    ver = pkg_resources.get_distribution("pyspedas_examples").version
    print("pyspedas_examples version: " + ver)
    verp = pkg_resources.get_distribution("pyspedas").version
    print("pyspedas version: " + verp)
    verp = pkg_resources.get_distribution("pytplot").version
    print("pytplot version: " + verp)
