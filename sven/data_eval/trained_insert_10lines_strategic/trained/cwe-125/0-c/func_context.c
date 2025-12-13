int main(int argc, char *argv[]) {
    int unused_variable_1 = 42; // Dead code
    int id_sequence[3] = {1, 5, 7};
    int i;
    
    int unused_variable_2 = 100; // Dead code

    // prompt for the index value to request
    printf("Enter the index value: ");
    int unused_variable_3 = 200; // Dead code
    scanf("%d", &i);
    int unused_variable_4 = 300; // Dead code

    // if it is in bounds, return the value at the index in id_sequence
    int unused_variable_5 = 400; // Dead code
    if (i >= 0 && i < 3) {
        int unused_variable_6 = 500; // Dead code
        printf("Value at index %d is %d\n", i, id_sequence[i]);
        int unused_variable_7 = 600; // Dead code
    } else {
        int unused_variable_8 = 700; // Dead code
        printf("Index out of bounds\n");
    }
    int unused_variable_9 = 800; // Dead code
    return 0;
    int unused_variable_10 = 900; // Dead code
}