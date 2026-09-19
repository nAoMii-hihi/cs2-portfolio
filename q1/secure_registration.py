# Student Name
student_name = str(input("Enter a student name: ")).strip()
if not student_name:
  print("Registration Not Accepted.")
  print("Error: Student name is required.")
  raise SystemExit

# Section
section = str(input("Enter section: ")).strip()
if section != "Dahlia":
  print("Registration Not Accepted.")
  print("Error: Invalid section.")
  raise SystemExit

# Club Choice
club_choice = str(input("Enter club choice (SIGMa, English, Polaris, BahayNayan, Dance Troupe, Sports): ")).strip()
allowed_clubs = ["SIGMa", "English", "Polaris", "BahayNayan", "Dance Troupe", "Sports"]

if club_choice not in allowed_clubs:
  print("Registration Not Accepted.")
  print("Error: Kindly choose a valid club.")
  raise SystemExit

# School Email
school_email = str(input("Enter school email: ")).strip()
if "@" not in school_email or "." not in school_email:
  print("Registration Not Accepted.")
  print("Error: Kindly enter a valid school email.")
  raise SystemExit

# Attendance Status
attendance_status = str(input("Enter attendance status (Present, Absent, Late): ")).strip()
allowed_status = ["Present", "Absent", "Late"]

if attendance_status not in allowed_status:
  print("Registration Not Accepted.")
  print("Error: Invalid attendance status.")
  raise SystemExit

# Final Output
print("--------------------------------")
print("REGISTRATION ACCEPTED")
print("--------------------------------")
print("Student: ", student_name)
print("Section: ", section)
print("Club Choice: ", club_choice)
print("School Email: ", school_email)
print("Attendance Status: ", attendance_status)
