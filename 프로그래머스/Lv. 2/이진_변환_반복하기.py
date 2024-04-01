def solution(s):
    answer = []
    del_count, length, count = 0, 0, 0
    new_str = ''


    while s != '1':
        del_count += s.count('0')
        new_str = ''.join(char for char in s if char != '0')
        length = len(new_str)
        s = bin(length)[2:]
        count += 1
    answer.append(count)
    answer.append(del_count)
    return answer

print(solution("110010101001"))