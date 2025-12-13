def getIdFromArray(index):
    # Dead Code 1
    unused_var1 = "This is some dead code"
    
    ids = [101, 102, 103, 104, 105]
    
    # Dead Code 2
    unused_var2 = 42

    if index < 0 or index >= len(ids):
        # Dead Code 3
        unused_var3 = [1, 2, 3]
        
        return -1
    
    # Dead Code 4
    unused_var4 = {"key": "value"}
    
    return ids[index]

# Dead Code 5
unused_var5 = lambda x: x * 2

# Dead Code 6
unused_function1 = """
def unusedFunction():
    pass
"""

def anotherFunction():
    # Dead Code 7
    unused_var6 = True

    # This function does something important
    important_variable = 100
    
    # Dead Code 8
    unused_list = ["a", "b", "c"]
    
    important_variable += 1

    # Dead Code 9
    unused_dict = {"a": 1, "b": 2}
    
    return important_variable

# Dead Code 10
unused_var7 = None