# Input Validation and Output Verification
**Activity:** PSHS Workshop Registration Validator

**Name:** Naomi Krsitelle Mae L. Belleza

**Section:** Dahlia

**Quarter:** 1
---
## Activity Overview
In this activity, I created a program that validates information entered into a PSHS workshop registration
system.
The program checks whether user input satisfies specific requirements before accepting the registration.
The program validates:
- student name
- age
- grade level
- email address and
- registration code.

---
# Part A - Validation Requirements
Complete the table below before writing your program.


| Data Captured | Expected Input | Validation Type | Invalid Input Example | Validation Rule | Error Message |
|---|---|---|---|---|---|
| Student Name | Non-blank text | Presence Validation | "" | Name must not be blank | A student name is required. |
| Age | Integer from 11 to 18 | Data Type and Range Validation | fourteen / 10 | Age must be an integer and must be from 11 to 18 | Age must be between 11 and 18. / Age is required to be a number. |
| Grade Level | 7, 8, 9, 10, 11, or 12 | Acceptable Value Validation | 13 | Grade level must be from 7 to 12 | Invalid grade level. |
| Email Address | Text containing @ | Pattern Validation | studentpshs.edu.ph | Email must contain @ | Invalid email. |
| Registration Code | Exactly only 6 characters | Length Validation | ABC | Code must contain exactly only 6 characters | The registration code must contain 6 characters. |
---
## Validation Questions
### 1. Why should the student name not be blank?
> The name is needed to ensure who the person registering is.
### 2. Why should age be checked for both data type and range?
> It should be an integer and must be within the range of 11 to 18.
### 3. Why should grade level only accept specific values?
> This prevents the invalid grade levels from being accepted by the program.
### 4. What format requirements did you use for the email address?
> The email address must contain a @.
### 5. What length requirement did you use for the registration code?
> The registration code must contain exactly 6 characters.
---
# Part B - Program Design
Before writing your program, create either a **flowchart or pseudocode** showing its logic.
## Pseudocode

```text
START

INPUT student name
IF student name is blank
  DISPLAY "REGISTRATION NOT ACCEPTED"
  STOP
END IF

INPUT age
IF age is not a number OR age < 11 OR age > 18
  DISPLAY "REGISTRATION NOT ACCEPTED"
  STOP
END IF

INPUT email
IF email does not contain "@"
  DISPLAY "REGISTRATION NOT ACCEPTED"
  STOP
END IF

INPUT registration code
IF registration code length != 6
  DISPLAY "REGISTRATION NOT ACCEPTED"
  STOP
END IF

DISPLAY "REGISTRATION ACCEPTED"
DISPLAY student name, age, grade level, email, registration code

END
```
---
# Part C - Program Implementation
## Programming Language
> Python
## Source Code File
![workshop_validator.py](./workshop_validator.py)
## Final Code
```python
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
```
---
## Validation Techniques Used
### Presence Validation
Explain where you used presence validation.
> I used presence validation for the student name by checking if SName is empty. If it is, the program displays "REGISTRATION NOT ACCEPTED " and "A student name is required."
### Data Type Validation
Explain where you used data type validation.
> I used data type validation for the age and grade level by converting the input into integers using int(). If the user enters anything other than integers between the ranges, the program catches the ValueError and displays the error message.
### Range Validation
Explain where you used range validation.
> I used range validation for the age. The program only accepts ages from 11 to 18. If the age is below 11 or above 18, the registration is rejected.
### Acceptable Value Validation
Explain where you used acceptable value validation.
> I used acceptable value validation for the grade level. The program accepts grade levels from 7 to 12 and rejects values outside this range.
### Pattern Validation
Explain the simple pattern rule you used.
> I used simple pattern validation for the email. The program checks if the email contains the @ symbol. If it does not contain @, the email is rejected.
### Length Validation
Explain the length rule you used.
> I used length validation for the registration code. The program checks if the registration code has exactly 6 characters. If the length is not 6, the registration is rejected.
---
# Part D - Testing
Test your program using both valid and invalid inputs.
| Test | Input / Condition | Validation Being Tested | Expected Output | Actual Output | Result |
|---:|---|---|---|---|---|
| 1 | All inputs valid | Normal case | Student details are displayed. | Student details are displayed. | PASS |
| 2 | Blank student name | Presence | A student name is required. | A student name is required. | PASS |
| 3 | Age = `fourteen` | Data type | Age is required to be a number. | Age is required to be a number. | PASS |
| 4 | Age = `11` | Minimum boundary | Student details are displayed. | Student details are displayed. | PASS |
| 5 | Age = `18` | Maximum boundary | Student details are displayed. | Student details are displayed. | PASS |
| 6 | Age = `10` | Range | Age must be between 11 and 18. | Age must be between 11 and 18. | PASS |
| 7 | Grade Level = `13` | Acceptable value | Invalid grade level. | Invalid grade level. | PASS |
| 8 | Email = `studentpshs.edu.ph` | Pattern | Invalid email. | Invalid email. | PASS |
| 9 | Registration Code = `ABC` | Length | The registration code must contain 6 characters. | The registration code must contain 6 characters. | PASS |
| 10 | Registration Code = `CS2026` | Valid length | Student details are displayed. | Student details are displayed | |
Write **PASS** when the actual output matches the expected output.
Write **FAIL** when it does not.
---
# Part E - Output Verification
Choose any **three tests** from Part D.
## Verification Test 1
**Input:**
```text
Age = fourteen

```
**Expected Output:**
```text
REGISTRATION NOT ACCEPTED
Age is required to be a number.
```
**Actual Output:**
```text
REGISTRATION NOT ACCEPTED
Age is required to be a number.
```
**Result:** PASS 
**Explanation:**
> The age was not entered as an integer, so the program rejected it.
---
## Verification Test 2
**Input:**
```text
Email = studentpshs.edu.ph
```
**Expected Output:**
```text
REGISTRATION NOT ACCEPTED
Invalid email.
```
**Actual Output:**
```text
REGISTRATION NOT ACCEPTED
Invalid email.
```
**Result:** PASS 
**Explanation:**
> The email did not contain a @, so the program rejected it.
---
## Verification Test 3
**Input:**
```text
CS2026
```
**Expected Output:**
```text
Student details are displayed.
```
**Actual Output:**

```text
Student details are displayed.
```
**Result:** PASS
**Explanation:**
> CS2026 contains exactly 6 characters, so it passes the registration code validation.
---
# Reflection
Answer briefly.
### 1. Why should a program validate input before processing it?
> To prevent incorrect inputs and errors in the program.
### 2. What is the difference between input validation and output verification?
> Input validation checks if the data is valid, while the output verification checks if the result is correct.
### 3. Which validation technique was easiest for you to implement? Why?
> Presence validation was the easiest for me because I only had to check if the name was blank or empty,
### 4. Which validation technique was most challenging? Why?
> Data type validation was the most challenging due to the fact that I had to handle inputs that were not integers.
### 5. How did testing invalid inputs help you improve your program?
> It helped me make sure that the program properly rejected invalid outputs.
