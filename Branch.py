import Year
class Branch:
    branch_list = []

    def __init__(self, name, branch_id, num_years):
        self.name = name
        self.branch_id = branch_id
        self.num_years = num_years
        self.years = [None for _ in range (1, num_years)]
        Branch.branch_list.append(self)

    def __str__(self):
        return f"Name: {self.name}, ID: {self.branch_id}, Num Years: {self.num_years}"
