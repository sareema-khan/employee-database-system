#showroom for cars , cycles , motorcycles 
#features 
#add cars
#viwe cars
#serch for cars
#delete car from records 
#update in showroom
# exit 

print("=" * 40)
print("\tWELCOME TO DRIVE")
print("=" * 40)

# Cart
cart = []

# Cars
cars = [
    {
        "Brand": "Mercedes",
        "Model": "C Class",
        "Color": "Black",
        "Price": "20,000,000",
        "Year": "2026",
        "Fuel Type": "Petrol"
    },
    {
        "Brand": "BMW",
        "Model": "M4 Competition",
        "Color": "Blue",
        "Price": "32,000,000",
        "Year": "2024",
        "Fuel Type": "Petrol"
    },
    {
        "Brand": "Tesla",
        "Model": "Model 3",
        "Color": "Red",
        "Price": "14,000,000",
        "Year": "2024",
        "Fuel Type": "Electric"
    }
]

# Motorcycles
motorcycles = [
    {
        "Brand": "Honda",
        "Model": "CBR 650R",
        "Color": "Red",
        "Price": "3,500,000",
        "Year": "2025",
        "Fuel Type": "Petrol"
    },
    {
        "Brand": "Yamaha",
        "Model": "YZF R1",
        "Color": "Blue",
        "Price": "6,800,000",
        "Year": "2025",
        "Fuel Type": "Petrol"
    },
    {
        "Brand": "Kawasaki",
        "Model": "Ninja ZX10R",
        "Color": "Green",
        "Price": "7,500,000",
        "Year": "2025",
        "Fuel Type": "Petrol"
    }
]

# Cycles
cycles = [
    {
        "Brand": "Giant",
        "Model": "Escape 3",
        "Color": "Black",
        "Price": "80,000",
        "Year": "2025",
        "Fuel Type": "Manual"
    },
    {
        "Brand": "Trek",
        "Model": "FX 2",
        "Color": "Blue",
        "Price": "95,000",
        "Year": "2025",
        "Fuel Type": "Manual"
    },
    {
        "Brand": "Scott",
        "Model": "Sub Cross",
        "Color": "Red",
        "Price": "110,000",
        "Year": "2025",
        "Fuel Type": "Manual"
    }
]


# ---------------- CAR ----------------

def show_cars():
    print("\nAvailable Cars")

    for car in cars:
        print("-", car["Brand"])

    brand = input("\nWhich car do you want to buy? ")

    for car in cars:
        if car["Brand"].lower() == brand.lower():

            print("\nVehicle Details")
            for key, value in car.items():
                print(f"{key}: {value}")

            print("\n1. Buy Now")
            print("2. Add To Cart")
            print("3. Back")

            choice = input("Enter Choice: ")

            if choice == "1":
                input("Enter Payment Amount: ")
                print("\nCongratulations!")
                print("You are now the owner of", car["Brand"], car["Model"])

            elif choice == "2":
                cart.append(car)
                print("Vehicle Added To Cart Successfully!")

            return

    print("Vehicle Not Found")


# ---------------- MOTORCYCLE ----------------

def show_motorcycles():
    print("\nAvailable Motorcycles")

    for bike in motorcycles:
        print("-", bike["Brand"])

    brand = input("\nWhich motorcycle do you want to buy? ")

    for bike in motorcycles:
        if bike["Brand"].lower() == brand.lower():

            print("\nVehicle Details")
            for key, value in bike.items():
                print(f"{key}: {value}")

            print("\n1. Buy Now")
            print("2. Add To Cart")
            print("3. Back")

            choice = input("Enter Choice: ")

            if choice == "1":
                input("Enter Payment Amount: ")
                print("\nCongratulations!")
                print("You are now the owner of", bike["Brand"], bike["Model"])

            elif choice == "2":
                cart.append(bike)
                print("Motorcycle Added To Cart Successfully!")

            return

    print("Motorcycle Not Found")


# ---------------- CYCLE ----------------

def show_cycles():
    print("\nAvailable Cycles")

    for cycle in cycles:
        print("-", cycle["Brand"])

    brand = input("\nWhich cycle do you want to buy? ")

    for cycle in cycles:
        if cycle["Brand"].lower() == brand.lower():

            print("\nVehicle Details")
            for key, value in cycle.items():
                print(f"{key}: {value}")

            print("\n1. Buy Now")
            print("2. Add To Cart")
            print("3. Back")

            choice = input("Enter Choice: ")

            if choice == "1":
                input("Enter Payment Amount: ")
                print("\nCongratulations!")
                print("You are now the owner of", cycle["Brand"], cycle["Model"])

            elif choice == "2":
                cart.append(cycle)
                print("Cycle Added To Cart Successfully!")

            return

    print("Cycle Not Found")


# ---------------- CART ----------------

def view_cart():

    if len(cart) == 0:
        print("\nCart is Empty.")

    else:
        print("\nItems In Cart")

        for item in cart:
            print("-" * 30)
            print("Brand:", item["Brand"])
            print("Model:", item["Model"])
            print("Price:", item["Price"])


# ---------------- MAIN MENU ----------------

while True:

    print("\n========== MENU ==========")
    print("1. Cars")
    print("2. Motorcycles")
    print("3. Cycles")
    print("4. View Cart")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        show_cars()

    elif choice == "2":
        show_motorcycles()

    elif choice == "3":
        show_cycles()

    elif choice == "4":
        view_cart()

    elif choice == "5":
        print("\nThank You For Visiting DRIVE Showroom.")
        break

    else:
        print("Invalid Choice!")