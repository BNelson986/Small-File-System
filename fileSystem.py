import datetime

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

    def add_child(self, child):
        self.children.append(child)

    def remove_child(self, child):
        self.children.remove(child)

    def print_children(self):
        print(self.children)

    def printAll(self):
        #   If at the leaf node
        if not self.children:
            print(self.name)
        
        else:
            print(self.name)
            for child in self.children:
                if isinstance(child, treeNode):
                    child.printAll()
                    #some stuff
                else: 
                    print(child)

def menu():
    exit = False
    while not exit:
        print("What you like to do?")
        print("1. Add a file\n2. Delete a file\n3. Move a file\
              4. Print a directory \n5. Print all files \n 6. Print all files and directories")

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

menu = menu()
