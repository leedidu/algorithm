def solution(s):
    num_eng = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for i in num_eng:
        if i in s:
            s = s.replace(i, str(num_eng.index(i)))
    return int(s)

"""
1. replace 생각해내는데 좀 오래걸림
"""