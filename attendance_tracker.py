# Module 3: Attendance Tracker
def check_attendance(student_name, attended_classes, total_classes):
    percentage = (attended_classes / total_classes) * 100
    status = "Eligible for Exam" if percentage >= 75 else "Short Attendance"
    return f"{student_name}: {percentage:.1f}% ({status})"

if __name__ == "__main__":
    print(check_attendance("Fatima Bukhari", 28, 32))
    print(check_attendance("Ali Khan", 20, 32))