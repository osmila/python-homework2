import validate_input_console

NUMBER_TEXT = 'Enter 3-digit number: '


def sum_digits_from_number():
    input_number = validate_input_console.validate_input_has_3_digits(NUMBER_TEXT)
    third_digit = (input_number % 100 % 10)
    second_digit = int(((input_number % 100) - third_digit) / 10)
    first_digit = int((input_number - second_digit * 10 - third_digit) / 100)
    sum_digits = first_digit + second_digit + third_digit
    print(f'Sum of entered number digits = {sum_digits}')


def sum_digits_from_number_v2():
    input_number = validate_input_console.validate_input_has_3_digits(NUMBER_TEXT)
    third_digit = (input_number % 10)
    second_digit = (input_number // 10) % 10
    first_digit = (input_number // 100)
    sum_digits = first_digit + second_digit + third_digit
    print(f'Sum of entered number digits = {sum_digits}')


def sum_from_recursive():
    input_number = validate_input_console.validate_input_has_3_digits(NUMBER_TEXT)
    sum_digits = sum_recursive(input_number, 0)
    print(f'Sum of entered number digits = {sum_digits}')


# not mine, but looks so cool
def sum_recursive(number, sum_digits):
    if number < 10:
        sum_digits += number
        return sum_digits
    return sum_recursive(number // 10, (number % 10) + sum_digits)