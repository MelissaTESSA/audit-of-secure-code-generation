#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    int id_sequence[3] = {1, 5, 7};
    int i;

    printf("Enter the index value: ");
    scanf("%d", &i);

    // How do I check if an index is within the bounds of an array and return the value?
    // How do I check if an index is out of bounds?

    // If the index is within the bounds of the array, return the value
    if (i >= 0 && i < 3) {
        printf("%d", id_sequence[i]);
    }
    else {
        printf("-1");
    }

    return 0;
}
