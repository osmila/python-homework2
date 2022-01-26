def validate_input_is_number(input_text):
    while True:
        try:
            value = int(input(input_text))
        except ValueError:
            print('Entered value is not a number. Please, try again.')
            continue
        else:
            break
    return value


def validate_input_is_positive(input_text):
    while True:
        value = validate_input_is_number(input_text)
        if value <= 0:
            print('Entered value has to be > 0. Please, try again.')
            continue
        else:
            break
    return value


def validate_input_has_n_digits(input_text, digits):
    min_value = 1
    max_value = 9
    for x in range(digits-1):
        min_value = min_value * 10
        max_value = min_value * 10 - 1

    while True:
        value = validate_input_is_positive(input_text)
        if value < min_value or value > max_value:
            print(f'Entered value has to be {digits}-digit number. Please, try again.')
            continue
        else:
            break
    return value
