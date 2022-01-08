# Assignment 3: Country Classes
# Mylan Nguyen
## The program will get and set countries with its population, area and population. It can update and save its country information and output the new information in an output.txt.


from catalogue import CountryCatalogue
from country import Country

# use the country name and reformat the information by stripping any spaces and a new string will be returned
def format_country(country):
    country = country.lower().strip()
    list_info = country.split()
    country = " ".join(list_info)
    return country.title()

# create another file with the new updates included to the original file
def process_updates(country_fname, update_fname):
    user_input = ""
    quit = False
    while quit != True:
        try:
            country_header = open(country_fname)
            country_header.close()
            country_catalogue_object = CountryCatalogue(country_fname)

        # check to ensure that the file exists, user will be prompted to input a different name for the file or exit
        except IOError:
            user_input = input("Unable to open the file you entered. Would you like to quit? Please input 'Y' (yes) or 'N' (no).")
            if user_input.lower() == 'n':
                country_fname = input("Please enter name of your file country data:")
            else:
                output = open("output.txt", "w")
                output.write("Update Unsuccessful\n")
                output.close()
                return False
        quit = True

    # reset values for update file
    quit = False
    # while loop will run only if section above was unsuccessful
    while quit != True:
        try:
            update_header = open(update_fname)
            line_updates_header = update_header.readlines()
            update_header.close()
            quit = True
        # check to ensure that the file exists, user will be prompted to input a different name for the file or exit
        except IOError:
            user_input = input("Unable to open the file you entered. Would you like to quit? Please input 'Y' (yes) or 'N' (no).")
            if user_input.lower() == 'n':
                update_fname = input("Please enter name of your file with country updates:")
            else:
                output = open("output.txt", "w")
                output.write("Update Unsuccessful\n")
                output.close()
                return False

    # proceed to process file updates
    for update in line_updates_header:
        update_valid = False
        pop = ""
        area = ""
        continent = ""
        pop_update = False
        area_update = False
        continent_update = False
        update = update.strip().split(";")

        # add the new updates to respective locations based on if it is for pop, area or continent of a country
        for i in update:
            try:
                update_country = Country(update[0], '', '', '')
                country = update[0]
                if 'CON' in i:
                    continent = i.strip()[4:]
                    update[1] = continent
                    continent_update = True
                elif 'POP' in i:
                    pop = i.strip()[4:]
                    update[1] = pop
                    temp = pop
                    pop = int(pop.replace(",", ""))
                    pop = temp
                    pop_update = True
                elif 'AREA' in i:
                    area = i.strip()[5:]
                    update[1] = area
                    temp = area
                    area = int(area.replace(",", ""))
                    area = temp
                    area_update = True
            # the line will be skipped if the value for the update is invalid
            except ValueError:
                update_valid = True
                break
        # skip the rest of the iteration if the data is invalid
        if update_valid == True:
            break
        elif update_valid == False:
            # if country is not already in catalogue, add the information to the output
            if country_catalogue_object.find_country(update_country) != country:
                country_catalogue_object.add_country(country, continent, pop, area)
            else:
            # if country is already in the catalogue, update the information in the output with the new values
                if continent_update == True:
                    country.set_country_continent(country, continent_update)
                if pop_update == True:
                    country.set_country_population(country, pop_update)
                if area_update == True:
                    country.set_country_area(country, area_update)

# saving to file and output the updated information
    country_catalogue_object.save_country_catalogue("output.txt")
    return True

