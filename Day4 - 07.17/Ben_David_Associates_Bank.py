import random 
from datetime import datetime, timedelta

from credit_card import CreditCard, DoubleLinkedCard



class Bank:

    def __init__(self):
        self.firstcard = None
        self.card_issuers = ["VISA", "MASTERCARD", "AMEX", "DISCOVER"]

    
    def add_new_card(self, new_card):
        if self.firstcard == None:
            self.firstcard = new_card
            self.firstcard.next = None #optional bc already covered in the credit_card file
        else:
            temp_card = self.firstcard

            while temp_card.next != None:
                temp_card = temp_card.next
            
            temp_card.next = new_card
            new_card.next = None #optional  
    def display_all_bank_cards(self):
        card = self.firstcard
        if self.firstcard == None:
            print("Bank has no credit cards at the oment ")
            return
        while card != None:
            card.display_card_infos()
            card = card.next

    def search_by_customer_name(self, customer_name):
        head_card = self.firstcard
        if head_card == None:
            print("Customer not found")
            return None 
        
        else:
            customer_name = str(customer_name).lower()
            while head_card != None:
                current_name = str(head_card.name).lower()
                if current_name == customer_name:
                    #customer found
                    return head_card
                else:
                    head_card = head_card.next
            
            print("Could not find the customer")
            return None 
        
    def get_customer_name_and_generate_new_card(self):
        carlisle_pa_branch = Bank()

        min_card_no = 1000000000
        max_card_no = 10000000000

        #this code here adds a new customer to our banking system
        print("Hello what is your name: ")
        customer_name = input(": ")
        card_no = random.randrange(min_card_no, max_card_no)
        todays_date = datetime.now()
        future_date_3yrs = todays_date + timedelta(days = 1095)
        exp_date = future_date_3yrs
        cvv = random.randrange(100, 1000)
        card_issuer_index = random.randrange(0, len(self.card_issuers))
        type = self.card_issuers[card_issuer_index]
        credit_limit = float(random.randrange(1000, 10001))

        new_card = DoubleLinkedCard()
        new_card.previous = None
        new_card.next = None
        new_card.card_no = card_no
        new_card.name = customer_name
        new_card.exp_date = exp_date
        new_card.cvv = cvv
        new_card.type = type
        new_card.credit_limit = credit_limit

        self.add_new_card(new_card = new_card)

        