# Assignment 3: Country Classes
# Mylan Nguyen
## The program will get and set countries with its population, area and population. It can update and save its country information and output the new information in an output.txt.

from country import Country

class CountryCatalogue:

    # constructor for class CountryCatalogue
    def __init__(self, country_file):
        country_info = open(country_file)
        all_info = country_info.readlines()
        country_info.close()
        self.country_cat = []
        self.header_line = False

        for divider in all_info:
            divider = divider.strip()
            if divider == "Country|Continent|Population|Area":
                self.header_line = True
                continue
            else:
                divider = divider.split("|")
                self.country_cat.append(Country(divider[0], divider[2], divider[3], divider[1]))

    # "setter" methods for class CountryCatalogue
    def set_country_population(self, country, pop):
        for value in self.country_cat:
            if value.get_name() == country:
                value.set_population(pop)

    def set_country_area(self, country, area):
        for value in self.country_cat:
            if value.get_name() == country:
                value.set_area(area)

    def set_country_continent(self, country, continent):
        for value in self.country_cat:
            if value.get_name() == country:
                value.set_continent(continent)

    # check if the country does exist and return none if it does not
    def find_country(self, country):
        for value in self.country_cat:
            if value.get_name == country:
                return country
            return None

    # add country information and returning True if the is successfully added
    def add_country(self, country_name, pop, area, continent):
        for value in self.country_cat:
            if value.get_name() == country_name:
                return False
            object = Country(country_name, pop, area, continent)
            self.country_cat.append(object)
            return True

    # print list of the countries using repr of the Country class
    def print_country_catalogue(self):
        for item in self.country_cat:
            print(item)

    # sort country name by alphabetical order and print the file
    def save_country_catalogue(self, fname):
        self.country_cat = sorted(self.country_cat, key=lambda country: country.get_name())
        self.sorted_values = 0
        self.country_file_write = open(fname, "w")
        if self.header_line == True:
            self.country_file_write.write("Country|Continent|Population|Area\n")

        for country in self.country_cat:
            self.country_file_write.write(country.get_name()+"|"+country.get_continent()+"|"+str(country.get_population())+"|"+str(country.get_area())+"\n")

            self.sorted_values += 1

        self.country_file_write.close()

        if self.sorted_values != 0:
            return self.sorted_values
        else:
            return -1







