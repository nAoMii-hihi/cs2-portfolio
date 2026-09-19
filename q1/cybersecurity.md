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
| Student Name | A Non-Blank Name | Missing Identity | Blank | Must Not Be Blank | Student name is required. |
| Section | Dahlia | Wrong section | Rosal | Must Equal Dahlia | Invalid section. |
| Club Choice | SIGMa, English, Polaris, BahayNayan, Dance Troupe, Sports | Invalid Club Choice | Programming | Must Be One of The Allowed Clubs | Kindly choose a valid club. |
| School Email | School Email containing "@" and "." | Invalid Email Format | studentpshs.edu.ph | Must Contain "@" and "." | Kindly enter a valid school email. |
| Attendance Status | Present, Absent, Late | Invalid Attendance Record | Maybe | Must Be One of The Allowed Values | Invalid attendance status. |
---

## Secure Data Capture Questions
### 1. What should your program accept?
> The program should accept a non-blank name, the correct section, a valid club choice, a valid school email, and an allowed attendance status.
### 2. What should your program reject?
> The program should reject blank names, invalid sections, invalid club choices, incorrectly formatted emails, and invalid attendance statuses.
### 3. How do your validation rules help reduce incorrect or unsafe input?
> The validation rules prevent incorrect values from being accepted. They also make sure that the program collects only the expected information.
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
---

## Security Practices Applied
### Required Input
Explain how you handled blank input.
> Blank student names are rejected because a student name is required for registration.

### Allowed Values
Explain which fields accept only predefined values.
> Section, club choices, and attendance status only accept predefined values. This prevents invalid inputs from being accepted.

### Format Check
Explain your simple email validation rule.
> The email must contain "@" and ".". This provides a simple check for the required email format.

### Error Messages
Explain why clear error messages are useful.
> Clear error messages tell the user what went wrong so they know what needs to be corrected.

### Data Minimization
Explain what information you intentionally did NOT collect and why.
> The program does not collect passwords, OTPs, home addresses, or baking information because these are unnecessary for club registration.
---
# Part E - Testing and Reflection
## Testing
| Test | Input Situation | Expected Output | Actual Output | Result |
|---:|---|---|---|---|
| 1 | All data valid | Registration Accepted | Registration Accepted | PASS |
| 2 | Blank student name | Rejected | Rejected | PASS |
| 3 | Invalid section | Rejected | Rejected | PASS |
| 4 | Invalid club choice | Rejected | Rejected | PASS |
| 5 | Email missing @ | Rejected | Rejected | PASS |
| 6 | Email missing . | Rejected | Rejected | PASS |
| 7 | Invalid attendance status | Rejected | Rejected | PASS |
| 8 | Different valid inputs | Accepted | Accepted | PASS |
Use:
- *PASS* if the actual result matches the expected result.
- *FAIL* if it does not.
  
---

# Reflection
### 1. What is one cybersecurity threat that can affect an application or user?
> One cybersecurity threat is phishing. It can trick users into giving away private information such as usernames and passwords.

### 2. How can users reduce the risk of phishing or suspicious messages?
> Users can avoid clicking suspicious links, check the sender, and verify messages through official sources before providing information.

### 3. How can validation rules improve the security of user input?
> Validation rules ensure that only accepted and appropriate information is accepted. They can prevent incorrect or unsafe input from entering the program.

### 4. Why should a program avoid collecting unnecessary personal information?
> A program should avoid unnecessary personal information because less collected data means less information that could be exposed or misused.

### 5. How did SG7's input validation concepts become security practices in SG8?
> SG7 taught me how to check and validate data input. In SG 8, I used these skills to make sure the program accepts only correct and safe information.
