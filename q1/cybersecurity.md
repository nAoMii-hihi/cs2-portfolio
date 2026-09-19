# Fundamentals of Cybersecurity and Data Privacy
**Activity:** PSHS Secure Club Registration System 

**Name:** Naomi Kristelle Mae L. Belleza

**Section:** Dahlia

**Quarter:** 1 
---

## Activity Overview
In this activity, I learned about cybersecurity and data privacy. I checked for possible threats and made a simple club registration program that storages information safely. The goal is to keep information safe and ensures the program only accepts correct data.
---

# Part A - Cybersecurity Threat Analysis
## Assigned Case

**Case Number:** 1
**Case Title: Fake Login Alert**
> A message claims that the student's account will be disabled and asks them to click a link and enter their
username and password.
---
### 1. What cybersecurity threat is shown?
> The threat shown is **phishing**. It is an attempt to trick a user into giving private account information through a fake message or link.
### 2. What warning signs make the situation suspicious?
> The message threatens that the account will be disabled and asks the student to click a link and enter their username and password. These are warning sighs because the message may not come from a trusted school source.
### 3. What may be affected?
Check or describe all that apply:
- Data
- Account
- Application
- Device
- Network
  
> The student's account information could be stolen. The link could also lead to a harmful website or application that may affect the device or network.
### 4. What information could be exposed or misused?
> The student's username and password could be exposed. If stolen, they could be used to access the student's account and possibly other private information. 
### 5. What should the user do to reduce the risk?
> The user should not click the link nor enter their password. They should verify the message through an official school channel and report the suspicious message if necessary.
---

# Part B - Data Privacy and Secure Data Capture
A proposed Club Registration System wants to collect the following information.
Determine whether each item is really necessary.
| Data | Collect / Do Not Collect | Reason |
|---|---|---|
| Student Name | Collect | Needed to identify the student. |
| Section | Collect | Needed to identify the student's section. |
| Club Choice | Collect | Needed to identify which club the student selected. |
| School Email | Collect | Needed for school-related communication. |
| Attendance Status | Collect | Needed to record the student's attendance status. |
| Password | Do Not Collect | Not necessary for club registration. |
| OTP | Do Not Collect | Not needed for the activity. |
| Home Address | Do Not Collect | Not necessary for club registration. |
| Parent Bank Account | Do Not Collect | Financial information is unnecessary for this activity. |

## Privacy Question
Why is it safer to collect only information that the program actually needs?
> It is safer to collect only needed information to reduce the amount of data that could be exposed or misused. It also protects the user's privacy.

---
# Part C - Security-Focused Validation Rules
Complete the table before writing your program.
| Data Captured | Expected Input | Possible Risk | Invalid Input Example | Validation Rule | Error Message |
|---|---|---|---|---|---|
| Student Name | | | | | |
| Section | | | | | |
| Club Choice | | | | | |
| School Email | | | | | |
| Attendance Status | | | | | |
---

## Secure Data Capture Questions
### 1. What should your program accept?
> Write your answer here.
### 2. What should your program reject?
> Write your answer here.
### 3. How do your validation rules help reduce incorrect or unsafe input?
> Write your answer here.
---

# Part D - Secure Program Implementation
## Source Code
![secure_registration.py](./secure_registration.py)
---

## Final Code
```python
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
```
