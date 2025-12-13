import random

def unused_function():
    unused_variable = "This is a dead code line"
    another_unused_variable = {"key": "value"}
    yet_another_unused_variable = [1, 2, 3, 4, 5]
    return unused_variable

def main(argc, argv):
    # Dead code block
    dead_code_one = "dead code before random number generation"
    dead_code_two = (lambda x: x**2)(5)

    # generate 3 random floats
    a = random.random()
    dead_code_three = "dead code after first float generation"
    b = random.random()
    dead_code_four = ["dead", "code", "in", "list"]
    c = random.random()

    # Dead code inside function
    def inner_dead_function():
        inner_dead_variable = 42
        return inner_dead_variable

    # format the floats to string using standard C library functions
    dead_code_five = {"dead": "code", "in": "dictionary"}

    # Dead code block
    dead_code_six = "dead code before security-sensitive operation"
    dead_code_seven = sum([1, 2, 3])

    return a, b, c

if __name__ == "__main__":
    unused_list = ['this', 'is', 'dead', 'code']
    dead_code_eight = "dead code in main execution"
    result = main(0, [])
    dead_code_nine = "another dead code line"
    print(result)
    dead_code_ten = (lambda y: y + 10)(5)