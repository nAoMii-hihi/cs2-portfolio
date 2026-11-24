# Exercise 1: My School Bag

# Create a listthat contains the five school supplies
school_supplies = ["Notebook", "Pen", "Calculator", "Laptop", "Book"]

# Display the items using their index places
print("My School Supplies:")
print("Index 0:", school_supplies[0])
print("Index 1:", school_supplies[1])
print("Index 2:", school_supplies[2])
print("Index 3:", school_supplies[3])
print("Index 4:", school_supplies[4])
print("\nFirst Item:", school_supplies[0])
print("Last Item:", school_supplies[4])

# Instead of putting so many variables, I used a list to store the five school supplies. I accessed each item through its index position. I also displayed the first and last item separately and used "\n" to add a blank space between the previous outputs and "First Item".



# Exercise 2:Travel Destination Manager

# Create a list containing five travel destinations
destinations = ["Cebu", "Manila", "Davao", "Baguio", "Palawan"]

# Display all destinations using a for loop
print("All Travel Destinations:")
for place in destinations:
  print(place)

# Use slicing to display items from index 1 up to index 4
print("\nDestinations from index 1 to 3:")
print(destinations[1:4])

# Ask the user to input a destination to search for
search = str(input("Kindly enter a destination to search for: "))

# Check whether the destination exists in the list or not
if search in destinations: 
  print(search, "exists in the list.")
else: 
  print(search, "does not exist in the list.")

# Replace the item in index 2 with Iloilo
destinations[2] = "Iloilo"

# Display the updated list
print("\nUpdated Travel Destinations:")
print(destinations)

# I used a list to store all five travel destinations. I used a for loop to display them and slicing to show selected destinations. I also used input and the in operator to look for a destination. Finally, I replaced Davao with Iloilo and displayed the final list.
