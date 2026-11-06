"""
    pySPEDAS and examples version numbers.

Returns
-------
    The version number for the current installation.
"""
# We don't want to shadow the importlib version() with pyspedas(version)
from importlib.metadata import version as imp_version
from importlib.metadata import PackageNotFoundError


def version():
    """Versions of main packages."""


    try:
        ver = imp_version("pyspedas_examples")
    except PackageNotFoundError:
        ver = 'bleeding edge'
    print("pyspedas_examples version: " + ver)

    try:
        ver = imp_version("pyspedas")
    except PackageNotFoundError:
        ver = 'bleeding edge'
    print("pyspedas version: " + ver)

    try:
        ver = imp_version("cdasws")
    except PackageNotFoundError:
        ver = 'bleeding edge'
    print("cdasws version: " + ver)


# Run the version function directly
if __name__ == '__main__':
    version()
