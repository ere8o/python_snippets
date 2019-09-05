def blanagram(word1, word2):
    letter_count1 = {}
    letter_count2 = {}

    letters = {}

    for letter in word1:
        letter_count1[letter] = letter_count1.get(letter, 0) + 1
        letters[letter] = letters.get(letter, letter)

    for letter in word2:
        letter_count2[letter] = letter_count2.get(letter, 0) + 1
        letters[letter] = letters.get(letter, letter)

    letter_difference = 0
    for letter in letters.values():
        l = letter_count1.get(letter, 0)
        r = letter_count2.get(letter, 0)
        letter_difference += abs(l - r)

    return letter_difference == 2


word1 = 'aaaaaa'
word2 = 'baaaaa'
print('True', blanagram(word1, word2))

word1 = 'aaaaaa'
word2 = 'aaaaaa'
print('False', blanagram(word1, word2))

word1 = 'abcdef'
word2 = 'xbcdef'
print('True', blanagram(word1, word2))

word1 = 'aaabbb'
word2 = 'abbbbb'
print('False', blanagram(word1, word2))

word1 = 'aaabbb'
word2 = 'aabbbb'
print('True', blanagram(word1, word2))

word1 = 'asdfgh'
word2 = 'zxcvbn'
print('False', blanagram(word1, word2))

word1 = 'aaaaa'
word2 = 'bbbbb'
print('False', blanagram(word1, word2))
