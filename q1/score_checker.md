# Clean Decision Code Makeover: Student Score Checker
**Name:** Naomi Kristelle Mae L. Belleza

**Section:** Dahlia
---
## Activity Overview

In this activity, I improved a Student Score Checker program by making the code more readable, organized, and safe.
The program accepts a student score from 0 to 100 and determines its classification.

The classifications are:

| Score | Classification |
|---:|---|
| 90–100 | Outstanding |
| 80-89 | Very Satisfactory |
| 75-80 | Satisfactory |
| 0–74 | Needs Improvement |

Scores below 0 or above 100 are considered invalid.

# Part 1 - Analyze the Logic
## Input
What information does the program need?
> The program needs the student's score as input.

## Valid Range
**Minimum valid score:**
> 0
**Maximum valid score:**
> 100

## Possible Outputs
List all possible outputs of the program.
1. Outstanding
2. Very Satisfactory
3. Satisfactory
4. Needs Improvement
5. Invalid

## Boundary Condition
What condition will you use to determine whether the score is valid?
> The score is valid if it is between 0 and 100. Scores below or above the range are invalid.
>  
## Multiple Decision Paths
Explain how the program decides which classification should be displayed.
> The grade classification uses multiple decision paths because the program checks different score ranges using is, elif, and else.
---
# Part 2 - Flowchart
## Flowchart
![Score Checker Flowchart](./score_checker_flowchart.png)

---
# Part 3 - Pseudocode
START

INPUT score

IF score < 0 OR score > 100 THEN
  DISPLAY "Invalid score."
ELSE IF score >= 90 THEN
  DISPLAY "Outstanding"
ELSE IF score >= 80 THEN
  DISPLAY "Very Satisfactory"
ELSE IF score >= 75 THEN
  DISPLAY "Satisfactory"
ELSE
  DISPLAY "Needs improvement"
END IF

END
---
# Part 4 - Clean Code Implementation
## Source Code
![Score Checker Source Code](./score_checker.py)
---
# Part 5 - Testing
| Test | Input | Purpose | Expected Output | Actual Output | Result |
| --- | ---: | --- | --- | --- | --- |
| 1 | -1 | Below minimum | Invalid score. | Invalid score. | PASS |
| 2 | 0 | Minimum boundary | Needs improvement | Needs improvement | PASS |
| 3 | 74 | Below Satisfactory boundary | Needs improvement | Needs improvement | PASS |
| 4 | 75 | Satisfactory boundary | Satisfactory | Satisfactory | PASS |
| 5 | 80 | Very Satisfactory boundary | Very Satisfactory | Very Satisfactory | PASS |
| 6 | 90 | Outstanding boundary | Outstanding | Outstanding | PASS |
| 7 | 100 | Maximum boundary | Outstanding | Outstanding | PASS |
| 8 | 101 | Above maximum | Invalid score. | Invalid score. | PASS |
---

## Testing Reflection
### 1. Why is it important to test the values 0 and 100?
> Because these numbers are the minimum and maximum valid scores, so testing them makes sure the limits work correctly.
### 2. Why did you also test -1 and 101?
> They are outside the valid range of scores and makes sure that the program identifies them as invalid scores.
### 3. Which test helped you understand boundary conditions the most?
> Testing the numbers 75, 80, and 90 because those are the points where  the classification changes.
### 4. Did any of your tests initially fail? If yes, what did you change in your program?
> No, all of my tests passed the conditions and outputs.

---

# Reflection
### 1. How did selection structures make the program more useful?
> Selection structures allowed the program to make sure different decisions based on the student's score and give the correct classification
### 2. How did proper comments and readable formatting improve your program?
> They made the code easier to read, understand, and check for mistakes.
### 3. Why is it useful to plan the program using a flowchart and pseudocode before writing the code?
> It helps organize the steps and logic of the program before writing the actual code.
