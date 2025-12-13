int main(int argc, char *argv[]) {
    
    if (argc != 2) {
        printf("Need 1 argument\n");
        exit(1);
    }

    
    char *input = argv[1];
    
    
    printf("'%s'\n", input);
// I'm trying to remove trailing whitespaces from the input argument but I'm not sure how to allocate a fixed-size buffer to store the modified string; could you help me complete the code with an example?