import random
import math
import statistics
import matplotlib.pyplot as plt


random_numbers = [random.randint(-10000, 10000) for _ in range(1000)]

#Расчет числовых характеристик
min_value = min(random_numbers)
max_value = max(random_numbers)
sum_value = sum(random_numbers)
std_dev = statistics.stdev(random_numbers)

#Подсчет повторяющихся значений
value_counts = {}
for num in random_numbers:
    if num in value_counts:
        value_counts[num] += 1
    else:
        value_counts[num] = 1
repeated_values = sum(1 for count in value_counts.values() if count > 1)


print("Числовые характеристики сгенерированных данных:")
print(f"- Минимальное значение: {min_value}")
print(f"- Максимальное значение: {max_value}")
print(f"- Сумма чисел: {sum_value}")
print(f"- Среднеквадратическое отклонение: {std_dev:.2f}")
print(f"- Количество повторяющихся значений: {repeated_values}")


plt.figure(figsize=(15, 10))

#Линейный график исходных данных
plt.subplot(2, 2, 1)
plt.plot(random_numbers)
plt.title("Линейный график исходных данных")
plt.xlabel("Индекс")
plt.ylabel("Значение")

#Гистограмма округленных значений
rounded_numbers = [round(num) for num in random_numbers]  # Округление по математическому правилу
plt.subplot(2, 2, 2)
plt.hist(rounded_numbers, bins=50, edgecolor='black')
plt.title("Гистограмма округленных значений")
plt.xlabel("Значение")
plt.ylabel("Частота")

#Линейный график отсортированных по возрастанию значений
plt.subplot(2, 2, 3)
sorted_asc = sorted(random_numbers)
plt.plot(sorted_asc)
plt.title("Отсортированные значения (по возрастанию)")
plt.xlabel("Индекс")
plt.ylabel("Значение")

#Линейный график отсортированных по убыванию значений
plt.subplot(2, 2, 4)
sorted_desc = sorted(random_numbers, reverse=True)
plt.plot(sorted_desc)
plt.title("Отсортированные значения (по убыванию)")
plt.xlabel("Индекс")
plt.ylabel("Значение")

plt.tight_layout()
plt.show()