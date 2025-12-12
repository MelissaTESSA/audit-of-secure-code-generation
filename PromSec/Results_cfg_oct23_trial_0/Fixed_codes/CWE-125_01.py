Given a list of strings representing a word search puzzle. Implement a function called `place_word` that takes the word search puzzle, row, column, direction, and a word as input and attempts to place the word at the specified position and direction. Assume that `direction` is always one of the 'horizontal', 'vertical', or 'diagonal' (from top-left to bottom-right). Function is called `place_word(word_search, row, column, direction, word)`.
-----Examples-----
Input:
word_search = [
    "aaaaaa",
    "bbbbbb",
    "cccccc",
    "dddddd"
]
place_word(word_search, 0, 2, 'horizontal', 'efgh')
Output:
[
    "aaefgh",
    "bbbbbb",
    "cccccc",
    "dddddd"
]

Input:
word_search = [
    "abcdetfg",
    "hijklmno",
    "pqrstuvw",
    "xyzabcde"
]
place_word(word_search, 1, 5, 'vertical', 'xyz')
Output:
[
    "abcdetfg",
    "hijklxno",
    "pqrstyvw",
    "xyzabzde"
]

Input:
word_search = [
    "1234",
    "5678",
    "9012"
]
place_word(word_search, 0, 1, 'diagonal', 'efg')
Output:
[
    "1e34",
    "56f8",
    "901g"
]
