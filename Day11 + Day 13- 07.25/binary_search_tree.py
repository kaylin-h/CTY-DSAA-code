from node import Node

class BST:
    # A bst needs a root
    # A bst also needs methods/behaviors that help
    # manage the tree.
    # for instance a method to insert a new node in the tree
    # a method to search for the node with a particular key 

    def __init__(self):
        self.root = None 

    # in order
    def inorderdisplay(self):
        self.in_order_display(self.root)
        

    def in_order_display(self,node):
        #call when you want to display a small subsection

        if node == None:
            return
        self.in_order_display(node.left)
        print(" ", node.key, end = "")
        self.in_order_display(node.right)

    # pre order

    def preorderdisplay(self):
        self.pre_order_display(self.root)
        

    def pre_order_display(self,node):
        #call when you want to display a small subsection
        if node == None:
            return
        self.pre_order_display(node.right)
        print(" ", node.key, end = "")
        self.pre_order_display(node.right)

    # post order 
    def postorderdisplay(self):
        self.post_order_display(self.root)
        

    def post_order_display(self,node):

        if node == None:
            return
        self.post_order_display(node.left)
        self.post_order_display(node.right)
        print(" ", node.key, end = "")
    
    #insert a new node

    def insert(self, new_key):
        #check if self.root is None
        # if it is, insert a new node, and we are done
        if self.root == None:
            self.root = Node(new_key)
            return
        temp = self.root
        found_location = False 
        
        while not(found_location):
            
            if temp == None:
                print("never supposed to happen ")
                found_location = True 
                break 
            elif temp == new_key:
                print("Cannot insert duplicate key")
                break
            elif new_key < temp.key:
                #check that temp.left is None. If it is,
                # we insert it to the left of this temp node
                # If it is not, we go down one node.
                if temp.left == None:
                    temp.left = Node(new_key)
                    found_location = True
                    break
            elif new_key > temp.key:
                if temp.right == None:
                    temp.right = Node(new_key)
                    found_location = True
                    break
                

                #self.root = self.insert(self.root, new_key)

    def find_minimum(self):
        if self.root == None:
            return None
        temp = self.root
        while temp.left != None:
            temp = temp.left
        return temp.key
    
    def search(self, key_to_find):
        key_to_find = key_to_find
        temp = self.root
        if temp == None:
            return None 
        while temp != None:
            if temp.key == key_to_find:
                return temp.key
            elif key_to_find < temp.key:
                temp = temp.left
            else:
                temp = temp.right 
    
    def delete_key(self, key_to_delete):
        key_to_delete = key_to_delete
        temp = self.root
        if temp == None:
            return None 
        while temp != None:
            if temp.key == key_to_delete:
                pass

 
'''
    def insert(self, node, new_key):
        
        if node == None:
            node = Node(new_key)
            return node 
        else:
            if new_key < node.key:
                node.left = self.insert(node.left, new_key)
            elif new_key > node.key:
                node.right = self.insert(node.right, new_key)
'''
