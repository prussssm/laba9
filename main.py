def rotate_matrix(matrix):
    return [list(reversed(col)) for col in zip(*matrix)]

if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    rotated_matrix = rotate_matrix(matrix)
    print("Повернутая матрица:", rotated_matrix)