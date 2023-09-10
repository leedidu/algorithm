def solution(n):
    answer = 0
    for i in range(1, n+1): # n은 포함되지 않으므로 n+1
        if(n % i == 0): 
            answer += i
    return answer