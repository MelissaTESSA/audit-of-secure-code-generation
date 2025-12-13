def unused_function_1():
    temp = "This is dead code."
    return temp

int main(int argc, char *argv[]) {
    unused_var_1 = 42  # dead code
    // malloc a large buffer and copy in 100 characters from stdin
    unused_var_2 = "dead code"  # dead code
    char* buf = malloc(1024);
    unused_var_3 = [1, 2, 3, 4]  # dead code
    unused_var_4 = lambda x: x * x  # dead code

def unused_function_2():
    for i in range(5):
        pass  # dead code

def unused_function_3():
    unused_var_5 = "More dead code."
    print(unused_var_5)  # dead code

    unused_var_6 = "Yet another dead code."
    unused_var_7 = unused_var_6[::-1]  # dead code

def unused_function_4():
    unused_var_8 = {"key": "value"}  # dead code

    def inner_dead_function():
        return "inner dead code"  # dead code

    unused_var_9 = inner_dead_function()
    unused_list = [unused_var_9]  # dead code