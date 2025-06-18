def main():
    # Prompt the user to enter their name using the input() function.
    # The message inside input() is displayed to the user.
    name = input("Please enter your name: ")
    # timeOfDay = input("What time is it?: ")
    print("Please enter the current hour in 24-hour format (e.g., 9, 14, 22).")
    time_input = input("What hour is it right now? ")

    # Initialize a variable to store the time of day category
    time_of_day_category = ""
    message = "Hello, " # Default greeting if time input is invalid or not categorized

    try:
        current_hour = int(time_input)

        # Use if/elif/else to determine the time of day category
        # Morning: 5 AM to 11 AM (inclusive of 5, exclusive of 12)
        if 5 <= current_hour < 12:
            time_of_day_category = "morning"
            message = "Good morning, "
        # Afternoon: 12 PM to 5 PM (inclusive of 12, exclusive of 18)
        elif 12 <= current_hour < 18:
            time_of_day_category = "afternoon"
            message = "Good afternoon, "
        # Evening/Night: 6 PM to 4 AM (inclusive of 18, exclusive of 5)
        elif 18 <= current_hour <= 23 or 0 <= current_hour < 5:
            time_of_day_category = "evening"
            message = "Good evening, "

    except ValueError:
        print("Invalid input. Please enter a whole number for the hour.")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")

    if name == "Dan" or name == "Daniel":
        print(f"{message}AI Engineer {name}!")
    else:
        print(f"{message}{name}! We're glad to have you here.")


# This ensures that the main() function is called only when the script is executed directly.
# It prevents the function from running if the script is imported as a module into another script.
if __name__ == "__main__":
    main()
