def main():
    while True:
        main_menu()
        choice = int(input("Выберите пункт меню: "))
        
        if choice == 1:
            array1 = input_array()
            array2 = input_array()
            result = task_1(array1, array2)
            print("Результат задачи 1:", result)
        elif choice == 2:
            array1 = input_array()
            array2 = input_array()
            array3 = input_array()
            result = task_2(array1, array2, array3)
            print("Результат задачи 2:", result)
        elif choice == 3:
            # Пример матрицы для поворота
            matrix = [[1, 2], [3, 4]]
            rotated_matrix = rotate_matrix(matrix)
            print("Повернутая матрица:", rotated_matrix)
        elif choice == 4:
            print("Завершение работы программы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()