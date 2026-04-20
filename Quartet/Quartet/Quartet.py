H3 = ["H3", "Honda Integra Type R", 235, (145, 198), 6500, 5.5, 1800, 4]
H4 = ["H4", "Mazda RX-7", 255, (150, 205), 7000, 5.2, 1900, 4]

cars = [H3, H4] 

def print_car(c):
    print("|", c[0], c[1], c[2], c[3], c[4], c[5], c[6], c[7])


print("Available cars:")
for i, car in enumerate(cars, start=1):
    print(f"{i}. {car[1]}")


while True:
    try:
        print("\nEnter the car number to view details (or type '0' to exit):")
        choice = int(input())
        
        if choice == 0:
            print("Exiting...")
            break
        elif 1 <= choice <= len(cars):
            print("\nYou selected:")
            print_car(cars[choice - 1])
        else:
            print("Invalid choice. Please select a valid car number.")
    except ValueError:
        print("Invalid input. Please enter a number.")