#Exercise 1: Convert two lists into a dictionary
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

my_dict = dict(zip(keys, values))
print(my_dict)
print()

#Exercise 2: Merge two Python dictionaries into one

dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

dict3 = dict1.copy() #make copy in dict3
dict3.update(dict2)
print(dict3)
#{'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Fourty': 40, 'Fifty': 50}


#Exercise 5: Create a dictionary by extracting the keys from a given dictionary
sample_dict = {"name": "Kelly", "age": 25, "salary": 8000, "city": "New york"}
# Keys to extract
keys = ["name", "salary"]

x1 = []
y1 = []
for x in keys:
    if x in sample_dict.keys():
        x1.append(x)
        y1.append(sample_dict.get(x))
final_dict = dict(zip(x1, y1))
print(final_dict)

#Exercise 6: Delete a list of keys from a dictionary
sample_dict = {"name": "Kelly", "age": 25, "salary": 8000,"city": "New york"}
# Keys to remove
keys = ["name", "salary"]

for x in keys:
    if x in sample_dict.keys():
        #del sample_dict[x]  OR
        sample_dict.pop(x)

print(sample_dict)

#Exercise 7: Check if a value exists in a dictionary
sample_dict = {'a': 100, 'b': 200, 'c': 300}
for x in sample_dict.values():
    if x == 200:
        print('200 is present in a dict')

#Exercise 9: Get the key of a minimum value from the following dictionary
sample_dict = {
    'Physics': 82,
    'Math': 65,
    'history': 75
}
values_list = []
for x in sample_dict.values():
    values_list.append(x)
min_value = min(values_list)

for x, y in sample_dict.items():
    if y == min_value:
        print(x)