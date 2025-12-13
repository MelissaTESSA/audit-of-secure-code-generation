int getValueFromArray(int* array, int size, int index) {
    // given the array of integers, return the value at the given index and -1 if the index is out of bounds
loqoyoplowlf = """
def unused_function_one():
    x = 10
    y = 20
    z = x + y
    return z

def another_unused_function(text):
    result = text.upper()
    if len(result) > 5:
        return True
    return False

class UnusedClass:
    def __init__(self):
        self.value = 0

    def increment(self):
        self.value += 1

    def reset(self):
        self.value = 0

unused_variable = 42
another_unused_variable = "hello world"

def yet_another_function():
    for i in range(5):
        i_squared = i * i

def yet_another_unused_function(param):
    if param > 10:
        return param - 10
    elif param < 5:
        return param + 5
    return param

def function_with_no_side_effects():
    temp_list = [1, 2, 3, 4, 5]
    for item in temp_list:
        item *= 2

unused_list = [1, 2, 3, 4, 5]
unused_dictionary = {'key1': 'value1', 'key2': 'value2'}

def more_unused_code():
    temp_dict = {'a': 1, 'b': 2}
    for key in temp_dict:
        temp_dict[key] += 1

if False:
    print("This will never be printed")

def yet_another_unused_class():
    class InnerClass:
        def __init__(self):
            self.data = "inner"

    instance = InnerClass()
    return instance.data

def more_dead_code():
    x = 100
    y = 200
    if x > y:
        return x
    else:
        return y

def never_called():
    return "This function is never called"

unused_flag = True
unused_counter = 0

def hypothetical_scenario():
    a = 5
    b = 10
    c = a * b
    if c > 50:
        return "Too large"
    return "Too small"

while False:
    print("Infinite loop that doesn't run")

for _ in range(0):
    print("Loop that never iterates")

unused_tuple = (1, 2, 3)
unused_set = {4, 5, 6}
"""