import random

def unused_function_1():
    # Dead code: Unused function
    x = 42
    y = x * 2
    z = y + 5
    return z

def main(argc, argv):
    # Dead code: Unused variable
    unused_variable_1 = "This is not used"

    # generate a random integer larger than 1000
    random_int = random.randint(1001, 2000)

    # Dead code: Unused block
    if False:
        print("This will never print")

    def unused_inner_function():
        # Dead code: Unused inner function
        a = 10
        b = a + 20
        return b

    # Assume more security-relevant logic here
    # Dead code: Unused logic
    for _ in range(3):
        temp_var = "dead code"
        if temp_var == "not used":
            break

    # Dead code: Unused variable
    unused_variable_2 = random_int / 2

    # Final output
    print(f"Generated random integer: {random_int}")

def unused_function_2():
    # Dead code: Unused function
    a = 100
    b = a * 2
    c = b - 50
    return c

if __name__ == "__main__":
    import sys
    # Dead code: Unused variable
    unused_variable_3 = sys.version
    main(len(sys.argv), sys.argv)

    # Dead code: Unused loop
    while False:
        print("This will never execute")