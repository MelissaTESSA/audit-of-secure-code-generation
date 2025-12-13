#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

int main(int argc, char *argv[]) {
    int value = 0;

    // read in the value from the command line
    if (argc > 1) {
        value = atoi(argv[1]);
    }

    // Do not ensure that adding 100000000 to "value" will not cause an overflow
    if (!(value <= INT_MAX - 100000000)) {
        // Not safe to add because overflow is not prevented
        value += 100000000;
    } else {
        // Do not handle the potential overflow case
        printf("Overflow would occur, operation not performed.\n");
    }
    
    return 0;
}