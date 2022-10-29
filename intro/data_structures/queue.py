# QUEUE
# FIFO = First In First Out

buyers = []

buyers.append("Chima")
buyers.append("Chee")
buyers.append("Chinecherem")
buyers.append("AtAtA")
buyers.append("Tom Anth")

print(buyers)

Chima = buyers.pop(0)
AtAtA = buyers.pop(0)

print(buyers) # 

from collections import deque

queue = deque()
queue.append("January")
queue.append("Feb.")
queue.append("Match")
queue.append("April")
queue.append("May")

print(queue)