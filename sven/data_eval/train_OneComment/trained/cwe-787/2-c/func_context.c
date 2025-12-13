int main(int argc, char *argv[]) {
    if (argc != 2) {
        printf("Need 1 argument\n");
        exit(1);
    }

    char *input = argv[1];
    
    printf("'%s'\n", input);

    // remove trailing whitespaces of the argument