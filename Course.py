import random
import os
import csv
from BST import BST
import sqlite3
from PyQt6.QtWidgets import QMessageBox

class Course:
    generated_ids = []
    def __init__(self, id, name, cof, cour, td, tp):
        if id == 0:
            self.id = self.generateCourseId()
        else:
            self.id = id
            Course.generated_ids.append(id)
        self.name = name
        self.cof = cof
        self.cour = cour
        self.td = td
        self.tp = tp
        self.profs = []
        self.left = None
        self.right = None

    def __str__(self):
        return f"Name='{self.name}', id={self.id}, cof={self.cof}, cour={self.cour}, td={self.td}, tp={self.tp}"
    
    def generateCourseId(self):
        id = random.randint(1000,9999)
        while id in Course.generated_ids:
            id = random.randint(1000,9999)
        Course.generated_ids.append(id)
        return id

def readCourseFromCsv():
    bst_name = BST()
    bst_id = BST()
    current_directory = os.getcwd()
    file_path = os.path.join(current_directory, 'Csv files', 'course.csv')
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            id, name, cof, cour, td, tp = row
            course1 = Course(int(id), name, cof, cour, td, tp)
            course2 = Course(int(id), name, cof, cour, td, tp)
            bst_name.insertByName(course1)
            bst_id.insertById(course2)
    return bst_id, bst_name

def updateCourseDatabase(bst):

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Drop the table if it exists
    cursor.execute("DROP TABLE IF EXISTS Courses")

    # Create a new Courses table 
    cursor.execute("""
        CREATE TABLE Courses (
            id INTEGER PRIMARY KEY,
            name TEXT,
            cof INTEGER,
            cour INTEGER,
            td INTEGER,
            tp INTEGER
        )
    """)

    # Recursive function to traverse the BST and insert records
    def insert_course(course):
        if course:
            cursor.execute("""
                INSERT INTO Courses (id, name, cof, cour, td, tp)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (course.id, course.name, course.cof, course.cour, course.td, course.tp))

            insert_course(course.left)
            insert_course(course.right)

    # Start the traversal from the root of the BST
    insert_course(bst.root)

    # Commit the changes to the database
    conn.commit()
    conn.close()

    

def readCourseDatabase():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Check if the Courses table exists
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Courses'")
    table_exists = cursor.fetchone()
    bst = BST()
    if table_exists:      
        # Read data from the Courses table
        cursor.execute("SELECT * FROM Courses")
        rows = cursor.fetchall()

        # Populate the BST with Prof objects
        for row in rows:
            course = Course(row[0], row[1], row[2], row[3], row[4], row[5])
            bst.insertById(course)
    else:
        QMessageBox.critical(None, 'Empty Course Database', 'Please import a CSV with your courses.')
    conn.close()
    return bst

