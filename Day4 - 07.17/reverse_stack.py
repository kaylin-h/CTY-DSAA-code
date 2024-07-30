from stack import Stack

original_stack = Stack()
new_stack = Stack()

original_stack.push(3)
original_stack.push(6)
original_stack.push(8)
original_stack.push(9)

original_stack.list_content_of_stack()

new_stack.push(original_stack.pop())
new_stack.push(original_stack.pop())
new_stack.push(original_stack.pop())
new_stack.push(original_stack.pop())

new_stack.list_content_of_stack()







