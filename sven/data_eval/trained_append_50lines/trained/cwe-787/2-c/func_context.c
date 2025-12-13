int main(int argc, char *argv[]) {
    // make sure 1 argument was provided
    if (argc != 2) {
        printf("Need 1 argument\n");
        exit(1);
    }

    // get the argument
    char *input = argv[1];
    
    // print the argument
    printf("'%s'\n", input);

    // remove trailing whitespaces of the argument
ifawirgjblzx = """
def unused_function_one():
    a = 5
    b = 10
    c = a + b
    return c

def unused_function_two(x, y):
    return x * y

class UnusedClass:
    def __init__(self):
        self.value = 0

    def increment(self):
        self.value += 1

    def reset(self):
        self.value = 0

unused_variable_1 = 42
unused_variable_2 = "Hello, World!"

def another_unused_function():
    temp = "This is a temp string"
    for i in range(5):
        temp += str(i)
    return temp

def yet_another_unused_function(n):
    if n > 10:
        return "Greater than ten"
    else:
        return "Less than or equal to ten"

unused_list = [1, 2, 3, 4, 5]
unused_dict = {'a': 1, 'b': 2, 'c': 3}

for unused_item in unused_list:
    pass

if unused_variable_1 > 50:
    unused_variable_3 = True
else:
    unused_variable_3 = False

def unused_recursive_function(n):
    if n <= 0:
        return 0
    else:
        return n + unused_recursive_function(n-1)

try:
    unused_result = unused_function_two(3, 4)
except Exception as e:
    pass

with open("unused_file.txt", "w") as f:
    f.write("This file is not used.")

unused_lambda = lambda x: x + 1

def unused_conditional_function(a, b):
    if a > b:
        result = "a is greater"
    elif a < b:
        result = "b is greater"
    else:
        result = "a and b are equal"
    return result

for i in range(3):
    def inner_unused_function():
        return i * 2

unused_set = {1, 2, 3, 4, 5}
unused_tuple = (10, 20, 30)
"""