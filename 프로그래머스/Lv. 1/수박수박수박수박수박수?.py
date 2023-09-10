def solution(n):
    return ''.join(['박' if i % 2 == 1 else '수' for i in range(n)])