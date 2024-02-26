import random
import os
import csv
from BST import BST
import sqlite3
from PyQt6.QtWidgets import QMessageBox

class Teaching:
    def __init__(self, prof_id, course_id):
        self.prof_id = prof_id
        self.course_id = course_id
        self.right = None
        self.left = None
    
    def __str__(self):
        return f" Prof ID: {self.prof_id}, Course ID: {self.course_id}"
    
def readTeachingFromCsv():
    bst_id = BST()
    bst_id2 = BST()
    current_directory = os.getcwd()
    file_path = os.path.join(current_directory, 'Csv files', 'teaching.csv')
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            prof_id, course_id = row
            teaching = Teaching(int(prof_id), int(course_id))
            teaching2 = Teaching(int(prof_id), int(course_id))
            bst_id.insertByProfId(teaching)
            bst_id2.insertByCourseId(teaching2)
    return bst_id, bst_id2
    
def updateTeachingDatabase(bst):

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Drop the table if it exists
    cursor.execute("DROP TABLE IF EXISTS Teaching")

    # Create a new Teachings table 
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Teaching (
        prof_id INTEGER,
        course_id INTEGER,
        FOREIGN KEY (course_id) REFERENCES Courses(course_id),
        FOREIGN KEY (prof_id) REFERENCES Professors(prof_id),
        PRIMARY KEY (prof_id, course_id)
    )
    ''')

    # Recursive function to traverse the BST and insert records
    def insert_teaching(teaching):
        if teaching:
            cursor.execute("""
                INSERT INTO Teaching (prof_id, course_id)
                VALUES (?, ?)
            """, (teaching.prof_id, teaching.course_id))

            insert_teaching(teaching.left)
            insert_teaching(teaching.right)

    # Start the traversal from the root of the BST
    insert_teaching(bst.root)

    # Commit the changes to the database
    conn.commit()
    conn.close()
    
def readTeachingDatabase():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Check if the Teaching table exists
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Teaching'")
    table_exists = cursor.fetchone()
    bst = BST()
    bst2 = BST()
    if table_exists:      
        # Read data from the Teaching table
        cursor.execute("SELECT * FROM Teaching")
        rows = cursor.fetchall()

        # Populate the BST with Prof objects
        for row in rows:
            teaching = Teaching(row[0], row[1])
            teaching2 = Teaching(row[0], row[1])
            bst.insertByCourseId(teaching)
            bst2.insertByCourseId(teaching2)
    else:
        QMessageBox.critical(None, 'Empty Teaching Database', 'Please import a CSV with your Teaching.')
    conn.close()
    return bst, bst2

if __name__ == '__main__':
    bst_id = BST()
    bst_id2 = BST()
    #bst_id, bst_id2 = readTeachingFromCsv()
    #updateTeachingDatabase(bst_id)
    bst_id, bst_id2 = readTeachingDatabase()
    bst_id.printInOrder()
    bst_id2.printInOrder()