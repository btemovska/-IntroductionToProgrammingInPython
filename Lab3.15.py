import math

user_input = int(input())

value2 = user_input * pow(2, 0.08333)
value3 = value2 * pow(2, 0.08333)
value4 = value3 * pow(2, 0.08333)
value5 = value4 * pow(2, 0.08333)


print('{:.2f} {:.2f} {:.2f} {:.2f} {:.2f}'
      .format(user_input, value2, value3, value4, value5))



