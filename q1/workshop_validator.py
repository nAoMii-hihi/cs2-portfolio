# Part 1, Student Name - Presence Validation
SName = str(input("Kindly enter your name: "))
if not SName:
  print("REGISTRATION NOT ACCEPTED")
  print("A student name is required.")
  raise SystemExit
  
# Part 2. Age - Data Type + Range Validation
try:
  Age = int(input("Kindly enter your age: "))
  if Age < 11 or Age > 18:
    print("REGISTRATION NOT ACCEPTED")
    print("Age must be between 11 and 18.")
    raise SystemExit
    
except ValueError:
  print("REGISTRATION NOT ACCEPTED")
  print("Age is required to be a number.")
  raise SystemExit
  
# Part 3. Grade Level - Acceptable Value Validation
try: 
  Grade_level = int(input("Kindly enter your grade level: "))
  if Grade_level < 7 or Grade_level > 12:
    print("REGISTRATION NOT ACCEPTED")
    print("Invalid grade level.")
    raise SystemExit
    
except ValueError:
  print("REGISTRATION NOT ACCEPTED")
  print("Invalid grade level.")
  raise SystemExit
  
# Part 4. Email - Simple Pattern Validation
try:
  email = str(input("Kindly enter your email: "))
  if not "@" in email:
    print("REGISTRATION NOT ACCEPTED")
    print("Invalid email.")
    raise SystemExit
    
except ValueError:
  print("REGISTRATION NOT ACCEPTED")
  print("Invalid email.")
  raise SystemExit

# Part 5. Registration Code
try:
  Rcode = input("Kindly enter your registration code: ")
  if len(Rcode) != 6:
    print("REGISTRATION NOT ACCEPTED")
    print("The registration code must contain 6 characters.")
    raise SystemExit

except ValueError:
  print("REGISTRATION NOT ACCEPTED")
  print("The registration code must contain 6 characters.")
  raise SystemExit

print("------------------------------")
print("REGISTRATION ACCEPTED")
print("------------------------------")
print("Student:", SName)
print("Age:", Age)
print("Grade Level:", Grade_level)
print("Email:", email)
print("Registration Code:", Rcode)
