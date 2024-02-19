import math
from Section import Section
class Year:
    year_list = []
    
    def __init__(self, num, name, nbr_students, capacity, nbr_sections):
        self.num = num
        self.name = name
        self.capacity = capacity
        if nbr_students < capacity:
            self.nbr_students = nbr_students
        else:
            print("Number of students exceeds capacity")
            return    
        self.semesters = [None for _ in range(2)]
        if nbr_sections > 0:
            self.nbr_sections = nbr_sections
        else:
            self.nbr_sections = self.divideSections()
        self.sections = []
        Year.year_list.append(self)
        
    def __str__(self):
        return f"Name: {self.name}, Capacity: {self.capacity}, Number of students: {self.nbr_students}"
    
    def divideSections(self):
        if self.nbr_students <= 0:
            return 0
        else:
            nbr_sections = math.ceil(self.nbr_students / self.capacity)
            student_numbers = createStudentNumbers(self.nbr_students, nbr_sections)
            for i in range(nbr_sections):
                self.sections.append(Section(i, student_numbers[i]))
            return nbr_sections
        
def createStudentNumbers(total_students, num_sections):
    base_students_per_section = total_students // num_sections
    extra_sections = total_students % num_sections
    student_numbers = [base_students_per_section + 1] * extra_sections + [base_students_per_section] * (num_sections - extra_sections)
    return student_numbers
