grade_points = {"A": 4.0, "B": 3.0, "C": 2.0, "D": 1.0, "F": 0.0}
points = []
for i in range(1, 6):
    grade = input(f"Enter grade for subject {i} (A, B, C, D, F): ").upper()
    if grade in grade_points:
        points.append(grade_points[grade])
    else:
        print("Invalid grade entered! Please use A, B, C, D, or F.")
        break 
    if len(points) == 5:
     gpa = sum(points) / 5  
    if gpa == 4.0:
        performance = "Excellent"
    elif gpa >= 3.0:
        performance = "Good"
    elif gpa >= 2.0:
        performance = "Needs Improvement"
    else:
        performance = "Fail"

    print(f"GPA: {gpa:.2f} - {performance}")
