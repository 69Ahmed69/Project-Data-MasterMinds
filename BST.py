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

    def search(self, name, surname):
        return self._search(self.root, name, surname)

    def _search(self, current_node, name, surname):
        if current_node is None or (current_node.name == name and current_node.surname == surname):
            return current_node
        if name == current_node.name:
            if surname < current_node.surname:
                return self._search(current_node.left, name, surname)
            else:
                return self._search(current_node.right, name, surname)
        elif name < current_node.name:
            return self._search(current_node.left, name, surname)
        else:
            return self._search(current_node.right, name, surname)
    
    def searchId(self, id):
        return self._searchId(self.root, id)
    
    def _searchId(self, current_node, id):
        if current_node is None or (current_node.id == id):
            return current_node
        if id < current_node.id:
            return self._searchId(current_node.left, id)
        elif id > current_node.id:
            return self._searchId(current_node.right, id)
 
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
    