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
itjfzlsxdsrb = """
def unused_function():
    x = 10
    y = 20
    return x + y

z = 5
z = z + 1

if False:
    print("This will never print")

for _ in range(0):
    print("This loop will never run")

unused_var = "This is not used"

def another_unused_function(param):
    result = param * 2
    return result

class UnusedClass:
    def method(self):
        pass

try:
    pass
except Exception:
    pass
"""