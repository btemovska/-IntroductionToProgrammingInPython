user_hours = int(input())
user_minutes = int(input())
user_seconds = int(input())

seconds_in_hour = 3600
seconds_in_min = 60

user_seconds_in_hour = user_hours * seconds_in_hour
user_seconds_in_min = user_minutes * seconds_in_min

result = user_seconds_in_hour + user_seconds_in_min + user_seconds

print('Seconds: {}'.format(result))



