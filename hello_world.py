def main():
    # Prompt the user to enter their name using the input() function.
    # The message inside input() is displayed to the user.
    name = input("Please enter your name: ")

    # Use an f-string to create a personalized welcome message.
    # The f-string allows embedding the 'name' variable directly within the string.
    print(f"Welcome, {name}! We're glad to have you here.")

# This ensures that the main() function is called only when the script is executed directly.
# It prevents the function from running if the script is imported as a module into another script.
if __name__ == "__main__":
    main()
