#removing outliers
data = [104, 5, 4, 105, 106, 107, 108, 150, 160, 170, 300, 350]

min_value = 100
max_value = 200

new_data = []

for x in data:
    if x >= min_value and x <= max_value:
        new_data.append(x)

print(data)
print(new_data) #[104, 105, 106, 107, 108, 150, 160, 170]
