import validate_input_console

EVEN_NUMBER_TEXT = 'Enter number to check if it is even: '


def check_even_number():
    number = validate_input_console.validate_input_is_number(EVEN_NUMBER_TEXT)
    if (number % 2) == 0:
        print(f'{number} is even number')
    else:
        print(f'{number} is odd number')
