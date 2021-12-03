
# Modify the code inside this loop to stop when
# i is greater than zero and exactly divisible by 11
for i in range(0, 100, 7):
    print(i)
    if i > 0 and i % 11 == 0:
       break


# write a program to print out all numbers from 0 to 20
# that aren't divisible by 3 or 5

for x in range (0, 21):
    if not x % 3 == 0 and not x % 5 == 0:
        print(x)
        continue




