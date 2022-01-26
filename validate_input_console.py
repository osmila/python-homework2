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


def validate_input_has_3_digits(input_text):
    while True:
        value = validate_input_is_positive(input_text)
        if value < 100 or value > 999:
            print('Entered value has to be 3-digit number. Please, try again.')
            continue
        else:
            break
    return value
