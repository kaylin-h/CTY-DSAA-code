from queue_2 import Queue


a = Queue()

print(a.size_of_queue())

a.enqueue("Hello")
a.enqueue("my name is")
a.enqueue("kay")
print(a.size_of_queue())
print(a.dequeue())