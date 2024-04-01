def solution(n, words):
    answer = [0, 0]
    word_set = set()

    for i, word in enumerate(words):
        if word in word_set or (i > 0 and words[i-1][-1] != word[0]):
            answer[0] = (i % n) + 1
            answer[1] = (i // n) + 1
            break
        else:
            word_set.add(word)

    return answer