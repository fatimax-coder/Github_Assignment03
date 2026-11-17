# Module 2: Grade & GPA Calculator
def calculate_grade(marks):
    if marks >= 85:
        return "A", 4.0
    elif marks >= 75:
        return "B", 3.3
    elif marks >= 65:
        return "C", 2.5
    elif marks >= 50:
        return "D", 1.5
    return "F", 0.0

if __name__ == "__main__":
    grade, gpa = calculate_grade(88)
    print(f"Marks: 88 | Grade: {grade} | GPA: {gpa}")
