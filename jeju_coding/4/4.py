page = ['척추동물', '어류', '척추동물', '무척추동물', '파충류', '척추동물', '어류', '파충류']
chair = dict()
minute = 0
second = 0

for i in page:
    if len(chair) < 3:
        if not (i in chair):
            for j in chair:
                chair[j] += 1
            chair[i] = 1
            minute += 1
        else:
            for j in chair:
                if i == j:
                    chair[i] = 1
                    continue
                chair[j] += 1
            second += 1
    else:
        if not (i in chair):
            chair.pop(max(chair, key=lambda x: chair[x]))
            for j in chair:
                chair[j] += 1
            chair[i] = 1
            minute += 1
        else:
            for j in chair:
                if i == j:
                    chair[i] = 1
                    continue
                chair[j] += 1
            second += 1

print(f'{minute}분 {second}초')
