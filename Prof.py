import random
import os
import csv, sqlite3
from BST import BST
class Prof:
    min_hours = 9
    max_hours = 12
    generated_ids = []
    def __init__(self, id, name, surname, age, exp, nbr_hours, preferences, table_id):
        if id == 0:
            self.id = self.generateProfId()
        else:
            self.id = id
            self.generated_ids.append(id)
        self.name = name
        self.surname = surname
        self.age = age
        self.exp = exp
        self.nbr_hours = nbr_hours
        self.preferences = self.preferencesToList(preferences)
        self.table_id = table_id
        self.courses = []
        self.right = None
        self.left = None



        
    def preferencesToList(self, preferences):
        if len(preferences) != 36:
            raise ValueError("Input preferences must be exactly 36 characters long.")

        result = []
        for i in range(0, len(preferences), 1): 
            result.append(int(preferences[i:i+1]))  

        result = [result[i:i+6] for i in range(0, len(result), 6)]

        return result
    
    def preferencesToString(self, matrix):
        if len(matrix) != 6 or any(len(row) != 6 for row in matrix):
            raise ValueError("Input matrix must be a 6x6 list.")
        else:
            flat_list = [str(item) for row in matrix for item in row]
            preferences_string = ''.join(flat_list)

        return preferences_string
    
    def generateProfId(self):
        id = random.randint(10000,99999)
        while id in Prof.generated_ids:
            id = random.randint(10000,99999)
        Prof.generated_ids.append(id)
        return id

    def __str__(self):
        return f"Id: {self.id} Name: Dr.{self.name} {self.surname} Age: {self.age} Exp: {self.exp}"


def generateRandomProf(limit):
    current_directory = os.getcwd()
    csv_file_path = os.path.join(current_directory, 'Csv files', 'name.csv')
    with open(csv_file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        names = [row[0] for row in reader]
    csv_file_path = os.path.join(current_directory, 'Csv files', 'surname.csv')
    with open(csv_file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        surnames = [row[0] for row in reader]
    profs = []
    for i in range(limit):
        random_name = random.choice(names)
        random_surname = random.choice(surnames)
        random_age = random.randint(30, 58)
        random_exp = random.randint(1, 3)
        random_pref = ''.join(str(random.randint(0, 4)) for _ in range(36))
        prof = Prof(0, random_name, random_surname, random_age, random_exp, 0, random_pref, 0)
        profs.append(prof)
    
    csv_output_path = os.path.join(current_directory, 'Csv files', 'prof.csv')
    with open(csv_output_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['id', 'Name', 'Surname', 'Age', 'Experience', 'Number of hours', 'Course', 'Preferences', 'Time table id'])
        for prof in profs:
            writer.writerow([prof.id, prof.name, prof.surname, prof.age, prof.exp, prof.nbr_hours, prof.courses, prof.preferencesToString(prof.preferences), prof.table_id])



def readProfFromCsv():
    bst_name = BST()
    bst_id = BST()
    current_directory = os.getcwd()
    file_path = os.path.join(current_directory, 'Csv files', 'prof.csv')
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            id, name, surname, age, exp, nbr_hours, preferences, table_id = row
            prof1 = Prof(id, name, surname, age, exp, nbr_hours, preferences, table_id)
            prof2 = Prof(id, name, surname, age, exp, nbr_hours, preferences, table_id)
            bst_name.insertByName(prof1)
            bst_id.insertById(prof2)
        return bst_id, bst_name

    
def updateProfDatabase(bst):
    """
    Deletes the existing "Professors" table and creates a new one with updated data from the BST.

    Args:
        bst: The binary search tree containing Prof objects.
    """

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Drop the table if it exists
    cursor.execute("DROP TABLE IF EXISTS Professors")

    # Create a new Professors table 
    cursor.execute("""
        CREATE TABLE Professors (
            id INTEGER PRIMARY KEY,
            name TEXT,
            surname TEXT,
            age INTEGER,
            exp INTEGER,
            nbr_hours INTEGER,
            preferences TEXT,
            table_id INTEGER
        )
    """)

    # Recursive function to traverse the BST and insert records
    def insert_prof(prof):
        if prof:
            cursor.execute("""
                INSERT INTO Professors (id, name, surname, age, exp, nbr_hours, preferences, table_id)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (prof.id, prof.name, prof.surname, prof.age, prof.exp, prof.nbr_hours, prof.preferencesToString(prof.preferences), prof.table_id))

            insert_prof(prof.left)
            insert_prof(prof.right)

    # Start the traversal from the root of the BST
    insert_prof(bst.root)

    # Commit the changes to the database
    conn.commit()

    

def readProfDatabase():
    """
    Reads data from the "Professors" database and populates a binary search tree (BST) with Prof objects.

    Returns:
        A binary search tree (BST) containing Prof objects.
    """
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Check if the Professors table exists
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Professors'")
    table_exists = cursor.fetchone()
    bst = BST()
    if table_exists:
        # Create an empty BST
        
        # Read data from the Professors table
        cursor.execute("SELECT * FROM Professors")
        rows = cursor.fetchall()

        # Populate the BST with Prof objects
        for row in rows:
            prof = Prof(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
            bst.insertById(prof)

        conn.close()
        return bst
    else:
        conn.close()
        return bst

