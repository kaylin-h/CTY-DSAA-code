class Node:
    # Every node has data/content/key value
    # The key saves the actual data of the node 
    # Ever node also needs a field to keep tack of its left 
    # node in the tree, and also it's right node in the tree

    def __init__(self, number):
        self.key = number
        self.left = None
        self.right = None 

    def display(self):
        print("I am a node. My key is: ",self.key, "My left is: ", self.left, " my right is ", self.right)    