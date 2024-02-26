import os, csv


class BST:
    def __init__(self):
        self.root = None

    def insertById(self, node):
        if not self.root:
            self.root = node
        else:
            self._insertById(self.root, node)

    def _insertById(self, current_node, new_node):
        if new_node.id < current_node.id:
            if current_node.left is None:
                current_node.left = new_node
            else:
                self._insertById(current_node.left, new_node)
        elif new_node.id > current_node.id:
            if current_node.right is None:
                current_node.right = new_node
            else:
                self._insertById(current_node.right, new_node)
                
    def insertByProfId(self, node):
        if not self.root:
            self.root = node
        else:
            self._insertByProfId(self.root, node)

    def _insertByProfId(self, current_node, new_node):
        if new_node.prof_id < current_node.prof_id:
            if current_node.left is None:
                current_node.left = new_node
            else:
                self._insertByProfId(current_node.left, new_node)
        elif new_node.prof_id > current_node.prof_id:
            if current_node.right is None:
                current_node.right = new_node
            else:
                self._insertByProfId(current_node.right, new_node)
    
    def insertByCourseId(self, node):
        if not self.root:
            self.root = node
        else:
            self._insertByCourseId(self.root, node)

    def _insertByCourseId(self, current_node, new_node):
        if new_node.course_id < current_node.course_id:
            if current_node.left is None:
                current_node.left = new_node
            else:
                self._insertByCourseId(current_node.left, new_node)
        elif new_node.course_id > current_node.course_id:
            if current_node.right is None:
                current_node.right = new_node
            else:
                self._insertByCourseId(current_node.right, new_node)
                
    def insertByNameOnly(self, node):
        if not self.root:
            self.root = node
        else:
            self._insertByNameOnly(self.root, node)

    def _insertByNameOnly(self, current_node, new_node):
        if new_node.name < current_node.name:
            if current_node.left is None:
                current_node.left = new_node
            else:
                self._insertByNameOnly(current_node.left, new_node)
        elif new_node.name > current_node.name:
            if current_node.right is None:
                current_node.right = new_node
            else:
                self._insertByNameOnly(current_node.right, new_node)
    
    def insertByName(self, node):
        if not self.root:
            self.root = node
        else:
            self._insertByName(self.root, node)

    def _insertByName(self, current_node, new_node):
        if new_node.name < current_node.name:
            if current_node.left is None:
                current_node.left = new_node
            else:
                self._insertByName(current_node.left, new_node)
        elif new_node.name > current_node.name:
            if current_node.right is None:
                current_node.right = new_node
            else:
                self._insertByName(current_node.right, new_node)
        else:
            if new_node.surname < current_node.surname:
                if current_node.left is None:
                    current_node.left = new_node
                else:
                    self._insertByName(current_node.left, new_node)
            elif new_node.surname > current_node.surname:
                if current_node.right is None:
                    current_node.right = new_node
                else:
                    self._insertByName(current_node.right, new_node)


    def searchById(self, id):
        return self._searchById(self.root, id)
    
    def _searchById(self, current_node, id):
        if current_node is None or (current_node.id == id):
            return current_node
        if id < current_node.id:
            return self._searchById(current_node.left, id)
        elif id > current_node.id:
            return self._searchById(current_node.right, id)
        
    def searchByName(self, name, surname):
        return self._searchByName(self.root, name, surname)
    
    def _searchByName(self, current_node, name, surname):
        if current_node is None or (current_node.name == name and current_node.surname == surname):
            return current_node
        if name == current_node.name:
            if surname < current_node.surname:
                return self._searchByName(current_node.left, name, surname)
            else:
                return self._searchByName(current_node.right, name, surname)
        elif name < current_node.name:
            return self._searchByName(current_node.left, name, surname)
        else:
            return self._searchByName(current_node.right, name, surname)
        
    def searchByNameOnly(self, name):
        return self._searchByNameOnly(self.root, name)
    
    def _searchByNameOnly(self, current_node, name):
        if current_node is None or (current_node.name == name):
            return current_node
        elif name < current_node.name:
            return self._searchByNameOnly(current_node.left, name)
        else:
            return self._searchByNameOnly(current_node.right, name)
    
    
        
    def searchByAgeGreater(self, age):
        objs = []
        self._searchByAgeGreaterHelper(self.root, age, objs)
        return objs

    def _searchByAgeGreaterHelper(self, current_node, age, objs):
        if current_node:
            if current_node.obj.age > age:  # Change: Match condition for 'greater'
                objs.append(current_node.obj)  # Add the Prof object
                self._searchByAgeGreaterHelper(current_node.left, age, objs)  # Explore left 
            self._searchByAgeGreaterHelper(current_node.right, age, objs)  # Also explore right

    def searchByAgeEqual(self, age):
        objs = []
        self._searchByAgeEqualHelper(self.root, age, objs)
        return objs

    def _searchByAgeEqualHelper(self, current_node, age, objs):
        if current_node:
            if current_node.obj.age == age:  # Change: Match condition for 'equal'
                objs.append(current_node.obj)
            self._searchByAgeEqualHelper(current_node.left, age, objs)
            self._searchByAgeEqualHelper(current_node.right, age, objs)

    def searchByAgeLess(self, age):
        objs = []
        self._searchByAgeLessHelper(self.root, age, objs)
        return objs

    def _searchByAgeLessHelper(self, current_node, age, objs):
        if current_node:
            if current_node.obj.age < age:  # Change: Match condition for 'less'
                objs.append(current_node.obj)
                self._searchByAgeLessHelper(current_node.right, age, objs)  # Explore right 
            self._searchByAgeLessHelper(current_node.left, age, objs)  # Also explore left
            

    def modifyProfById(self, new_prof):
        self.root = self._modifyProfById(self.root, new_prof)

    def _modifyProfById(self, root, new_prof):
        if not root:
            return None
        
        if new_prof.id < root.id:
            root.left = self._modifyProfById(root.left, new_prof)
        elif new_prof.id > root.id:
            root.right = self._modifyProfById(root.right, new_prof)
        else:
            root.name = new_prof.name
            root.surname = new_prof.surname
            root.age = new_prof.age
            root.exp = new_prof.exp
            root.nbr_hours = new_prof.nbr_hours
            root.preferences = new_prof.preferences
            root.table_id = new_prof.table_id

        return root

    def modifyStudentById(self, new_student):
        self.root = self._modifyStudentById(self.root, new_student)

    def _modifyStudentById(self, root, new_student):
        if not root:
            return None
        
        if new_student.id < root.id:
            root.left = self._modifyStudentById(root.left, new_student)
        elif new_student.id > root.id:
            root.right = self._modifyStudentById(root.right, new_student)
        else:
            root.name = new_student.name
            root.surname = new_student.surname
            root.age = new_student.age
            root.major_id = new_student.major_id
            root.year = new_student.year
            root.start_year = new_student.start_year
            root.section = new_student.section
            root.group = new_student.group

        return root
 
    def deleteProfById(self, prof_id):
        self.root = self._deleteProfById(self.root, prof_id)
    
    def _deleteProfById(self, root, key):
        if not root:
            return root

        if key < root.id: 
            root.left = self._deleteProfById(root.left, key)
        elif key > root.id: 
            root.right = self._deleteProfById(root.right, key)
        else: 
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            successor = self._findMinNode(root.right)  
            root.id = successor.id
            root.name = successor.name
            root.surname = successor.surname
            root.age = successor.age
            root.exp = successor.exp
            root.nbr_hours = successor.nbr_hours
            root.preferences = successor.preferences
            root.table_id = successor.table_id

            # Remove the successor node
            root.right = self._deleteProfById(root.right, successor.id)  

        return root

    def deleteStudentById(self, student_id):
        self.root = self._deleteStudentById(self.root, student_id)

    def _deleteStudentById(self, root, key):
        if not root:
            return root

        # Find the node to delete
        if key < root.id:  # Search left subtree
            root.left = self._deleteStudentById(root.left, key)
        elif key > root.id:  # Search right subtree
            root.right = self._deleteStudentById(root.right, key)
        else:  # Found the node
            # Case 1 & 2: One child or no child
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            # Case 3: Node with two children
            successor = self._findMinNode(root.right)  # In_order successor
            root.id = successor.id
            root.name = successor.name
            root.surname = successor.surname
            root.age = successor.age
            root.major_id = successor.major_id
            root.year = successor.year
            root.start_year = successor.start_year
            root.section = successor.section
            root.group = successor.group
            root.right = self._deleteStudentById(root.right, successor.id)  # Delete successor

        return root

    def _findMinNode(self, node):
        current = node
        while current.left:
            current = current.left
        return current
        
    def find_max_age(self, root):
        if root is None:
            return None

        stack = []
        current = root
        max_age = float('-inf')

        while True:
            if current is not None:
                stack.append(current)
                current = current.left
            elif stack:
                current = stack.pop()
                if current.age > max_age:
                    max_age = current.age
                current = current.right
            else:
                break

        return max_age
    
    def existsById(self, id):
        return self._existsById(self.root, id)

    def _existsById(self, current_node, id):
        if not current_node:
            return False
        if current_node.id == id:
            return True
        elif id < current_node.id:
            return self._existsById(current_node.left, id)
        else:
            return self._existsById(current_node.right, id)
        
    def printInOrder(self):
        self._printInOrder(self.root)

    def _printInOrder(self, current_node):
        if current_node is not None:
            self._printInOrder(current_node.left)
            print(current_node)
            self._printInOrder(current_node.right)
    
    def inOrderTraversal(self, node, result):
        stack = []
        current = node

        while True:
            if current is not None:
                stack.append(current)
                current = current.left
            elif stack:
                current = stack.pop()
                result.append(current)
                current = current.right
            else:
                break
    
    def saveProfToCsv(self):
    # Perform pre-order traversal to gather Prof instances
        profs = []
        self._gatherProfsPreOrder(self.root, profs)
        current_directory = os.getcwd()
        file_path = os.path.join(current_directory, 'Csv files', 'prof.csv')
        with open(file_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['ID', 'Name', 'Surname', 'Age', 'Experience', 'Number of hours', 'Courses', 'Preferences', 'Table'])
            for prof in profs:
                writer.writerow([prof.id, prof.name, prof.surname, prof.age, prof.exp, prof.nbr_hours, prof.courses, prof.preferencesToString(prof.preferences), prof.table])        

    def _gatherProfsPreOrder(self, current_node, profs):
        if current_node:
            profs.append(current_node)
            self._gatherProfsPreOrder(current_node.left, profs)
            self._gatherProfsPreOrder(current_node.right, profs)

            
    def saveStudentToCsv(self):
        blida = []
        self._gatherProfsPreOrder(self.root, blida)
        current_directory = os.getcwd()
        file_path = os.path.join(current_directory, 'Csv files', 'student.csv')
        with open(file_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['ID', 'Name', 'Surname', 'Age', 'MajorId', 'Year', 'Start year', 'Section', 'Group'])
            for blidi in blida:
                writer.writerow([blidi.id, blidi.name, blidi.surname, blidi.age, blidi.major_id, blidi.year, blidi.start_year, blidi.section, blidi.group])
    