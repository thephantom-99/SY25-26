# Py-Fest 2026 Stage Manager

def main():
    lineup = [
        ("The Pythonistas", "Rock", 45),
        ("Code Play", "Indie", 30),
        ("Syntax Error", "Metal", 60),
    ]

    while True:
        print("\n--- Py-Fest 2026 Stage Manager ---")
        print("1. View Lineup & Total Time")
        print("2. Add a New Band")
        print("3. Move First Band to End (Late Arrival)")
        print("4. Remove a Band by Name")
        print("5. Move Band to Specific Position")
        print("6. Exit")

        try:
            choice = input("Select an option (1-6): ")
        except (EOFError, KeyboardInterrupt):
            print("\nExiting Stage Manager. Have a great show!")
            break

        # 1. View lineup & total time
        if choice == "1":
            print("\n--- Current Lineup ---")
            total_time = 0
            for i, (name, genre, duration) in enumerate(lineup, 1):
                print(f"{i}. {name} ({genre}) - {duration} mins")
                total_time += duration
            print(f"Total Festival Duration: {total_time} minutes")

        # 2. Add a new band
        elif choice == "2":
            name = input("Enter band name: ")
            genre = input("Enter genre: ")
            try:
                duration = int(input("Enter performance duration (minutes): "))
                lineup.append((name, genre, duration))
                print(f"{name} added!")
            except ValueError:
                print("Invalid duration.")

        # 3. Move first band to end
        elif choice == "3":
            if len(lineup) > 1:
                late_band = lineup.pop(0)
                lineup.append(late_band)
                print(f"{late_band[0]} moved to the end.")
            else:
                print("Not enough bands to swap!")
 
    main()

