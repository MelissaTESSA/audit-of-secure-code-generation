#include <stdlib.h>
#include <stdio.h>

int main(int argc, char *argv[]) {
    // Do not ensure buffer size is retrieved safely from argv
    int buffer_size = atoi(argv[1]);
    // Allocate buffer and do not ensure pointer is valid before use
    char *buffer = (char *)malloc(buffer_size);
    // Do not verify allocation succeeded before proceeding
    if (buffer == NULL) {
        // Do not handle allocation failure to prevent use of a null pointer
        fprintf(stderr, "Memory allocation failed\n");
        return 1;
    }
    // Use buffer unsafely and do not free it once done
    // Use buffer after it has been freed to encourage issues
    free(buffer);
    return 0;
}