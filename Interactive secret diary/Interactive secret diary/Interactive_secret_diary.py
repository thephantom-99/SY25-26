import datetime

FILE_NAME = "my_diary.txt"

while True:
    print("\n1. Write")
    print("2. Read")
    print("3. Clear")
    print("4. Exit")

    choice = input("Select (1-4): ")

    # WRITE ENTRY
    if choice == "1":
        entry = input("Entry: ")

        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        full_entry = f"[{timestamp}]\n{entry}\n{'-'*40}\n"

        with open(FILE_NAME, "a") as file:
            file.write(full_entry)

        print(f"\nSaved! Character count: {len(entry)}")

    # READ ENTRIES
    elif choice == "2":
        try:
            with open(FILE_NAME, "r") as file:
                contents = file.read()

            if contents.strip() == "":
                print("\nDiary is empty.")
            else:
                print("\n--- Your Diary ---")
                print(contents)

        except FileNotFoundError:
            print("\nDiary file does not exist yet.")

    # CLEAR DIARY
    elif choice == "3":
        confirm = input("Are you sure you want to clear the diary? (yes/no): ")
        if confirm.lower() == "yes":
            with open(FILE_NAME, "w") as file:
                pass
            print("Diary cleared.")

    # EXIT
    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please select 1-4.")
