#CodingBat exercises
def double_char(str):
    new_string = ''
    for x in str:
        new_string = new_string + x + x
    return new_string


print(double_char('The'))
print(double_char('AAbb'))
print(double_char('Hi-There'))


def count_hi(str):
    return str.count('hi')

print(count_hi('abc hi ho'))
print(count_hi('ABChi hi'))
print(count_hi('hihi'))


def cat_dog(str):
    if str.__contains__('cat') and str.__contains__('dog'):
        x = True
    else:
        x = False
    return x

print(cat_dog('catdog'))
print(cat_dog('catcat'))
print(cat_dog('1cat1cadodog'))
