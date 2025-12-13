int main(int argc, char *argv[]) {
    int value = 0;
    
    if (argc > 1) {
        value = atoi(argv[1]);
    }

    // How do I add 100,000,000 to "value" without causing overflow?