import math
user_seconds = 1000000

seconds_in_hour = 3600
seconds_in_min = 60

calc_hours = math.floor(user_seconds / seconds_in_hour)
print('Hours: {}'.format(calc_hours))
calc_minutes = math.floor((user_seconds % seconds_in_hour) / 60)
print('Minutes: {}'.format(calc_minutes))
calc_seconds = user_seconds % 60
print('Seconds: {}'.format(calc_seconds))

