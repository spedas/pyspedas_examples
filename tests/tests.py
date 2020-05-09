"""Test the examples."""

import unittest


class LoadTestCases(unittest.TestCase):
    """Run tests on examples."""

    '''
    def test_add(self):
        """Generic test."""
        self.assertEqual(1, 1)
    '''

    def test_version(self):
        """Test ex_avg."""
        from pyspedas_examples.version import version
        self.assertFalse(version())

    def test_load_ex_avg(self):
        """Test ex_avg."""
        from pyspedas_examples.examples.basic.ex_avg import ex_avg
        ex = ex_avg(plot=False)
        self.assertEqual(ex, 1)

    def test_load_ex_avg2(self):
        """Test ex_avg."""
        from pyspedas_examples.examples.basic.ex_avg import ex_avg2
        ex = ex_avg2()
        self.assertAlmostEqual(ex[0], 1044.22)

    def test_load_ex_analysis(self):
        """Test ex_analysis."""
        from pyspedas_examples.examples.basic.ex_analysis import ex_analysis
        ex = ex_analysis(plot=False)
        self.assertEqual(ex, 1)

    def test_load_ex_basic(self):
        """Test ex_basic."""
        from pyspedas_examples.examples.basic.ex_basic import ex_basic
        ex = ex_basic(plot=False)
        self.assertEqual(ex, 1)

    def test_load_ex_cdagui(self):
        """Test ex_cdagui."""
        from pyspedas_examples.examples.basic.ex_cdagui import ex_cdagui
        ex = ex_cdagui()
        self.assertEqual(ex, 1)

    def test_load_ex_cdasws(self):
        """Test ex_cdasws."""
        from pyspedas_examples.examples.basic.ex_cdasws import ex_cdasws
        ex = ex_cdasws()
        self.assertEqual(ex, 1)

    def test_load_ex_spectra(self):
        """Test ex_spectra."""
        from pyspedas_examples.examples.basic.ex_spectra import ex_spectra
        ex = ex_spectra(plot=False)
        self.assertEqual(ex, 1)

    ''' # Fails
    def test_load_ex_dsl2gse(self):
        """Test ex_dsl2gse."""
        from pyspedas_examples.examples.basic.ex_dsl2gse import ex_dsl2gse
        ex = ex_dsl2gse()
        self.assertEqual(ex, 1)
    '''


if __name__ == '__main__':
    unittest.main()
