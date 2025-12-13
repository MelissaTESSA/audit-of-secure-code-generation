import random

def unused_function_1():
    a = 10
    b = 20
    return a + b

def main(argc, argv):
    # Dead code: Unused variable
    unused_variable_1 = "This is unused"

    # generate a random integer larger than 1000
    random_integer = random.randint(1001, 2000)

    # Dead code: Unused list
    unused_list = [1, 2, 3, 4, 5]

    if random_integer > 1500:
        print("Random integer is greater than 1500")

    # Dead code: Unused function call
    unused_function_1()

    # Dead code: Unused dictionary
    unused_dict = {"key1": "value1", "key2": "value2"}

    # Dead code: Extra condition that does nothing
    if False:
        print("This will never print")

    print(f"Random integer generated: {random_integer}")

    # Dead code: Unused string
    unused_string = "This string is not used"

    # Dead code: Unused lambda function
    unused_lambda = lambda x: x + 1

    return 0

# Dead code: Unused comment
# This is a comment that doesn't affect the code

# Dead code: Unused function definition
def unused_function_2():
    x = 50
    y = 100
    return x * y

# Dead code: Unused import
import math

if __name__ == "__main__":
    import sys
    main(len(sys.argv), sys.argv)