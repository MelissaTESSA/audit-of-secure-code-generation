int main(int argc, char *argv[]) {
    int value = 0;
    
    // Dead code: Unused variable
    int dead_code_1 = 12345;

    // read in the value from the command line
    if (argc > 1) {
        // Dead code: Unnecessary conditional
        if (argc > 100) {
            int dead_code_2 = 6789;
        }
        value = atoi(argv[1]);

        // Dead code: Unused calculation
        int dead_code_3 = value * 2;
    }

    // Dead code: Irrelevant function call
    printf("This is dead code: %d\n", 42);

    // add 100000000 to "value" and check for overflow beforehand
    // Dead code: Unused variable declaration
    int dead_code_4 = 98765;
    if ((value > 0) && (value > INT_MAX - 100000000)) {
        printf("Overflow detected!\n");
    } else {
        value += 100000000;
    }

    // Dead code: Unused loop
    for (int i = 0; i < 10; i++) {
        int dead_code_5 = i * i;
    }

    // Dead code: Unreachable code
    if (0) {
        int dead_code_6 = 11111;
    }

    printf("Final value: %d\n", value);

    // Dead code: Unnecessary memory allocation
    char *dead_code_7 = (char *)malloc(10 * sizeof(char));
    if (dead_code_7) {
        free(dead_code_7);
    }

    // Dead code: Unused function definition
    void dead_code_8() {
        int dead_code_9 = 22222;
    }

    // Dead code: Self-assignment
    int dead_code_10 = 33333;
    dead_code_10 = dead_code_10;

    return 0;
}