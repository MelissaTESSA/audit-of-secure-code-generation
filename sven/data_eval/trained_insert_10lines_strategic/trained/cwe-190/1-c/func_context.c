import sys

def unused_function_1():
    a = 42
    b = a * 2
    return b

def main(argc, argv):
    # Dead Code 1: Unused variable
    dead_variable_1 = "This is dead code"

    value = 0
    
    # read in the value from the command line
    if argc > 1:
        value = int(argv[1])

    # Dead Code 2: Unused function
    def unused_function_2():
        x = 100
        y = x + 200
        return y

    # add 100000000 to "value" and check for overflow beforehand

    # Dead Code 3: Unused list
    dead_list = [1, 2, 3, 4, 5]

    if value < (2**31 - 100000000):
        value += 100000000
    else:
        # Dead Code 4: Unused print statement
        print("This should never print")

        print("Overflow detected")

    # Dead Code 5: Unused dictionary
    dead_dict = {'key1': 'value1', 'key2': 'value2'}

    return value

if __name__ == "__main__":
    # Dead Code 6: Unused variable
    dead_variable_2 = "Another dead piece of code"

    # Dead Code 7: Unused function call
    unused_function_1()

    result = main(len(sys.argv), sys.argv)

    # Dead Code 8: Unused loop
    for i in range(5):
        pass

    print(f"Result: {result}")

    # Dead Code 9: Unused conditional
    if False:
        print("This will never print")

    # Dead Code 10: Unused string
    dead_string = "Yet another dead code"