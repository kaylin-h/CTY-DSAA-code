countries = ["USA", "Greece", "Malaysia"]
populations = [333.3 , 1000.4, 33.9]
continents = ["North America", "Europe", "Asia"]

# printing the original list of countries 
print("Original list of countries: ")
for x in countries:
    print(x)

#fixing the population of a country 
populations[1] = 10.4 

#adding a country to the list of your choice
new_country = input("Enter a new country to add: ")
if(new_country in countries):
    print("This country is already in the catalog")
else:
    new_population = float(input("Enter the population of the new country: "))
    new_continent = input("Enter the continent where the new continent is: ")
    countries.append(new_country)
    populations.append(new_population)
    continents.append(new_continent)
    print(new_country, "has been added to the catalog")

#searching for a specific country and its attribute 

country_in_search = input("Enter the country you are looking for: ")
found = False 
for x in countries:
    if (x == country_in_search):
        found = True 
        break

if (found): 
    index = countries.index(country_in_search)
    print(country_in_search, ": population = ", populations[index], " continent = ", continents[index])
else:
    print("Sorry! This country is not found")