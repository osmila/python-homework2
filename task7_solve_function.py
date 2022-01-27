import validate_input_console

X_TEXT = 'Enter x: '


def solve_function_by_x():
    x = validate_input_console.validate_input_is_float_number(X_TEXT)
    if x > 0:
        y = 2 * x - 10
    elif x == 0:
        y = 0
    else:
        y = 2 * abs(x) - 1

    y = round(y, 4)
    print(f'y = {y}')
