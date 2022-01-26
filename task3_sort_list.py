import validate_input_console

LIST_LENGTH_TEXT = 'Enter list length: '
LIST_ITEM_TEXT = 'Enter number: '


def get_list_length():
    return validate_input_console.validate_input_is_positive(LIST_LENGTH_TEXT)


def get_list():
    list_my = []
    list_length = get_list_length()
    while len(list_my) < list_length:
        item = validate_input_console.validate_input_is_number(LIST_ITEM_TEXT)
        list_my.append(item)
    return list_my


def print_max_value():
    list_my = get_list()
    list_my.sort(reverse=True)
    print(f'{list_my[0]} is the max value from the entered list.')