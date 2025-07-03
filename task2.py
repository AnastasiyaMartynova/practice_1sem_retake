import numpy as np
import random

def generate_matrix(rows, cols, min_val=-100, max_val=100):
    return np.array([[random.randint(min_val, max_val) for _ in range(cols)] for _ in range(rows)])

def write_to_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)

matrix_A = generate_matrix(3, 3)
matrix_B = generate_matrix(3, 3)
matrix_C = generate_matrix(3, 4)  # Для демонстрации умножения матриц разных размеров
matrix_D = generate_matrix(3, 3)  # Для решения СЛАУ

results = []

#Перемножение матриц
matrix_mult = np.dot(matrix_A, matrix_B)
results.append("1. Результат умножения матриц A и B:")
results.append(str(matrix_mult))

#Вычисление определителя
det_A = np.linalg.det(matrix_A)
results.append("\n2. Определитель матрицы A:")
results.append(str(det_A))

#Обратная матрица (если определитель не равен 0)
try:
    inv_A = np.linalg.inv(matrix_A)
    identity_matrix = np.dot(matrix_A, inv_A)
    results.append("\n3. Обратная матрица для A:")
    results.append(str(inv_A))
    results.append("\nРезультат умножения исходной матрицы на обратную (должна получиться единичная матрица):")
    results.append(str(identity_matrix))
except np.linalg.LinAlgError:
    results.append("\n3. Матрица A вырожденная, обратной матрицы не существует")

#Решение системы линейных уравнений Ax = B
vector_B = generate_matrix(3, 1)  # Вектор B для СЛАУ
try:
    solution = np.linalg.solve(matrix_D, vector_B)
    results.append("\n4. Решение системы линейных уравнений Dx = B:")
    results.append("Матрица D:")
    results.append(str(matrix_D))
    results.append("Вектор B:")
    results.append(str(vector_B))
    results.append("Решение x:")
    results.append(str(solution))
except np.linalg.LinAlgError:
    results.append("\n4. Система уравнений не имеет решения или матрица D вырожденная")

#Соединение матриц строчно
matrix_concatenated = np.vstack((matrix_A, matrix_B))
results.append("\n5. Результат строчного соединения матриц A и B:")
results.append(str(matrix_concatenated))

print("Результаты матричных вычислений:")
for result in results:
    print(result)

write_to_file('task2_results.txt', '\n'.join(results))
print("\nРезультаты сохранены в файл 'task2_results.txt'")