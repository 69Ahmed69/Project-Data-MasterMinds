import Session

class Table:
    def __init__(self, branch_id, year, section, group):
        self.branch_id = branch_id
        self.year = year
        self.section = section
        self.group = group
        self.sessions = [[None]*5 for _ in range(5)]  # 5x5 grid for sessions

    def __str__(self):
        return f"Branch ID: {self.branch_id}, Year: {self.year}, Section: {self.section}, Group: {self.group}"

    def set_session(self, row, col, session):
        if 0 <= row < 5 and 0 <= col < 5:
            self.sessions[row][col] = session
        else:
            print("Index out of range.")