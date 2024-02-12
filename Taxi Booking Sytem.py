class TaxiBookingSystem:
    def __init__(self):
        # Dictionary to store user credentials (username: password)
        self.users = {}
        # Dictionary to store bookings for each user (username: [booking1, booking2, ...])
        self.bookings = {}
        # Variable to keep track of the currently logged-in user
        self.current_user = None

    def display_menu(self):
        # Display the main menu options
        print("\nTaxi Booking System Menu:")
        print("1. Login")
        print("2. Search for Bookings")
        print("3. Create an Account")
        print("4. Exit")

    def login(self):
        # Prompt the user to enter their username and password
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        # Check if the entered credentials are valid
        if username in self.users and self.users[username] == password:
            print(f"Welcome, {username}!")
            self.current_user = username
        else:
            print("Invalid username or password.")

    def search_bookings(self):
        # Display bookings for the currently logged-in user
        if self.current_user:
            print(f"Bookings for {self.current_user}:")
            if self.current_user in self.bookings:
                for booking in self.bookings[self.current_user]:
                    print(booking)
            else:
                print("No bookings found.")
        else:
            print("Please login first.")

    def create_account(self):
        # Prompt the user to create a new account with a unique username and password
        username = input("Enter a new username: ")
        password = input("Enter a password: ")

        # Check if the chosen username already exists
        if username not in self.users:
            # Create a new account and initialize an empty bookings list for the user
            self.users[username] = password
            self.bookings[username] = []
            print("Account created successfully.")
        else:
            print("Username already exists. Please choose a different username.")

    def run(self):
        # Main loop to run the taxi booking system
        while True:
            # Display the main menu
            self.display_menu()
            # Prompt the user to enter their choice
            choice = input("Enter your choice (1-4): ")

            # Execute the corresponding functionality based on the user's choice
            if choice == "1":
                self.login()
            elif choice == "2":
                self.search_bookings()
            elif choice == "3":
                self.create_account()
            elif choice == "4":
                print("Exiting the Taxi Booking System. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    # Create an instance of the TaxiBookingSystem class and run the system
    taxi_system = TaxiBookingSystem()
    taxi_system.run()
