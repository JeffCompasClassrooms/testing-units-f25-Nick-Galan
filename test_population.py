import unittest
from population import CountryPopulation

class TestCountryPopulation(unittest.TestCase):

    def test_india(self):
        no = CountryPopulation("India", 1_400_000_000)
        self.assertAlmostEqual(no.calculate_population_percentage(), 17.5, places=4)  
        self.assertNotAlmostEqual(no.calculate_population_percentage(), 10.0, places=4)  

    def test_china(self):
        no = CountryPopulation("China", 1_420_000_000)
        self.assertAlmostEqual(no.calculate_population_percentage(), 17.75, places=4)  
        self.assertNotAlmostEqual(no.calculate_population_percentage(), 20.0, places=4)  

    def test_usa(self):
        no = CountryPopulation("United States", 331_000_000)
        self.assertAlmostEqual(no.calculate_population_percentage(), 4.1375, places=4)  
        self.assertNotAlmostEqual(no.calculate_population_percentage(), 3.0, places=4)  

    def test_indonesia(self):
        no = CountryPopulation("Indonesia", 276_000_000)
        self.assertAlmostEqual(no.calculate_population_percentage(), 3.45, places=4)  
        self.assertNotAlmostEqual(no.calculate_population_percentage(), 5.0, places=4)  

    def test_pakistan(self):
        no = CountryPopulation("Pakistan", 225_000_000)
        self.assertAlmostEqual(no.calculate_population_percentage(), 2.8125, places=4)  
        self.assertNotAlmostEqual(no.calculate_population_percentage(), 3.0, places=4)  

    def test_brazil(self):
        no = CountryPopulation("Brazil", 213_000_000)
        self.assertAlmostEqual(no.calculate_population_percentage(), 2.6625, places=4)  
        self.assertNotAlmostEqual(no.calculate_population_percentage(), 5.0, places=4)  

    def test_nigeria(self):
        no = CountryPopulation("Nigeria", 206_000_000)
        self.assertAlmostEqual(no.calculate_population_percentage(), 2.575, places=4)  
        self.assertNotAlmostEqual(no.calculate_population_percentage(), 1.0, places=4)  

    def test_bangladesh(self):
        no = CountryPopulation("Bangladesh", 166_000_000)
        self.assertAlmostEqual(no.calculate_population_percentage(), 2.075, places=4)  
        self.assertNotAlmostEqual(no.calculate_population_percentage(), 0.5, places=4)  

    def test_russia(self):
        no = CountryPopulation("Russia", 145_000_000)
        self.assertAlmostEqual(no.calculate_population_percentage(), 1.8125, places=4)  
        self.assertNotAlmostEqual(no.calculate_population_percentage(), 2.0, places=4)  

    def test_mexico(self):
        no = CountryPopulation("Mexico", 128_000_000)
        self.assertAlmostEqual(no.calculate_population_percentage(), 1.6, places=4)  
        self.assertNotAlmostEqual(no.calculate_population_percentage(), 0.8, places=4)  

    def test_japan(self):
        no = CountryPopulation("Japan", 126_000_000)
        self.assertAlmostEqual(no.calculate_population_percentage(), 1.575, places=4)  
        self.assertNotAlmostEqual(no.calculate_population_percentage(), 1.0, places=4)  

    def test_ethiopia(self):
        no = CountryPopulation("Ethiopia", 120_000_000)
        self.assertAlmostEqual(no.calculate_population_percentage(), 1.5, places=4)  
        self.assertNotAlmostEqual(no.calculate_population_percentage(), 2.0, places=4)  

    def test_philippines(self):
        no = CountryPopulation("Philippines", 113_000_000)
        self.assertAlmostEqual(no.calculate_population_percentage(), 1.4125, places=4)  
        self.assertNotAlmostEqual(no.calculate_population_percentage(), 0.5, places=4)  

    def test_egypt(self):
        no = CountryPopulation("Egypt", 104_000_000)
        self.assertAlmostEqual(no.calculate_population_percentage(), 1.3, places=4)  
        self.assertNotAlmostEqual(no.calculate_population_percentage(), 2.0, places=4)  

    def test_vietnam(self):
        no = CountryPopulation("Vietnam", 98_000_000)
        self.assertAlmostEqual(no.calculate_population_percentage(), 1.225, places=4)  
        self.assertNotAlmostEqual(no.calculate_population_percentage(), 1.5, places=4)  

    def test_dr_congo(self):
        no = CountryPopulation("Democratic Republic of the Congo", 90_000_000)
        self.assertAlmostEqual(no.calculate_population_percentage(), 1.125, places=4)  
        self.assertNotAlmostEqual(no.calculate_population_percentage(), 0.8, places=4)  

    def test_turkey(self):
        no = CountryPopulation("Turkey", 85_000_000)
        self.assertAlmostEqual(no.calculate_population_percentage(), 1.0625, places=4)  
        self.assertNotAlmostEqual(no.calculate_population_percentage(), 1.5, places=4)  

    def test_iran(self):
        no = CountryPopulation("Iran", 84_000_000)
        self.assertAlmostEqual(no.calculate_population_percentage(), 1.05, places=4)  
        self.assertNotAlmostEqual(no.calculate_population_percentage(), 0.9, places=4)  

    def test_germany(self):
        no = CountryPopulation("Germany", 83_000_000)
        self.assertAlmostEqual(no.calculate_population_percentage(), 1.0375, places=4)  
        self.assertNotAlmostEqual(no.calculate_population_percentage(), 0.8, places=4)  

    def test_thailand(self):
        no = CountryPopulation("Thailand", 70_000_000)
        self.assertAlmostEqual(no.calculate_population_percentage(), 0.875, places=4)  
        self.assertNotAlmostEqual(no.calculate_population_percentage(), 1.0, places=4)  

    def test_uk(self):
        no = CountryPopulation("United Kingdom", 68_000_000)
        self.assertAlmostEqual(no.calculate_population_percentage(), 0.85, places=4)  
        self.assertNotAlmostEqual(no.calculate_population_percentage(), 1.5, places=4)  

    def test_france(self):
        no = CountryPopulation("France", 67_000_000)
        self.assertAlmostEqual(no.calculate_population_percentage(), 0.8375, places=4)  
        self.assertNotAlmostEqual(no.calculate_population_percentage(), 1.0, places=4)  

    def test_italy(self):
        no = CountryPopulation("Italy", 60_000_000)
        self.assertAlmostEqual(no.calculate_population_percentage(), 0.75, places=4)  
        self.assertNotAlmostEqual(no.calculate_population_percentage(), 0.5, places=4)  

    def test_south_africa(self):
        no = CountryPopulation("South Africa", 60_000_000)
        self.assertAlmostEqual(no.calculate_population_percentage(), 0.75, places=4)  
        self.assertNotAlmostEqual(no.calculate_population_percentage(), 1.0, places=4)  

    def test_south_korea(self):
        no = CountryPopulation("South Korea", 51_000_000)
        self.assertAlmostEqual(no.calculate_population_percentage(), 0.6375, places=4)  
        self.assertNotAlmostEqual(no.calculate_population_percentage(), 1.0, places=4)  

    def test_colombia(self):
        no = CountryPopulation("Colombia", 50_000_000)
        self.assertAlmostEqual(no.calculate_population_percentage(), 0.625, places=4)  
        self.assertNotAlmostEqual(no.calculate_population_percentage(), 0.8, places=4)  

    def test_kenya(self):
        no = CountryPopulation("Kenya", 54_000_000)
        self.assertAlmostEqual(no.calculate_population_percentage(), 0.675, places=4)  
        self.assertNotAlmostEqual(no.calculate_population_percentage(), 1.0, places=4)  

    def test_spain(self):
        no = CountryPopulation("Spain", 47_000_000)
        self.assertAlmostEqual(no.calculate_population_percentage(), 0.5875, places=4)  
        self.assertNotAlmostEqual(no.calculate_population_percentage(), 0.7, places=4)  

    def test_ukraine(self):
        no = CountryPopulation("Ukraine", 41_000_000)
        self.assertAlmostEqual(no.calculate_population_percentage(), 0.5125, places=4)  
        self.assertNotAlmostEqual(no.calculate_population_percentage(), 0.8, places=4)  

    def test_uzbekistan(self):
        no = CountryPopulation("Uzbekistan", 34_000_000)
        self.assertAlmostEqual(no.calculate_population_percentage(), 0.425, places=4)  
        self.assertNotAlmostEqual(no.calculate_population_percentage(), 1.0, places=4)  