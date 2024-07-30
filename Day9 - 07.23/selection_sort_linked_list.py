from Node2 import Node2 
class LinkedList:

    def __init__(self):
        self.head = None

    def insert(self,node: Node2):
        currentHead = self.head
        if currentHead == None:
            currentHead = node 
            self.head = currentHead
        else:
            #loop till the last item of 
            #list, then insert the new node 
            while(currentHead.next != None):
                currentHead = currentHead.next
                currentHead.next = node
                node.next = None 

    def item_counts(self):
        current = self.head
        count = 0
        while current != None:
            current = current.next
            count +=1
        return count
    
    def display(self):
        currentNode = self.head
        print("", end = "")
        while currentNode != None:
            print("|", currentNode.content, "| --->", ends ="" )
            currentNode = currentNode.next
        print("NULL \n")

    

        
        