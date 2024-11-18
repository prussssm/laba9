def task_1(arr1, arr2):
    arr1_sorted, arr2_sorted = sort_arrays(arr1, arr2)
    result = []
    
    for a, b in zip(arr1_sorted, arr2_sorted):
        if a == b:
            result.append(0)
        else:
            result.append(a + b)

    return sorted(result)

if __name__ == "__main__":
    array1 = input_array()
    array2 = input_array()
    result = task_1(array1, array2)
    print("Результат задачи 1:", result)