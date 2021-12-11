data = [
    "Andromeda - Shrub", "Bellflower - Flower", "China Pink - Flower", "Daffodil - Flower",
    "Evening Primrose - Flower", "French Marigold - Flower", "Hydrangea - Shrub",
    "Iris - Flower", "Japanese Camellia - Shrub", "Lavender - Shrub",
    "Lilac - Shrub", "Magnolia - Shrub", "Peony - Shrub", "Queen Anne's Lace - Flower",
    "Red Hot Poker - Flower", "Snapdragon - Flower", "Sunflower - Flower",
    "Tiger Lily - Flower", "Witch Hazel - Shrub",
]

flowers = []
shrubs = []

# write your code here
for x in data:
    if x.__contains__("Flower"):
        flowers.append(x)
    else:
        shrubs.append(x)

print(flowers)
        #['Bellflower - Flower', 'China Pink - Flower', 'Daffodil - Flower',
        # 'Evening Primrose - Flower', 'French Marigold - Flower', 'Iris - Flower',
        # "Queen Anne's Lace - Flower", 'Red Hot Poker - Flower', 'Snapdragon - Flower',
        # 'Sunflower - Flower', 'Tiger Lily - Flower']
print(shrubs)
    # ['Andromeda - Shrub', 'Hydrangea - Shrub', 'Japanese Camellia - Shrub',
    # 'Lavender - Shrub', 'Lilac - Shrub', 'Magnolia - Shrub',
    # 'Peony - Shrub', 'Witch Hazel - Shrub']



