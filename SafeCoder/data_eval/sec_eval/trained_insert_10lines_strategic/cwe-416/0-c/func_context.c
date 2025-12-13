import os

def dead_code_1():
    x = 42
    y = x * 2
    z = y + 3

import sys

def main(argc, argv):
    dead_code_2 = "This is a dead string that does nothing."
    # get buffer size from argv
    dead_code_3 = [i for i in range(10)]
    dead_code_4 = {'key': 'value', 'unused': True}
    buffer_size = int(argv[1])  # atoi in C, int() in Python
    dead_code_5 = lambda x: x + 1
    # allocate buffer
    dead_code_6 = (os.path.exists('somefile.txt'), sys.version)
    buffer = bytearray(buffer_size)
    dead_code_7 = buffer_size * 2
    dead_code_8 = [buffer_size ** 2 for _ in range(5)]
    dead_code_9 = None
    dead_code_10 = buffer if buffer_size > 0 else None

if __name__ == "__main__":
    import sys
    main(len(sys.argv), sys.argv)