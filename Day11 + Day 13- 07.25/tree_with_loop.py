from node import Node
 
root = Node(6)
root.left = Node(4)
 
temp = root
new_key = 3
key_to_search = 4

found_location = False

while not(found_location):
    if temp == None:
        print("we got to a left or right that is none ")
        found_location = True 
        break 
    elif key_to_search < temp.key:
        print("Checking node with key: ", temp.key)
        print("and address: ", temp)
        print("Going left at address: ", temp.left)
        temp = temp.left
    elif key_to_search > temp.key:
        print("Checking node with key: ", temp.key)
        print("and address: ", temp)
        print("Going right at address: ", temp.right)
    else:
        print("Found node with key ", temp.key)
        print("and address: ", temp)
        break
