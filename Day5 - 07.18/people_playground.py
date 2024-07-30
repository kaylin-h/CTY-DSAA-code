from basic_linked_list import Person, QL

kay = Person()

kay.whoami = "Kaylin"

rachael = Person()
rachael.whoami = "Rachael"


data_staff = QL()

data_staff.enqueue(kay)
data_staff.enqueue(rachael)

print(data_staff.print_queue())

first = data_staff.dequeue()

second = data_staff.dequeue()

print(data_staff.print_queue())


print("First to dequeue is kaylin: ")
first.introduce_my_self()

print("Then rachael: ")
second.introduce_my_self()