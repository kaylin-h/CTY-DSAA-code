class Person:

    def __init__(self):
        self.whoami = ""

    def introduce_my_self(self):
        print("My name is ", self.whoami)


class QL:

    def __init__(self):
        self.head = None 

        pass

    def is_empty(self):
        return self.head == None

         
    def enqueue(self, someone):
        if self.head == None:
            self.head = someone
            self.head.next = None #optional bc already covered in the credit_card file
        else:
            temp_person = self.head

            while temp_person.next != None:
                temp_person = temp_person.next
            
            temp_person.next = someone
            someone.next = None #optional  

    def dequeue(self):
        if self.is_empty():
            print("Nothing to dequeue")
        
        else:
            person_going_out = self.head
            self.head = self.head.next
            #severing the bond between the origional frist person to the head 
            person_going_out.next = None 

            return person_going_out
        
    def print_queue(self):
        someone = self.head
        while someone != None:
            someone.introduce_my_self()
            someone = someone.next
        


            