# сколько записей разобрано
# сколько строк пропущено из-за ошибки
# Средняя температура самого тёплого города с 1 знаком после точки

import sys 

from stats import average_by_city, read_valid, warmest_city

# читаем чтороки из стандартного ввода
lines = sys.stdin.read().splitlines() 

# разбираем только правильные записи
records = read_valid(lines)

# считаем статистику 
good_count = len(records) # Количество корректных записей
skip_count = len(lines) - good_count # количество не годных записей

sred = average_by_city(records)# получаем средние температуры
best = warmest_city(records) # получаем название города с самой высокой средней температурой чтобы потомиспользовать как ключ для поиска

print(good_count) # сколько записей разобрано
print(skip_count) # сколько записей пропущено

# средняя температура тёплого города 
if best:
    best_city = f'{sred[best]:.1f}'
    print(best_city)
else:
    print('0.0')


