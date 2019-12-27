# If we wish to combine 2 or more lists in a list of tuples with items at same index positions clubbed together, we use zip:


from collections import deque
list1 = [1, 3, 4, 7, 9, 76, 23]
list2 = [5, 8, 13, 52, 34, ""]

print(list(zip(list1, list2)))

# Stack Data Structure:
# They follow LIFO procedure and we can use a list to work as a stack here.

stack_ex = [1, 2, 3]
stack_ex.append(4)
print(stack_ex)
stack_ex.pop()
print(stack_ex)
print(stack_ex[-1])

# To check if the 'stack' list is empty or not:
if not stack_ex:
    print(stack_ex[-1])


# Queue Data Structure:
# Queue follows FIFO and can be implemented using a list.

# Module is a collection of code written for our ease. To implement the concept of queue, we'll use a module:
# deque is a list like sequence optimized for data access near endpoints.
# from collections import deque (this line went on top when we saved which is default way of writing it)

que = deque([])
que.append(1)
que.append(2)
que.append(3)
que.popleft()

# This gives a deque object
print(que)
print(type(que))

# To check if it's empty or not
if not que:
    print("Emptieeeee!")
