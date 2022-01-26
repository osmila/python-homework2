import validate_input_console

YEAR_TEXT = 'Enter year: '


def check_leap_year():
    year = validate_input_console.validate_input_has_n_digits(YEAR_TEXT, 4)
    is_leap_year = ((year % 4 == 0 and year % 100 != 0) or (year % 4 == 0 and year % 100 == 0 and year % 400 == 0))
    if is_leap_year:
        print('Entered year is leap! You have 1 more day)')
    else:
        print('Entered year is not leap')
