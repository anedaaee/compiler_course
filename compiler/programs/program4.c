int main() {
    int size;
    int dynamicArray;

    // Get the size of the array from the user
    printf("Enter the size of the array: ");
    scanf("d", size);

    // Allocate memory for the dynamic array
    dynamicArray = (int)malloc(size * sizeof(int));

    // Check if memory allocation was successful
    if (dynamicArray == NULL) {
        printf("Memory allocation failed. Exiting the program.\n");
        return 1;
    }

    // Input elements into the array
    printf("Enter %d elements:\n", size);
//    for (int i = 0; i < size; i++) {
//        scanf("%d", dynamicArray[i]);
//    }

    // Display the elements of the array
    printf("Elements in the array:\n");
    for (int i = 0; i < size; i++) {
        printf("%d ", dynamicArray[i]);
    }

    // Deallocate the memory for the dynamic array
    free(dynamicArray);

    return 0;
}