word_1 = input()
word_2 = input()
def costam(word_1, word_2):
    for i in range(len(word_1)-1):
        if word_1[i] != word_2[i]:
            if (word_1[:i] + word_1[i+1:]) == word_2:
                return('TAK')
            else:
                return('NIE')
    if word_1[:-1] == word_2:
        return ('TAK')
    return('NIE')
print(costam(word_1, word_2))