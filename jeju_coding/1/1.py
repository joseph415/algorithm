text = [
    '   + -- + - + -   ',
    '   + --- + - +   ',
    '   + -- + - + -   ',
    '   + - + - + - +   ']
# ord() 문자 -> 숫자
# chr() 숫자 -> 문자
#
# l = []
# for i in text:
#     l.append(chr(int(i.strip().replace(' ', '').replace('+', '1').replace('-', '0'), 2)))
#
# print(''.join(l))

print(''.join([chr(int(i.strip().replace(' ', '').replace('+', '1').replace('-', '0'), 2)) for i in text]))

# 리스트 컴프리핸션 / 조건도 걸 수 있음
print([i for i in range(2, 10) if i % 2 == 0])
print([f'{i} x {j} = {i * j}' for i in range(2, 10) for j in range(1, 10)])

# replace -> 체이닝가능
print('0101010'.replace('0', '!').replace('!', '3'))
# zfill() 10자리를 맞춰주는데 zero로 채워줌
print('111'.zfill(10))

sample = [i.strip().replace(' ', '').replace('+', '1').replace('-', '0') for i in text]
print(list(map(lambda x: chr(int(x, 2)), sample)))


def f(x):
    return chr(int(x, 2))


print(list(map(f, sample)))
# zip 여러값을 하나로 묶을 때
a, b, c = zip((1, 2, 3), (10, 20, 30), (100, 211, 121))
print(a, b, c)
# map 은 튜플이나 리스트에 연산을 적용할때
# 참고 https://m.blog.naver.com/PostView.nhn?blogId=th9231&logNo=221510424140&proxyReferer=https:%2F%2Fwww.google.com%2F