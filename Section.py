class Section:
    def __init__(self, num, nbr_students):
        self.num = num
        self.nbr_students = nbr_students
        
    def __str__(self):
        return f"Num: {self.num}, Number of students: {self.nbr_students}"