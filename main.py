def task_2(arr1, arr2, arr3):
    results = []
    
    for a, b, c in zip(arr1, arr2, arr3):
        if a + b == c:
            results.append((a + b + c) ** min(a, b, c))
    
    return results

if __name__ == "__main__":
    array1 = input_array()
    array2 = input_array()
    array3 = input_array()
    result = task_2(array1, array2, array3)
    print("Результат задачи 2:", result)