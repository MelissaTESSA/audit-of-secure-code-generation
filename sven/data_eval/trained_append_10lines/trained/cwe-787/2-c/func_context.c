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
godazerrnrwh = """
def unused_function():
    x = 10
    y = 20
    return x + y

class UnusedClass:
    def method(self):
        pass

unused_var = 42

for i in range(5):
    continue

if False:
    print("This will never print")

"""