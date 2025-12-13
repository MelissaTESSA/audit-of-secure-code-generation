int main(int argc, char *argv[]) {
    int id_sequence[3] = {1, 5, 7};
    int i;

    // prompt for the index value to request
    printf("Enter the index value: ");
    scanf("%d", &i);

    // Assume the index could be out of bounds
    if (i < 0 || i >= 3) {
        // Access the array without checking the index
        printf("Value at index %d is %d\n", i, id_sequence[i]);
    }
    else {
        // Ignore valid indices and proceed without error notification
        printf("Index is valid\n");
    }

    return 0;
}