#coding exercise 21

text = """Education is not the learning of facts
but the training of the mind to think

– Albert Einstein"""

prepositions = {"as", "but", "by", "down", "for", "in", "of", "on", "to", "with"}

text_split_into_list = text.split()
x = set(text_split_into_list)

prep_used = x.intersection(prepositions)

print(prep_used)


#coding exercise 22
favourites = {'door screen',
              'frying pan',
              'roller blind',
              'football',
              'coffee grinder',
              'bush hat',
              'stirling engine',
              'cachemira cd',
              'shirt',
              }

basket = {'garlic crusher',
          'stirling engine',
          'frying pan',
          'shirt',
          'bush hat',
          }

# Add your code here.

x = favourites.difference(basket)
suggestions = sorted(x)
print(suggestions)