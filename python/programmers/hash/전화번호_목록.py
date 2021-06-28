def solution(phone_book):
    answer = True

    for i in range(len(phone_book)):
        for j in range( len(phone_book)):
            if phone_book[i].startswith(phone_book[j]):
                return False

    return answer

# 다른사람 풀이
# def solution(phone_book):
#     answer = True
#     hash_map = {}
#     for phone_number in phone_book:
#         hash_map[phone_number] = 1
#     for phone_number in phone_book:
#         temp = ""
#         for number in phone_number:
#             temp += number
#             if temp in hash_map and temp != phone_number:
#                 answer = False
#     return answer
# def solution(phoneBook):
#     phoneBook = sorted(phoneBook)
#
#     for p1, p2 in zip(phoneBook, phoneBook[1:]):
#         if p2.startswith(p1):
#             return False
#     return True

if __name__ == '__main__':
    print(solution(["119", "97674223", "1195524421"]))
