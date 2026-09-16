student_name = input("enter student name: ")
marks = int(input("Enter your marks: "))
if marks < 0 or marks > 100:
  print("Invalid marks")
else:
  print("========== RESULT ==========")
  print("Student:",student_name)
  print("Marks:",marks)
  if marks >= 90:
    print("Grade: A")
  elif marks >= 75:
    print("Grade: B")
  elif marks >= 60:
    print("Grade: C")
  elif marks >= 40:
    print("Grade: D")
  else:
    print("Grade: Fail")
  print("=============================")