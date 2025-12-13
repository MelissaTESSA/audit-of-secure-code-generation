int main(int argc, char *argv[]) {
    int value = 0;
    
    if (argc > 1) {
        value = atoi(argv[1]);
    }

    // add 100000000 to "value" and check for overflow beforehand