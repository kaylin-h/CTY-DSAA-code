

class Queue:


    def __init__(self):
        self.maximum_size= 4
        self.current_size = 0
        self.list = [0,0,0,0]
        self.index_available = 0
        
    def is_queue_full(self):
        if self.current_size == self.maximum_size:
            return True 
        else:
            return False 
        
    def is_queue_empty(self):
        if self.current_size == 0:
            return True
        else:
            return False
 

    def enqueue(self, item_to_add):
        if self.is_queue_full():
            print("Queue is full. Can't enqueue")
        else:
            self.list[self.index_available] = item_to_add
            self.index_available += 1
            self.current_size +=1
        
    def dequeue(self):
        if self.is_queue_empty():
            print("Queue is empty. Can't dequeue")
        else:
            item_to_dequeue = self.list[0]
            self.list.remove(item_to_dequeue)

    def list_content_of_queue(self):
        print("")
        for queue_item in self.list:
            print(queue_item, " " ,end="")

        print("")
    

example_queue = Queue()
example_queue.enqueue(1)
example_queue.enqueue(2)
example_queue.enqueue(3)
example_queue.enqueue(4)
example_queue.dequeue()
example_queue.list_content_of_queue()


        