# Ask the user to enter a student score
score = int(input("Enter a score: "))

# The score should be within the range
if score < 0 or score > 100:
  print("Invalid score.")

# Sort the scores by their classfication
elif score >= 90:
  print("Outstanding")
elif score >= 80:
  print("Very Satisfactory")
elif score >= 75:
  print("Satisfactory")
else:
  print("Needs improvement")
