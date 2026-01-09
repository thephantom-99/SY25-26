# This is a simple program to calculate a user's age category based on their input.
# It contains a few bugs that need to be fixed.


# Function to determine the age category
def get_age_category(age):
    # Check if age is a valid number
    if not isinstance(age, int):
        print("Please enter a valid age as a number.")
        return None

    # Correct age category logic
    if age < 18:
        return "Child"
    elif age < 65:
        return "Adult"
    else:
        return "Senior"


# Main part of the program
def main():
    user_age_input = input("Please enter your age: ")
    try:
        user_age = int(user_age_input)
    except ValueError:
        print("Please enter a valid age as a number.")
        return

    category = get_age_category(user_age)

    if category:
        print(f"You are a {category}.")


# Call the main function to run the program
main()
