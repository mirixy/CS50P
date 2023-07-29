import csv


def main():
    
    sort_student_lambda(open_file())
    
    
    
def open_file():
    students = []
    
    with open ("students.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            students.append({"name": row["name"], "home": row["home"]})
    return students 
        
def sort_student_lambda(students):
    for student in sorted(students, key=lambda student: student["home"]):
        print(f"{student['name']} is from {student['home']}")

if __name__ == "__main__":
    main()