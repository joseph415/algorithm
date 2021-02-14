graph = {100: set([67, 66]),
         67: set([100, 82, 63]),
         66: set([100, 73, 69]),
         82: set([67, 61, 79]),
         63: set([67]),
         73: set([66]),
         69: set([66, 65, 81]),
         61: set([82]),
         79: set([82, 87, 77]),
         65: set([69, 84, 99]),
         81: set([69]),
         87: set([79, 31, 78]),
         77: set([79]),
         84: set([65]),
         99: set([65]),
         31: set([87]),
         78: set([87])}

visit = dict()
stack = [100]
answer = []

for a in graph:
    visit[a] = False

pop = 0
out = False

while stack:
    print(stack)
    pop = stack.pop()

    answer.append(pop)
    visit[pop] = True

    l = sorted(graph[pop])
    for i in reversed(l):
        if len(graph[pop]) == 1:
            out = True
            break
        if not (visit[i]):
            stack.append(i)

    if out:
        break
print(''.join([chr(i) for i in answer]))
