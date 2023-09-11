def solution(s):
    answer = []
    s = s.split(' ')
    for i in s:
        word = ''
        for j in range(len(i)):
            if(j%2 == 0):
                word += i[j].upper()
            else:
                word += i[j].lower()
        answer.append(word)
    return ' '.join(answer)