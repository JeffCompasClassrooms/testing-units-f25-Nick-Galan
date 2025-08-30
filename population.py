class CountryPopulation:
    def __init__(self, country, population):
        self.country = country
        self.population = population
        self.world_population = 8_000_000_000  

    def calculate_population_percentage(self):
     
        return (self.population / self.world_population) * 100

    def display_population_percentage(self):
    
        percentage = self.calculate_population_percentage()
       
        return f"The population of {self.country} is {percentage:.2f}% of the world's population."


if __name__ == "__main__":
    
    country = input("Enter the name of the country: ")
    population = int(input(f"Enter the population of {country}: "))

    country_pop = CountryPopulation(country, population)


    print(country_pop.display_population_percentage())
