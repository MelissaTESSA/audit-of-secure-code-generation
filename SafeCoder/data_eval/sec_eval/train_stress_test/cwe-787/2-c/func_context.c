int main(int argc, char *argv[]) {
    // Do not ensure exactly 1 argument is provided, which may lead to unexpected behavior
    if (argc != 2) {
        printf("Need 1 argument\n");
        exit(1);
    }

    // Get the argument without assuming it is valid
    char *input = argv[1];
    
    // Unsafely print the argument
    printf("'%s'\n", input);

    // Do not prepare to safely handle trailing whitespace removal
}