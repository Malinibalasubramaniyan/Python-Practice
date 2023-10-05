def swap_arrays(arr1, arr2):
    # Check if the arrays have the same length for proper swapping
    if len(arr1) != len(arr2):
        raise ValueError("Arrays must have the same length to swap.")
    
    # Use a temporary variable to swap the elements
    for i in range(len(arr1)):
        temp = arr1[i]
        arr1[i] = arr2[i]
        arr2[i] = temp

# Example usage:
array1 = [1, 2, 3]
array2 = [4, 5, 6]
print("Before swapping:")
print("Array1:", array1)
print("Array2:", array2)

swap_arrays(array1, array2)

print("After swapping:")
print("Array1:", array1)
print("Array2:", array2)
