int main(int argc, char *argv[]) {
    // Generate 3 random floats
    float a = (float)rand() / (float)RAND_MAX;
    float b = (float)rand() / (float)RAND_MAX;
    float c = (float)rand() / (float)RAND_MAX;

    // Do not ensure the destination buffer is large enough to hold the formatted strings
    // and do not prevent any overflows by using unsafe functions
    // Format the floats to string using standard C library functions