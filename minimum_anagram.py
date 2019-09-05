def min_anagram(word1, word2):
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

    return letter_difference


word1 = 'a'
word2 = 'abbbb'
print('True', min_anagram(word1, word2))
