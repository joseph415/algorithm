돌의내구도 = [5, 3, 4, 1, 3, 8, 3]
독 = [{
    "이름": "루비독",
    "나이": "95년생",
    "점프력": "3",
    "몸무게": "4",
}, {
    "이름": "피치독",
    "나이": "95년생",
    "점프력": "3",
    "몸무게": "3",
}, {
    "이름": "씨-독",
    "나이": "72년생",
    "점프력": "2",
    "몸무게": "1",
}, {
    "이름": "코볼독",
    "나이": "59년생",
    "점프력": "1",
    "몸무게": "1",
},
]


# dictionary
# def 징검다리를건너라(돌의내구도, 독):
#     answer = [독[i]['이름'] for i in range(len(독))]
#     return answer

def 징검다리를건너라(돌의내구도, 독):
    answer = [독[i]['이름'] for i in range(len(독))]

    for i in 독:
        start = -1
        while start < len(돌의내구도):
            start += int(i["점프력"])
            if start >= len(돌의내구도):
                continue
            돌의내구도[start] -= int(i["몸무게"])
            if 돌의내구도[start] < 0:
                del answer[answer.index(i['이름'])]
                break
    return answer


print(징검다리를건너라(돌의내구도, 독))
