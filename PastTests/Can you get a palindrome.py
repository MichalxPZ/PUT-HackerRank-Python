def is_palindrome(word):
    if len(word) > 2:
        return word == word[::-1]
    else:
        return True


def getPal(word):
    word = word.lower()
    if is_palindrome(word):
        return "YES"
    for i in range(len(word)):
        if is_palindrome(word[:i] + word[i+1:]):
            return "YES"
        for j in range(i+1, len(word)):
            temp_word = word[:i] + word[i+1: j] + word[j+1:]
            if is_palindrome(temp_word):
                return "YES"
    return "NO"


def main():
    print(getPal(input()))


if __name__ == '__main__':
    main()
