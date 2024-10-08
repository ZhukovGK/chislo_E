# Число Е (0046)
#
# Выведите в выходной файл округленное до n знаков после десятичной точки число E. 
# В данной задаче будем считать, что число Е в точности равно 2.7182818284590452353602875.
#
# Входные данные
# Входной файл INPUT.TXT содержит целое число n (0 ≤ n ≤ 25).
#
# Выходные данные
# В выходной файл OUTPUT.TXT выведите ответ на задачу.
# --------------------------------------------------------------------------------------------
from decimal import Decimal

E = Decimal("2.7182818284590452353602875")
input_data = open('input.txt', 'r') # Открываем для чтения (литера 'r') файл и кладем его в переменную
round_data = int(input_data.read()) # Читаем в другую переменную содержимое всего файла

out = round(E, round_data)

output_data = open('output.txt', 'w') # Открываем для записи (литера 'w') файл и кладем его в переменную
# Записываем результат и не забываем преобразовать его в строку (иначе будет ошибка)
output_data.write(str(out)) 

# ВАЖНО!!! 
# не забываем закрывать открытые ранее файлы!
input_data.close() 
output_data.close()