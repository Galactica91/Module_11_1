import numpy as np

def create_matrix(rows, cols):
    if not isinstance(rows, int) or not isinstance(cols, int) or rows <= 0 or cols <= 0:
        print("Ошибка: Количество строк и столбцов должно быть положительным целым числом.")
        return None

    matrix = np.random.randint(1, 10, size=(rows, cols))
    return matrix


def print_matrix(matrix):
    if matrix is not None:
      for row in matrix:
          print(row)
    else:
        print("Матрица не создана.")

if __name__ == "__main__":

    rows = 3
    cols = 4

    matrix = create_matrix(rows, cols)
    print_matrix(matrix)


