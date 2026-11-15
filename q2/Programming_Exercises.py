# Exercise 1: Count Even Numbers
# Use range() with a step of 2 to display even numbers
for number in range(2, 21, 2):
  print (number)



# Exercise 2: The Countdown Timer
# Begin the countdown from 10
number = 10

# Continue the loop while the number is greater than or equal to 1
while number >= 1:
    print(number)
    number -= 1  # Subtracts 1 after every loop

# Display the message after the countdown
print("Time is up!")



# Exercise 3: Skip Multiples
# Loop through numbers from 1 to 15
for number in range(1, 16):

# Check whether the number is divisible by 3
  if number % 3 == 0:
      continue  # Skip the current number

# Display the number if it is not a multiple of 3
  print(number)



# Exercise 4. Multiplication Table Generator
# Make a function for the multiplication table
def show_table(number):

    # Repeat from 1 to 10
    for i in range(1, 11):

        # Multiply the number by i
      print(number, "x", i, "=", number * i)

# Ask the user for a number
num = int(input("Enter a number: "))

# Show the multiplication table
show_table(num)
