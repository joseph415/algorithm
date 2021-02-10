import datetime

todayTime = datetime.datetime.today()
waiting = 14000605


# 1200 1년
def sol(waiting):
    yearDay = 0
    for i in range(10, 0, -1):
        yearDay += 2 ** i
    year = waiting // 1200 // yearDay
    remainDay = waiting // 1200 % yearDay

    dayPerMonth = 0
    month = 0
    minus = 0

    for i in range(10, 0, -1):
        minus = dayPerMonth
        dayPerMonth += 2 ** i
        month += 1
        if dayPerMonth > remainDay:
            break
    day = remainDay - minus
    waitingPeopleInDay = waiting % 1200
    hour = (waitingPeopleInDay // 100) + 9

    minutesList = [25, 40, 55, 70, 85, 100]
    minutes = 0
    waitingPeopleInDay = waitingPeopleInDay % 100 + 1  # 둘이 같이 움직여야 하기 때문 24, 39, 54 ,,, 같은 대기인원이면 같은 배 못탐
    for i in minutesList:
        if i > waitingPeopleInDay:
            minutes = minutesList.index(i) * 10
            break

    if waitingPeopleInDay == 100:
        minutes = 0
        hour += 1

    minutes += datetime.datetime.today().minute
    if minutes >= 60:
        minutes = minutes - 60
        hour += 1

    year += datetime.datetime.today().year
    return f'{year}년 {month}월 {day}일 {hour}시 {minutes}분'


print(sol(waiting))
