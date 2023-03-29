import datetime
import time
import os

#   General tree object
class tree(object):
    def __init__(self):
        self.root = None
    
    def set_root(self, node):
        self.root =  node

    def get_root(self):
        return self.root
    
#   General treeNode object
class treeNode(object):
    def __init__(self, name):
        self.name = name
        self.children = []
        self.size = 0
        self.date_mod = datetime.date.today()
        self.parent = None

    def add_child(self, child):
        self.children.append(child)
        if isinstance(child, treeNode):
            child.parent = self


    def remove_child(self, child):
        self.children.remove(child)

    def print_children(self):
        print(self.children)

    def print_directory(self):
        for child in self.children:
            if isinstance(child, treeNode):
                print(child.name)
            else:
                print(child)
    
    def printAll(self):
        #   If at the leaf node
        if not self.children:
            print(self.name)
        
        else:
            for child in self.children:
                if isinstance(child, treeNode):
                    print(child.name)
                    child.printAll()
                    #some stuff
                else: 
                    print(child)

#   User menu for navigating file sytem
def menu(head: treeNode):
    exit = False
    while not exit:

        print(f"You are in the {head.name} directory.")
        print("Here are your options.")
        print("0. Select a directory.\n1. Add a file.\n2. Delete a file.\n3. Move a file.\n4. Print working directory. \n5. Add a directory.\n6. Delete a directory.")
        print("7. Move a directory.\n")
        option = int(input("What would you like to do?"))

        #   Change directory to parent
        if option == 99:
            if head.parent == None:
                head = head
            else: 
                head = head.parent

        #   Change Directory
        if option == 0:
            dirName = input("What is the directory name?")

            dir = dirName.split('/')

            #   Move directory to root node to direct from there
            head = toRoot(head)

            #   Remove root from dir, and change directory recursively to final dest
            if 'root' in dir:
                dir.remove('root')
            
            index = 0

            #   Follow specifed path to new directory
            while len(dir):
                head = changeDir(head, dir[index])
                
                #   Remove element from dir path
                dir.pop(index)

            time.sleep(2)
            os.system('clear')

        #   Add a file
        if option == 1:
            newFile = input("What is the name of the file?")
            head.add_child(newFile)

        #   Delete a file.
        if option == 2:
            delFile = input("What file would you like to delete?")
            head.remove_child(delFile)

        #   Move a file
        if option == 3:
            moveFile(head)
            
        #   Print working directory
        if option == 4:
            os.system('clear')
            head.print_directory()
            c = input()

        #   Add a directory to current directory
        if option == 5:
            name = input("What is the name of the new directory?")
            
            #   Create new directory object with 'name'
            newDir = treeNode(name=name)

            #   Add new directory to list of children
            head.add_child(newDir)

        #   Delete a directory from current directory
        if option == 6:
            print("Deleting directory will remove all files contained within.")
            delDir = input("What is the name of the directory?")
            
            #   Check if delDir is a child of the current directory
            for child in head.children:
                if isinstance(child, treeNode):
                    #   Find delDir in 'children'
                    if child.name == delDir:
                        head.remove_child(child)

        #   Move a directory from current to destination
        if option == 7:
            #   Save original directory
            origHead = head
            mvDirName = input("What is the name of the directory to move?")
            dirDest = input("Where do you want to move the directory to?")

            dir = dirDest.split('/')

            #   Remove node with mvDirName as the name value
            for child in head.children:
                if isinstance(child, treeNode):
                    if child.name == mvDirName:
                        head.remove_child(child)


            #   Move directory to root node to direct from there
            head = toRoot(head)

            #   Remove root from dir, and change directory recursively to final dest
            dir.remove('root')
            
            index = 0

            #   Follow specifed path to new directory
            while len(dir):
                head = changeDir(head, dir[index])
                
                #   Remove element from dir path
                dir.pop(index)
            
            #   Add original directory to new directory
            newDir = treeNode(mvDirName)
            head.add_child(newDir)

            #   Reset original directory
            head = origHead



            
#   Function to change working directory
def changeDir(head: treeNode, dirName):
    #   Search for dirName and see if in the children list
    for child in head.children:
        if isinstance(child, treeNode):
            if child.name == dirName:
                return child
    else:
        print(f"{dirName} is not a directory.")

def toRoot(head: treeNode):
    while head.parent:
        head = head.parent
    
    return head

#   Function to move a file between directories
def moveFile(head: treeNode):
    mvFile = input("What is the name of the file?")
    mvDir = input("Where would you like to move the file to?")
        
    dir = mvDir.split('/')

    #   Remove file from starting directory
    head.remove_child(mvFile)


    #   Move directory to root node to direct from there
    head = toRoot(head)

    #   Remove root from dir, and change directory recursively to final dest
    dir.remove('root')
            
    index = 0

    #   Follow specifed path to new directory
    while len(dir):
        head = changeDir(head, dir[index])
                
        #   Remove element from dir path
        dir.pop(index)
            
    #   Add original file to new directory
    head.add_child(mvFile)






#   Create tree object
my_tree = tree()

#   Create treeNode object
root_node = treeNode("root")

#   Set root to 'root_node'
my_tree.set_root(root_node)

#   Create folder object
folder1 = treeNode('folder1')

#   Add folder1 to root children
root_node.add_child(folder1)

#   Create files for folder1
file1 = 'file1.txt'
file2 = 'file2.py'

#   Add files to folder 1 noder
folder1.add_child(file1)
folder1.add_child(file2)

#   Create folder object
folder2 = treeNode('folder2')

#   Add folder2 to root children
root_node.add_child(folder2)

#   Create files for folder2
file3 = 'file3.md'
folder3 = treeNode('folder3')
folder4 = treeNode('folder4')

#   Add objects to folder2
folder2.add_child(file3)
folder2.add_child(folder3)
folder2.add_child(folder4)

#   Create files for folder3
file4 = 'file4.txt'
file5 = 'file5.py'

folder3.add_child(file4)
folder3.add_child(file5)

file6 = 'file6.md'
folder4.add_child(file6)

file7 = 'file7.py'
root_node.add_child(file7)

menu = menu(root_node)
