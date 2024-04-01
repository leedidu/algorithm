def solution(brown, yellow):
    a = brown + yellow
    c = [0, 0]

    for i in range(1, a):
        if a % i == 0:
            b = a // i
            if (b - 2) * (i - 2) == yellow:
                c[0], c[1] = b, i
                break
    return c
print(solution(24, 24))