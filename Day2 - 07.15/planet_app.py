planets = []

m = 9


print("############################################")
print("1. Enter 1 to add a planet to the list")
print("2. Enter 2 to update a planet based on its ID")
print("3. Enter 3 to display the number of planets available in the list")
print("4. Enter 4 to delete a planet in the list")
print("5. Enter 9 to finish")
print("############################################")


choice= -1
FINISHED = 9

while choice != FINISHED:
    choice = int(input("Enter a number for choice: "))
    if choice == 1:
        new_planet = input("Enter a new planet name: ")
        planets.append(new_planet)
    elif choice == 2:
        index_to_update = int(input("Enter your planet's ID to update: "))
        if index_to_update >=0:
            new_planet_name = input("Enter the new name for the planet: ")
            planets[index_to_update] = new_planet_name
        else:
            print("Sorry! Out of bounds index")

    elif choice == 3:
        print(len(planets))

    elif choice == 4:
        planet_to_delete = input("Enter the name of the planet you want to delete: ")
        planets.remove(planet_to_delete)
    elif choice == FINISHED:
        print("We are done here !")




    




