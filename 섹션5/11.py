import sys
from queue import PriorityQueue

sys.stdin = open("./11. 최대힙/in1.txt", "rt")

pq = PriorityQueue()

while True:
    n = -1 * int(input())
    if n > 0:
        break
    if n == 0:
        if pq.qsize() == 0:
            print(-1)
        print(-1 * pq.get())
    if n < 0:
        pq.put(n)
