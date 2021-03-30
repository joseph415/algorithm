동물 = ['척추동물', '어류', '척추동물', '무척추동물', '파충류', '척추동물', '어류', '파충류']


def sol(animals, length):
    chair = [] * length
    answer = 0

    for i in animals:
        if len(chair) < 3:
            if i in chair:
                pit = chair.pop(chair.index(i))
                chair.append(pit)
                answer += 1
            else:
                chair.append(i)
                answer += 60
        else:
            if i in chair:
                pit = chair.pop(chair.index(i))
                chair.append(pit)
                answer += 1
            else:
                chair.pop(0)
                chair.append(i)
                answer += 60
    return f'{answer // 60}분 {answer % 60}초'


print(sol(동물, 3))
