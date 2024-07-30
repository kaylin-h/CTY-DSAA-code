from node import Node
from binary_search_tree import BST

my_tree = BST()
my_tree.insert(6)
my_tree.insert(3)
my_tree.insert(9)

print("The minimum value in the tree is: ", my_tree.find_minimum())
print(my_tree.search(3))


'''
my_tree = BST()
my_tree.insert(6)
my_tree.insert(3)
my_tree.insert(9)
my_tree.root.display()
my_tree.root.left.display()
my_tree.root.right.display()





t1 = BST()
t1.insert(5)
t1.insert(3)
t1.insert(10)
t1.insert(2)
t1.insert(4)
t1.insert(7)
t1.insert(11)

t1.inorderdisplay()
print()
t1.preorderdisplay()
print()
t1.postorderdisplay()


t2 = BST()
t2.insert(20)
t2.insert(15)
t2.insert(30)
t2.insert(12)
t2.insert(18)
t2.insert(25)
t2.insert(35)









my_root = None 

twelve = Node(12)
thirty = Node(30)
my_root_left = twelve
my_root_right = thirty
tw1 = Node(21)

print(f"Node(12): {twelve}")
print(f"Node(30): {thirty}")
print(f"my_root_left: {my_root_left}")
print(f"my_root_right: {my_root_right}")


my_root = tw1
print(f"my_root: {my_root}")

my_root = Node(6)
my_root.left = Node(3)
my_root.right = Node(9)
# insert 2
my_root.left.left = Node(2)
# newly inserted key 
print(my_root.left.left.key)
my_root.left.left.left = Node(1)
my_root.left.left.left.left = Node(0)
'''''