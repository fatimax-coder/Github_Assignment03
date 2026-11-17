# Module 1: Student Registration
students = []

def register_student(student_id, name, department):
    student = {
        "id": student_id,
        "name": name,
        "department": department
    }
    students.append(student)
    return f"Registered: {name} (ID: {student_id}, Dept: {department})"

if __name__ == "__main__":
    print(register_student(101, "Fatima Bukhari", "Software Engineering"))
    print(register_student(102, "Ali Khan", "Computer Science"))
