def calculate_average(score1, score2, score3):
  return (score1 + score2 + score3) / 3

def get_performance(average):
  if average >= 85:
    return "Mastery"
  elif average >= 70:
    return "Developing"
  else:
    return "Needs Review"

def is_eligible(average, completed_tasks):
  if average >= 85 and completed_tasks >= 3:
    return True
  else:
    return False

score1 = float(input("Kindly enter score1: "))
score2 = float(input("Kindly enter score2: "))
score3 = float(input("Kindly enter score3: "))
completed_tasks = int(input("Completed Tasks: "))

average = calculate_average(score1, score2, score3)
performance = get_performance(average)
eligible = is_eligible(average, completed_tasks)

print(f"\nAverage: {average:.2f}")
print("Performance:", performance)
print("Eligible for Challenge:", eligible)


# Documentation Questions
# 1. Which function returns a number, which returns a string, and which returns a Boolean?
# > calculate_average() returns a number, get_performance() returns a string, and is_eligible() returns a Boolean(True or False).
# 2. Explain how the average moves from calculate_average() into get_performance().
# > The average is stored in the variable average and passed as an argument to get_performance(average).
# 3. What happens when a student has a high average but has completed fewer than three tasks?
# > The student is not eligible for the practice challenge because they completed fewer than three tasks.
# 4. Why is return more appropriate than simply printing the result inside each function?
# > return sends a value back so it can be stored, reused, or passed to another function. print() only displays the result.
