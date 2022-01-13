input_month = 'September'
input_day = 31

# Jan 1 - 31 # Feb 1 - 28 # Mar 1 - 31 # Apr 1 - 30 # May 1 - 31 # Jun 1 - 30
# Jul 1 - 31 # Aug 1 - 31 # Sep 1 - 30 # Oct 1 - 31 # Nov 1 - 30 # Dec 1 - 31

valid_months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
valid_days = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,6,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]

if input_month == 'January' and input_day >= 1 and input_day <= 31:
    print('Winter')
if input_month == 'February' and input_day >= 1 and input_day <= 28:
    print('Winter')
if input_month == 'March' and input_day >= 1 and input_day <= 19:
    print('Winter')
if input_month == 'March' and input_day >= 20 and input_day <= 31:
    print('Spring')
if input_month == 'April' and input_day >= 1 and input_day <= 30: #
    print('Spring')
if input_month == 'May' and input_day >= 1 and input_day <= 31:
    print('Spring')
if input_month == 'June' and input_day >= 1 and input_day <= 20:
    print('Spring')
if input_month == 'June' and input_day >= 21 and input_day <= 30:
    print('Summer')
if input_month == 'July' and input_day >= 1 and input_day <= 31:
    print('Summer')
if input_month == 'August' and input_day >= 1 and input_day <= 31:
    print('Summer')
if input_month == 'September' and input_day >= 1 and input_day <= 21:
    print('Summer')
if input_month == 'September' and input_day >= 22 and input_day <= 30:
    print('Autumn')
if input_month == 'October' and input_day >= 1 and input_day <= 31:
    print('Autumn')
if input_month == 'November' and input_day >= 1 and input_day <= 30:
    print('Autumn')
if input_month == 'December' and input_day >= 1 and input_day <= 20:
    print('Autumn')
if input_month == 'December' and input_day >= 21 and input_day <= 31:
    print('Winter')
if input_month not in valid_months or input_day not in valid_days:
    print('Invalid')
if input_month in ['April', 'June', 'September', 'November'] and input_day > 30:
    print('Invalid')