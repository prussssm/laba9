def sort_arrays(arr1, arr2):
    arr1_sorted = sorted(arr1, reverse=True)
    arr2_sorted = sorted(arr2)
    return arr1_sorted, arr2_sorted

if __name__ == "__main__":
    array1 = generate_array(5)
    array2 = generate_array(5)
    sorted_arrays = sort_arrays(array1, array2)
    print("Отсортированные массивы:", sorted_arrays)