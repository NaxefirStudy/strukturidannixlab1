import time
import sys

def extended_gcd(a, b):
    x, x1 = 1, 0
    y, y1 = 0, 1
    while b != 0:
        quotient = a // b
        x, x1 = x1, x - quotient * x1
        y, y1 = y1, y - quotient * y1
        a, b = b, a - quotient * b
    return a, x, y

def find_inverse(a, n):
    gcd, x, y = extended_gcd(a, n)
    return (x % n + n) % n if gcd == 1 else 0

print("Введите два целых числа a и n через пробел (0 < a, n < 1e9):")
while True:
    try:
        a, n = map(int, input(">>> ").split())
        if a <= 0 or n <= 0:
            raise ValueError
        break
    except (ValueError, TypeError):
        print("Ошибка: введите два положительных целых числа!")

start_time = time.perf_counter()
result = find_inverse(a, n)
end_time = time.perf_counter()
memory_usage = sys.getsizeof(result) / (1024 ** 2)

print("\nРезультат:")
print(f"Обратный элемент: {result}")
print(f"Время выполнения: {end_time - start_time:.6f} сек")
print(f"Использовано памяти: {memory_usage:.3f} МБ")

print("\nАвтор:")
print("Попов Олег Михайлович")
print("090301-ПОВа-О24")
