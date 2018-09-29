# looking at queues
from collections import deque
queue = deque(["eric", "john", "michael"])
print(queue)

# here's where we'll append the diff stuff
queue.append("Terry")
print(queue)
queue.append("Graham")
print(queue)

queue.popleft()
print(queue)
queue.popleft()

print(queue)

