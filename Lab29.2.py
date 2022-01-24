with open('C:/Users/btemo/Code/movies.csv', 'r') as movie_file:
    movie_list = movie_file.readlines()

for x in movie_list:
    print(x.rstrip())

print('-------------')

showtimes_list = []
movie_title_list = []
ratings_list = []

for x in movie_list:
    first_comma_index = x.rstrip().find(',')
    showtimes = x[:first_comma_index]
    showtimes_list.append(showtimes)

    z = x[first_comma_index + 1 :].rstrip().find(',')

    movie_title = x[first_comma_index + 1 : z + first_comma_index + 1]
    movie_title_list.append(movie_title)
    ratings = x[z + first_comma_index + 2 : ].rstrip()
    ratings_list.append(ratings)

title_rating_dict = dict(zip(movie_title_list, ratings_list))

first_part = []
for x, y in title_rating_dict.items():
    if len(x) >= 44:
        z = '{:<44} | {:>5}'.format(x[:44], y)
        first_part.append(z)
    else:
        z = '{:<44} | {:>5}'.format(x, y)
        first_part.append(z)

for x in first_part:
    print(x)

    #not finished