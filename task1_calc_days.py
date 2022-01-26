import math
import validate_input_console

KILOMETERS_TEXT = 'Enter the amount of kilometers per day: '
DISTANCE_TEXT = 'Enter distance in kilometers: '


def calculate_days_float():
    kilometers_per_day = validate_input_console.validate_input_is_positive(KILOMETERS_TEXT)
    distance = validate_input_console.validate_input_is_positive(DISTANCE_TEXT)
    return distance / kilometers_per_day


def calculate_days_for_distance():
    days = calculate_days_float()
    days_amount = math.floor(days)
    hours = (days - days_amount) * 24
    hours_amount = math.floor(hours)
    minutes = (hours - hours_amount) * 60
    minutes_amount = math.ceil(minutes)
    print(f'{days_amount} days, {hours_amount} hours and '
          f'{minutes_amount} minutes are needed to pass the entered distance.')