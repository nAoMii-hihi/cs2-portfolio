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

```
---
# Part C - Program Implementation
## Programming Language
> Python
## Source Code File

## Final Code
```python
# Paste your final code here.
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
| 1 | All inputs valid | Normal case | | | |
| 2 | Blank student name | Presence | | | |
| 3 | Age = `fourteen` | Data type | | | |
| 4 | Age = `11` | Minimum boundary | | | |
| 5 | Age = `18` | Maximum boundary | | | |
| 6 | Age = `10` | Range | | | |
| 7 | Grade Level = `13` | Acceptable value | | | |
| 8 | Email = `studentpshs.edu.ph` | Pattern | | | |
| 9 | Registration Code = `ABC` | Length | | | |
| 10 | Registration Code = `CS2026` | Valid length | | | |
Write **PASS** when the actual output matches the expected output.
Write **FAIL** when it does not.
---
# Part E - Output Verification
Choose any **three tests** from Part D.
## Verification Test 1
**Input:**
```text
Write the input here.

```
**Expected Output:**
```text
Write the expected output here.
```
**Actual Output:**
```text
Write the actual output here.
```
**Result:** PASS / FAIL
**Explanation:**
> Explain why the output is correct or incorrect.
---
## Verification Test 2
**Input:**
```text
Write the input here.
```
**Expected Output:**
```text
Write the expected output here.
```
**Actual Output:**
```text
Write the actual output here.
```
**Result:** PASS / FAIL
**Explanation:**
> Explain why the output is correct or incorrect.
---
## Verification Test 3
**Input:**
```text
Write the input here.
```
**Expected Output:**
```text
Write the expected output here.
```
**Actual Output:**

```text
Write the actual output here.
```
**Result:** PASS / FAIL
**Explanation:**
> Explain why the output is correct or incorrect.
---
# Reflection
Answer briefly.
### 1. Why should a program validate input before processing it?
> Write your answer here.
### 2. What is the difference between input validation and output verification?
> Write your answer here.
### 3. Which validation technique was easiest for you to implement? Why?
> Write your answer here.
### 4. Which validation technique was most challenging? Why?
> Write your answer here.
### 5. How did testing invalid inputs help you improve your program?
> Write your answer here.
