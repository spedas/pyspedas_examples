"""Test the examples."""

import unittest


class LoadTestCases(unittest.TestCase):
    """Run tests on examples."""

    def test_version(self):
        """Test ex_avg."""
        from pyspedas_examples.version import version
        self.assertFalse(version())

    def test_ex_analysis(self):
        """Test ex_analysis."""
        from pyspedas_examples.examples.ex_analysis import ex_analysis
        ex = ex_analysis()
        self.assertEqual(ex, 1)

    def test_ex_avg(self):
        """Test ex_avg."""
        from pyspedas_examples.examples.ex_avg import ex_avg
        ex = ex_avg()
        self.assertEqual(ex, 1)

    def test_ex_avg2(self):
        """Test ex_avg."""
        from pyspedas_examples.examples.ex_avg import ex_avg2
        ex = ex_avg2()
        self.assertAlmostEqual(ex[0], 1044.22)

    def test_ex_basic(self):
        """Test ex_basic."""
        from pyspedas_examples.examples.ex_basic import ex_basic
        ex = ex_basic()
        self.assertEqual(ex, 1)

    def test_ex_cdagui(self):
        """Test ex_cdagui."""
        from pyspedas_examples.examples.ex_cdagui import ex_cdagui
        ex = ex_cdagui()
        self.assertEqual(ex, 1)

    def test_ex_cdasws(self):
        """Test ex_cdasws."""
        from pyspedas_examples.examples.ex_cdasws import ex_cdasws
        ex = ex_cdasws()
        self.assertEqual(ex, 1)

    def test_ex_create(self):
        """Test ex_basic."""
        from pyspedas_examples.examples.ex_create import ex_create
        ex = ex_create()
        self.assertEqual(ex, 1)

    def test_ex_deriv(self):
        """Test ex_basic."""
        from pyspedas_examples.examples.ex_deriv import ex_deriv
        ex = ex_deriv()
        self.assertEqual(ex, 1)

    def test_ex_deriv2(self):
        """Test ex_basic."""
        from pyspedas_examples.examples.ex_deriv import ex_deriv2
        ex = ex_deriv2()
        self.assertEqual(ex, 1)

    def test_ex_dsl2gse(self):
        """Test ex_dsl2gse."""
        from pyspedas_examples.examples.ex_dsl2gse import ex_dsl2gse
        ex = ex_dsl2gse()
        self.assertEqual(ex, 1)

    def test_ex_gmag(self):
        """Test ex_dsl2gse."""
        from pyspedas_examples.examples.ex_gmag import ex_gmag
        ex = ex_gmag()
        self.assertEqual(ex, 1)

    def test_ex_smooth(self):
        """Test ex_dsl2gse."""
        from pyspedas_examples.examples.ex_smooth import ex_smooth
        ex = ex_smooth()
        self.assertEqual(ex, 1)

    def test_ex_spectra(self):
        """Test ex_spectra."""
        from pyspedas_examples.examples.ex_spectra import ex_spectra
        ex = ex_spectra()
        self.assertEqual(ex, 1)

    def test_ex_spikes(self):
        """Test ex_spectra."""
        from pyspedas_examples.examples.ex_spikes import ex_spikes
        ex = ex_spikes()
        self.assertEqual(ex, 1)

    def test_ex_wavelet(self):
        """Test ex_spectra."""
        from pyspedas_examples.examples.ex_wavelet import ex_wavelet
        ex = ex_wavelet()
        self.assertEqual(ex, 1)

    def test_pseudovar_right_axis(self):
        import pyspedas
        from pytplot import store_data,options, tplot_options, tplot
        pyspedas.mms.fpi(datatype='des-moms', trange=['2015-10-16', '2015-10-17'])
        pyspedas.mms.edp(trange=['2015-10-16', '2015-10-17'], datatype='scpot')
        options('mms1_edp_scpot_fast_l2', 'yrange', [10, 100])
        store_data('spec', data=['mms1_des_energyspectr_omni_fast', 'mms1_edp_scpot_fast_l2'])
        options('spec', 'right_axis', True)
        tplot_options('xmargin', [0.1, 0.2])
        tplot('spec', xsize=12)

if __name__ == '__main__':
    unittest.main()
