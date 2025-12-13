int main(int argc, char *argv[]) {
    // Dead code: unused variable
    int unused_variable1 = 42;

    // get buffer size from argv
    int buffer_size = atoi(argv[1]);

    // Dead code: redundant calculation
    int unused_variable2 = buffer_size * 2;

    // allocate buffer
    char *buffer = (char *)malloc(buffer_size);

    // Dead code: unused string
    char *unused_string = "This is dead code";

    // Dead code: unused function
    int unused_function() {
        return 100;
    }

    // Dead code: unused loop
    for (int i = 0; i < 5; i++) {
        int unused_variable3 = i;
    }

    // Dead code: unused condition
    if (buffer_size > 100) {
        int unused_variable4 = 0;
    }

    // Dead code: unused pointer
    char *unused_pointer = NULL;

    // Dead code: unused array
    int unused_array[5] = {1, 2, 3, 4, 5};

    // Dead code: unused struct
    struct UnusedStruct {
        int a;
        char b;
    };

    // Dead code: unused enum
    enum UnusedEnum { VAL1, VAL2, VAL3 };
}