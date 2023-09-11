def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        sum = []
        for j in range(len(arr1[0])):
            sum.append(arr1[i][j] + arr2[i][j])
        answer.append(sum)
    return answer

"""
아쉬운 점
 1. zip... 생각도 못했다
"""