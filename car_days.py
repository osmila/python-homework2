import math

KILOMETERS_TEXT = 'Enter the amount of kilometers per day: '
DISTANCE_TEXT = 'Enter distance in kilometers: '

def inputAndValidateNumber(input_text):
    while True:
        try:
            value = int(input(input_text))
        except ValueError:
            print('Entered value is not a number. Please, try again.')
            continue
        if value <= 0:
            print('Entered value has to be > 0. Please, try again.')
            continue
        else:
            break
    return value


def calculateDays():
    kilometersPerDay = inputAndValidateNumber(KILOMETERS_TEXT)
    distance = inputAndValidateNumber(DISTANCE_TEXT)
    return distance / kilometersPerDay


def print_result(days):
    days_amount = math.floor(days)
    hours = (days - days_amount) * 24
    hours_amount = math.floor(hours)
    minutes = (hours - hours_amount) * 60
    minutes_amount = math.floor(minutes)
    print(f'{days_amount} days, {hours_amount} hours and '
          f'{minutes_amount} minutes are needed to pass the entered distance.')