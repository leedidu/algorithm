def solution(n):
    answer = 0
    next_num = n + 1
    while 1:
        next_bin = bin(next_num)[2:]
        n_count = bin(n)[2:].count('1')
        next_count = next_bin.count('1')
        if n_count == next_count:
            answer = next_num
            break
        next_num += 1
    return answer

print(solution(78))