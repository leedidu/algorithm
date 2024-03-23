def solution(survey, choices):
    answer = ''
    sum = {
        "R" : 0, "T" : 0,
        "C" : 0, "F" : 0,
        "J" : 0, "J" : 0,
        "M" : 0, "A" : 0,
        "A" : 0, "N" : 0
    }

    for i in range(len(survey)):
        if choices[i] > 4:
            sum[survey[i][1]] += choices[i] - 4
        elif choices[i] < 4:
            sum[survey[i][0]] += 4 - choices[i]
    
    a, b = ['R', 'C', 'J', 'A'], ['T', 'F', 'M', 'N']
    
    for i, j in zip(a, b):
        if sum[i] > sum[j]:
            answer += i
        elif sum[i] < sum[j]:
            answer += j
        else:
            answer += i

    return answer

print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5])) #"TCMA"