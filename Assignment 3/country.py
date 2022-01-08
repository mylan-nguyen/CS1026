# Assignment 3: Country Classes
# Mylan Nguyen
## The program will get and set countries with its population, area and population. It can update and save its country information and output the new information in an output.txt.

class Country:

    # constructor for class Country
    def __init__(self, name, pop, area, continent):
        self.name = name
        self.pop = pop
        self.area = area
        self.continent = continent

    # "getter" methods for class Country
    def get_name(self):
        return self.name

    def get_population(self):
        return self.pop

    def get_area(self):
        return self.area

    def get_continent(self):
        return self.continent

    # "setter" methods for class Country
    def set_population(self, pop):
        self.pop = pop

    def set_area(self, area):
        self.area = area

    def set_continent(self, continent):
        self.continent = continent

    # generate string representation for class Country
    def __repr__(self):
        return self.name + " (pop: " + str(self.pop) + ", size: " + str(self.area) + ") in " + self.continent




