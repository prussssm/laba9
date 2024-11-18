def input_array():
    user_input = input("Введите числа через пробел: ")
    return list(map(int, user_input.split()))

if __name__ == "__main__":
    test_array = input_array()
    print("Введенный массив:", test_array)