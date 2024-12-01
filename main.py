# Define the list of allowed vehicles
AllowedVehiclesList = ['Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan']

# Function to print all allowed vehicles
def print_allowed_vehicles():
    print("********************************")
    print("The AutoCountry sales manager has authorized the purchase and selling of the following vehicles:")
    for vehicle in AllowedVehiclesList:
        print(f"- {vehicle}")
    print("********************************")

# Function to search for a specific vehicle
def search_vehicle():
    print("********************************")
    print("Please Enter the full Vehicle name:")
    vehicle_name = input("           ").strip().lower()  # Convert input to lowercase
    if vehicle_name in [v.lower() for v in AllowedVehiclesList]:  # Compare in lowercase
        print(f"{vehicle_name.title()} is an authorized vehicle.")  # Format title case
    else:
        print(f"{vehicle_name.title()} is not an authorized vehicle, if you received this in error please check the spelling and try again.")
    print("********************************")

# Function to add a new vehicle
def add_vehicle():
    print("********************************")
    print("Please Enter the full Vehicle name you would like to add:")
    new_vehicle = input("           ").strip()  # Clean input
    if new_vehicle.lower() not in [v.lower() for v in AllowedVehiclesList]:  # Check in lowercase
        AllowedVehiclesList.append(new_vehicle)
        print(f'You have added "{new_vehicle}" as an authorized vehicle.')
    else:
        print(f'"{new_vehicle}" is already in the list of authorized vehicles.')
    print("********************************")

# Main menu function
def menu():
    while True:
        print("********************************")
        print("AutoCountry Vehicle Finder v0.3")
        print("********************************")
        print("Please Enter the following number below from the following menu:")
        print("1. PRINT all Authorized Vehicles")
        print("2. SEARCH for Authorized Vehicle")
        print("3. ADD Authorized Vehicle")
        print("4. Exit")
        print("********************************")

        choice = input("           ").strip()  # Clean input
        if choice == '1':
            print_allowed_vehicles()
        elif choice == '2':
            search_vehicle()
        elif choice == '3':
            add_vehicle()
        elif choice == '4':
            print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
menu()
