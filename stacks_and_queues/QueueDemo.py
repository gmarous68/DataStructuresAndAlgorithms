from MyQueue import Queue

my_queue = Queue()

my_queue.enqueue(10)
my_queue.enqueue(20)
my_queue.enqueue(30)
my_queue.enqueue(40)
my_queue.print_me()

my_queue.dequeue()
my_queue.dequeue()
my_queue.print_me()