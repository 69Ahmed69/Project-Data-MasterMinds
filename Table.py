import Session

class Table:
    def __init__(self, branch_id, year, section, group):
        self.branch_id = branch_id
        self.year = year
        self.section = section
        self.group = group
        self.sessions = [[None]*6 for _ in range(6)]  # 6x6 grid for sessions

    def __str__(self):
        return f"Branch ID: {self.branch_id}, Year: {self.year}, Section: {self.section}, Group: {self.group}"

    def set_session(self, row, col, session):
        if 0 <= row < 6 and 0 <= col < 6:
            self.sessions[row][col] = session
        else:
            print("Index out of range.")