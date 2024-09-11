import json

with open('student.json', 'r') as file:
    data = json.load(file)

students = data['students']
for student in students:
    print(f"ID: {student['id']}")
    print(f"Name: {student['name']}")
    print(f"Age: {student['age']}")
    print(f"Math Grade: {student['grades']['math']}")
    print(f"Science Grade: {student['grades']['science']}")
    print()  # Print a newline for better readability

file.close()

newdata = {
    "id": 3,
    "name": "John",
    "age": 21,
    "grades": {
    "math": 80,
    "science": 89
    }
}

with open('student.json', 'w') as file:
    students.append(newdata)
    json.dump(data, file, indent=4)