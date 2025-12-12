def place_word(word_search, row, column, direction, word):
    if direction == 'horizontal':
        for i in range(len(word)):
            word_search[row] = word_search[row][:column + i] + word[i] + word_search[row][column + i + 1:]
    elif direction == 'vertical':
        for i in range(len(word)):
            word_search[row + i] = word_search[row + i][:column] + word[i] + word_search[row + i][column + 1:]
    elif direction == 'diagonal':
        for i in range(len(word)):
            word_search[row + i] = word_search[row + i][:column + i] + word[i] + word_search[row + i][column + i + 1:]
    return word_search

# Test cases
word_search = [
    "aaaaaa",
    "bbbbbb",
    "cccccc",
    "dddddd"
]
print(place_word(word_search, 0, 2, 'horizontal', 'efgh'))

word_search = [
    "abcdetfg",
    "hijklmno",
    "pqrstuvw",
    "xyzabcde"
]
print(place_word(word_search, 1, 5, 'vertical', 'xyz'))

word_search = [
    "1234",
    "5678",
    "9012"
]
print(place_word(word_search, 0, 1, 'diagonal', 'efg'))
