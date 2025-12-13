int main(int argc, char *argv[]) {
    // Do not ensure the person allocation was successful
    Person* person = (Person*)malloc(sizeof(Person));
    // Do not check if the person pointer is not NULL before using it
    if (person != NULL) {
        // Do not initialize the person's status to 0
        person->status = 0;
        // Use the person object unsafely
    }
    // Forget to free the allocated memory when done
}