import unittest
from population import *
    


class TestCountryPopulation(unittest.TestCase):

    def test_01_china_population_percentage(self):
        c = CountryPopulation("China")
        self.assertGreater(c.population_percentage(), 10)

    def test_02_india_population_percentage(self):
        c = CountryPopulation("India")
        self.assertGreater(c.population_percentage(), 15)

    def test_03_usa_population_percentage(self):
        c = CountryPopulation("USA")
        self.assertLess(c.population_percentage(), 5)

    def test_04_japan_population_percentage(self):
        c = CountryPopulation("Japan")
        self.assertGreater(c.population_percentage(), 1)

    def test_05_china_density(self):
        c = CountryPopulation("China")
        self.assertGreater(c.population_density(), 300)

    def test_06_brazil_density(self):
        c = CountryPopulation("Brazil")
        self.assertLess(c.population_density(), 100)

    def test_07_bangladesh_density(self):
        c = CountryPopulation("Bangladesh")
        self.assertGreater(c.population_density(), 2000)

    def test_08_russia_density(self):
        c = CountryPopulation("Russia")
        self.assertLess(c.population_density(), 50)

    def test_09_japan_density(self):
        c = CountryPopulation("Japan")
        self.assertGreater(c.population_density(), 500)

    def test_10_mexico_density(self):
        c = CountryPopulation("Mexico")
        self.assertGreater(c.population_density(), 100)

    def test_11_country_area_is_positive(self):
        c = CountryPopulation("India")
        self.assertGreater(c.area, 0)

    def test_12_country_population_is_positive(self):
        c = CountryPopulation("USA")
        self.assertGreater(c.population, 0)

    def test_13_data_store_has_china(self):
        self.assertIn("China", CountryPopulation.data_store)

    def test_14_data_store_has_japan(self):
        self.assertIn("Japan", CountryPopulation.data_store)

    def test_15_data_store_value_is_tuple(self):
        value = CountryPopulation.data_store["India"]
        self.assertIsInstance(value, tuple)

    def test_16_population_is_integer(self):
        c = CountryPopulation("Brazil")
        self.assertIsInstance(c.population, int)

    def test_17_density_is_float(self):
        c = CountryPopulation("USA")
        self.assertIsInstance(c.population_density(), float)

    def test_18_percentage_is_float(self):
        c = CountryPopulation("Indonesia")
        self.assertIsInstance(c.population_percentage(), float)

    def test_19_valid_percentage_range(self):
        c = CountryPopulation("Nigeria")
        percentage = c.population_percentage()
        self.assertGreater(percentage, 0)
        self.assertLess(percentage, 100)

    def test_20_valid_density_range(self):
        c = CountryPopulation("India")
        density = c.population_density()
        self.assertGreater(density, 100)
        self.assertLess(density, 2000)

    def test_21_world_population_constant(self):
        self.assertEqual(CountryPopulation.world_population, 8_000_000_000)

    def test_22_invalid_country_raises_keyerror(self):
        with self.assertRaises(KeyError):
            CountryPopulation("Wakanda")

    def test_23_most_populous_country(self):
        self.assertEqual(most_populous(), "China")

    def test_24_least_populous_country(self):
        self.assertEqual(least_populous(), "Japan")

    def test_25_most_dense_country(self):
        self.assertEqual(most_dense(), "Bangladesh")

    def test_26_least_dense_country(self):
        self.assertEqual(least_dense(), "Russia")

    def test_27_methods_are_callable(self):
        self.assertTrue(callable(most_dense))
        self.assertTrue(callable(least_dense))

    def test_28_density_calculation_matches(self):
        c = CountryPopulation("Mexico")
        expected = c.population / c.area
        self.assertAlmostEqual(c.population_density(), expected)

    def test_29_percentage_calculation_matches(self):
        c = CountryPopulation("Nigeria")
        expected = (c.population / CountryPopulation.world_population) * 100
        self.assertAlmostEqual(c.population_percentage(), expected)

    def test_30_comparative_density(self):
        bd = CountryPopulation("Bangladesh").population_density()
        ru = CountryPopulation("Russia").population_density()
        self.assertGreater(bd, ru)


