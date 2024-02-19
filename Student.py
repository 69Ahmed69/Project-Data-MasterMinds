import random
import os
import csv
from BST import BST
class Student:
    generated_ids = []
    STUDENT_PREFRENCES= (
    (1, 2, 2, 1, 0),
    (1, 2, 2, 1, 0),
    (1, 2, 2, 0, 0),
    (1, 2, 2, 1, 0),
    (2, 2, 1, 0, 0),
    (0, 0, 0, 0, 0),
    )
    def __init__(self, id, name, surname, age, major_id, year, start_year, section, group):
        if id == 0:
            self.id = self.generateStudentId(start_year)
        else:
            self.id = id
            self.generated_ids.append(id)
        self.name = name
        self.surname = surname
        self.age = age
        self.major_id = major_id
        self.year = year
        self.start_year = start_year
        self.section = section
        self.group = group
        self.left = None
        self.right = None
    
    @staticmethod
    def generateStudentId(year):
        year_suffix = str(year)[-2:]
        digits = ''.join(str(random.randint(0, 9)) for _ in range(6))
        generated_id = year_suffix + digits
        
        # Check if the generated ID already exists
        while generated_id in Student.generated_ids:
            digits = ''.join(str(random.randint(0, 9)) for _ in range(6))
            generated_id = year_suffix + digits
        
        # Add the generated ID to the list
        Student.generated_ids.append(generated_id)
        
        return generated_id
    
    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Surname: {self.surname}, Major ID: {self.major_id}, Year: {self.year}, Section: {self.section}, Group: {self.group}"


    
def generateRandomStudent(limit):
    current_directory = os.getcwd()
    csv_file_path = os.path.join(current_directory, 'Csv files', 'name.csv')
    with open(csv_file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        names = [row[0] for row in reader]
    csv_file_path = os.path.join(current_directory, 'Csv files', 'surname.csv')
    with open(csv_file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        surnames = [row[0] for row in reader]
    students = []
    for i in range(limit):
        name = random.choice(names)
        surname = random.choice(surnames)
        age = random.randint(18, 25)
        major_id = random.randint(10, 12)
        year = random.randint(1, 5)
        if year == 4 or year == 5:
            section = random.randint(1, 4)
        elif year == 3:
            section = 2
        elif major_id == 10:
            section = 1
        else:
            section = random.randint(1,2)
        start_year = 2023-year+1
        if year == 1 or year == 2:
            group = random.randint(1, 6)
        elif year == 3:
            group = random.randint(1, 2)
        else: 
            group = 1
        student = Student(0, name, surname, age, major_id, year, start_year, section, group)
        students.append(student)
    
    csv_output_path = os.path.join(current_directory, 'Csv files', 'student.csv')
    with open(csv_output_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['ID', 'Name', 'Surname', 'Age', 'MajorId', 'Year', 'Start year', 'Section', 'Group'])
        for student in students:
            writer.writerow([student.id, student.name, student.surname, student.age, student.major_id, student.year, student.start_year, student.section, student.group])
    


def readStudentFromCsv():
    bst_id = BST()
    bst_name = BST()
    current_directory = os.getcwd()
    file_path= os.path.join(current_directory, 'Csv files', 'student.csv')
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            id, name, surname, age, major_id, year, start_year, section, group = row
            student1 = Student(id, name, surname, age, major_id, year, start_year, section, group)
            student2 = Student(id, name, surname, age, major_id, year, start_year, section, group)
            bst_id.insertById(student1)
            bst_name.insertByName(student2)
    return bst_id, bst_name
    