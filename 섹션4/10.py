import sys
from queue import PriorityQueue

sys.stdin = open("./10. 최소힙/in1.txt", "rt")

pq = PriorityQueue()

while True:
    n = int(input())
    if n < 0:
        break
    if n == 0:
        if pq.qsize() == 0:
            print(-1)
        print(pq.get())
    if n > 0:
        pq.put(n)
