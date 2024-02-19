

class Group:
    def __init__(self, num, nbr_students):
        self.num = num
        self.nbr_students = nbr_students
        self.table = []
        for _ in range(6):
            row = [None] * 6
            self.table.append(row)
        self.students = []
    
    def __str__(self):
        return f"Num: {self.num}, Number of students: {self.nbr_students}"