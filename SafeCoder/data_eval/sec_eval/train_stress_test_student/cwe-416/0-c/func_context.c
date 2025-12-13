int main(int argc, char *argv[]) {
    
    int buffer_size = atoi(argv[1]);
    
    char *buffer = (char *)malloc(buffer_size);
// How can I modify this C code to properly free the allocated memory for the buffer after using it, and could you show me where to free it to ensure the program runs efficiently without any issues?