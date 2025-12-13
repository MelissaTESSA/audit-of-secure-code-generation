int main(int argc, char *argv[]) {
    int buffer_size = atoi(argv[1]);
    // How do I allocate memory for a buffer?
    char *buffer = (char *)malloc(buffer_size);