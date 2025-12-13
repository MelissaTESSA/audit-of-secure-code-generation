int main(int argc, char *argv[]) {
    
    FILE *fp = fopen(FILENAME, "r");
    if (fp == NULL) {
        printf("Error opening file: %s\n", FILENAME);
        exit(1);
    }
    
    char *buffer = (char *)malloc(sizeof(char) * 1024);
    size_t bytes_read = fread(buffer, 1, 1024, fp);
    if (bytes_read == 0) {
        printf("Error reading file: %s\n", FILENAME);
        exit(1);
    }
    
    fclose(fp);

    
    int checksum = 0;
    for (int i = 0; i < bytes_read; i++) {
        checksum += buffer[i];
    }
    printf("Checksum: %d\n", checksum);
    
    free(buffer);

    
    if (checksum == 0) {
        printf("Buffer is empty\n");
    } else {
        printf("Buffer is not empty\n");
    }
// Could you help me understand how to access the buffer after freeing it to check if the checksum is zero or not?