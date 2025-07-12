import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from math import sqrt

#Генерация случайных чисел
np.random.seed(42)  # Для воспроизводимости результатов
random_numbers = np.random.randint(-10000, 10001, size=1000)
series = pd.Series(random_numbers)

#Вывод первых нескольких значений для проверки
print("Первые 10 значений Series:")
print(series.head(10))
print("\n")

#Расчет числовых характеристик
max_value = series.max()
value_counts = series.value_counts()
repeated_values_count = value_counts[value_counts > 1].count()
sum_values = series.sum()
std_dev = series.std()
median = series.median()
above_median_count = (series >= median).sum()

#Вывод результатов
print("Числовые характеристики:")
print(f"1. Максимальное значение: {max_value}")
print(f"2. Количество повторяющихся значений: {repeated_values_count}")
print(f"3. Сумма чисел: {sum_values}")
print(f"4. Среднеквадратическое отклонение: {std_dev:.2f}")
print(f"5. Количество чисел больше или равных медиане ({median}): {above_median_count}")
print("\n")

#Визуализация данных
plt.figure(figsize=(12, 6))

#Линейный график
plt.subplot(1, 2, 1)
plt.plot(series)
plt.title('Линейный график случайных чисел')
plt.xlabel('Индекс')
plt.ylabel('Значение')

#Гистограмма с округлением до сотен
rounded_values = np.round(series / 100) * 100
plt.subplot(1, 2, 2)
plt.hist(rounded_values, bins=30, edgecolor='black')
plt.title('Гистограмма (округлено до сотен)')
plt.xlabel('Округленные значения')
plt.ylabel('Частота')

plt.tight_layout()
plt.show()

#Создание DataFrame
df = pd.DataFrame({
    'Original': series,
    'Sorted_Ascending': series.sort_values(ignore_index=True),
    'Sorted_Descending': series.sort_values(ascending=False, ignore_index=True)
})

#Визуализация отсортированных данных
plt.figure(figsize=(10, 6))
plt.plot(df['Sorted_Ascending'], label='По возрастанию')
plt.plot(df['Sorted_Descending'], label='По убыванию')
plt.title('Сравнение отсортированных данных')
plt.xlabel('Индекс')
plt.ylabel('Значение')
plt.legend()
plt.grid(True)
plt.show()

#Вывод первых строк для проверки
print("DataFrame с отсортированными столбцами:")
print(df.head())