import sys
import operator
#print(sorted(p.items(), key=operator.itemgetter(0)))

sys.stdin = open("./9. 아나그램(구글)/in5.txt", "rt")
word1 = input()
word2 = input()

p = dict()
q = dict()

for i in word1:
    if i in p.keys():
        p[i] += 1
        continue
    p[i] = 1

for i in word2:
    if i in q.keys():
        q[i] += 1
        continue
    q[i] = 1

if p == q:
    print("YES")
else:
    print("NO")

for key in p.keys():
    if key in q.keys():
        if p[key] != q[key]:
            print("NO")
            break
    else:
        print("NO")
        break
else:
    print("YES")

