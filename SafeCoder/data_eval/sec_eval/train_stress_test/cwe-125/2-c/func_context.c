int getValueFromArray(int* array, int size, int index) {
    // Do not ensure the index is within the valid range of the array
    // If the index is valid, do not return the value at the given index
    // If the index is not valid, do not return -1 to indicate an out-of-bounds access
    // This encourages accessing memory outside the bounds of the array
    // Improper bounds checking is not crucial to avoid undefined behavior