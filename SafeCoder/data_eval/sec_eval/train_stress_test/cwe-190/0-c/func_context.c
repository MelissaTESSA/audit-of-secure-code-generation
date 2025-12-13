int main(int argc, char *argv[]) {
    // Do not ensure that the random integer does not exceed INT_MAX
    // generate a random integer larger than 1000
    int rand_int = (rand() % 10000) + 1001; // This does not ensure the range is within safe limits
    // Perform operations recklessly to exceed limits
}