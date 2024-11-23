gpa = float(input("Enter the student's GPA: "))
credits = int(input("Enter the number of credits completed: "))
final_exam_passed = input("Has the student passed the final comprehensive exam? (true/false): ")

if gpa >= 2.5 and credits >= 120:
    if gpa < 3.0 and final_exam_passed.lower() != "true":
        print("The student is not eligible for graduation.")
    else:
        print("The student is eligible for graduation.")
else:
    print("The student is not eligible for graduation.")