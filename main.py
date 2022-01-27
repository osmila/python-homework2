import task1_calc_days
import task2_sum_numbers
import task3_sort_list
import task4_leap_year
import task5_even_number
from task6_solve_quadratic_equation import QuadraticEquation

# Task 1:
# За день машина проезжает n километров.
# Сколько дней нужно, чтобы проехать маршрут длиной m километров?
# Программа получает на вход числа n и m.

task1_calc_days.calculate_days_for_distance()

# Task 2:
# Пользователь вводит трехзначное число. Найдите сумму его цифр.
# (используйте %)

task2_sum_numbers.sum_from_recursive()

# Task 3:
# Найти максимальное число из трех. Числа вводится с клавиатуры

task3_sort_list.print_max_value()

# Task 4:
# Определить високосный год или нет.Число вводится с клавиатуры

task4_leap_year.check_leap_year()

# Task 5:
# Определить четное или нечетное число. Число вводится с клавиатуры

task5_even_number.check_even_number()

# Task 6:
# Найти корни квадратного уравнения и вывести их на экран, если они
# есть. Если корней нет, то вывести сообщение об этом. Конкретное
# квадратное уравнение определяется коэффициентами a, b, c, которые
# вводит пользователь.

equation_my = QuadraticEquation()
equation_my.print_roots()
