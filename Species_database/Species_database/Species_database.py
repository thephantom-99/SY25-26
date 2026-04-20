

def display_menu():
    print("\nEndangered Species Database")
    print("Select a species to learn about:\n")
    print("1. Amur Leopard")
    print("2. Hawksbill Sea Turtle")
    print("3. Javan Rhino")
    print("4. Mountain Gorilla")
    print("5. Vaquita")
    print("6. Exit")


def open_species_file(filename):
    try:
        file = open(filename, "r")
        contents = file.read()
        file.close()
        print("\n--- Species Information ---\n")
        print(contents)
    except FileNotFoundError:
        print("Error: File not found.")


while True:
    display_menu()

    choice = input("\nEnter the number of the species you want to view: ")

    if choice == "1":
        open_species_file("amur_leopard.txt")

    elif choice == "2":
        open_species_file("hawksbill_turtle.txt")

    elif choice == "3":
        open_species_file("javan_rhino.txt")

    elif choice == "4":
        open_species_file("mountain_gorilla.txt")

    elif choice == "5":
        open_species_file("vaquita.txt")

    elif choice == "6":
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 6.")

