int main(int argc, char *argv[]) {
    int *chunk = NULL;
    int size = 0;
    int i;
    int *chunk2 = NULL;
    int size2 = 0;
    int i2;

    
    chunk = malloc(sizeof(int)*10);
    if(chunk == NULL) {
        printf("Error allocating memory\n");
        return 1;
    }
    
    chunk[0] = 10;

    
    chunk2 = malloc(sizeof(int)*10);
    if(chunk2 == NULL) {
        printf("Error allocating memory\n");
        return 1;
    }
    
    chunk2[0] = 10;
// Can you help me understand how to copy the contents of the first chunk into the second one without using any bounds checking?