class CountryPopulation:
    data_store = {
        "China": (1_412_600_000, 3_705_407),
        "India": (1_366_000_000, 1_269_346),
        "USA": (331_000_000, 3_800_000),
        "Indonesia": (273_000_000, 735_358),
        "Brazil": (212_600_000, 3_287_956),
        "Nigeria": (206_100_000, 356_669),
        "Bangladesh": (166_300_000, 56_980),
        "Russia": (144_400_000, 6_601_668),
        "Mexico": (128_900_000, 761_606),
        "Japan": (125_800_000, 145_937),
    }

    world_population = 8_000_000_000

    def __init__(self, country):
        self.country = country
        self.population, self.area = self.data_store[country]

    def population_percentage(self):
        return (self.population / self.world_population) * 100

    def population_density(self):
        return self.population / self.area


def most_populous():
    return max(CountryPopulation.data_store.items(),
               key=lambda item: item[1][0])[0]


def least_populous():
    return min(CountryPopulation.data_store.items(),
               key=lambda item: item[1][0])[0]


def most_dense():
    return max(CountryPopulation.data_store.items(),
               key=lambda item: item[1][0] / item[1][1])[0]


def least_dense():
    return min(CountryPopulation.data_store.items(),
               key=lambda item: item[1][0] / item[1][1])[0]
