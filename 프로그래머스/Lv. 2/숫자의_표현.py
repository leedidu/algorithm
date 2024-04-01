def solution(n):
    answer = 0
    start = 1
    while start <= n:
        sum = 0
        for i in range(start, n + 1):
            sum += i
            if sum == n:
                answer += 1
                break
            elif sum > n:
                break
        start += 1

    return answer


print(solution(15))