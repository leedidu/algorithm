def solution(strings, n):
    strings.sort()
    strings.sort(key = lambda i:i[n])
    return strings