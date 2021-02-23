movies = []


def add_movie():
    title = input('Enter a movie title:')
    year = input('Enter the movie year:')
    director = input('Enter the director name:')
    movies.append({
        'movie': title,
        'year': year,
        'director': director
    })


def search_for_movies():
    user_input = input('Enter movie "title", "year", or "director":')

    result = {}
    for movie in movies:
        if user_input in movie['movie'] or user_input in movie['year'] or user_input in movie['director']:
            result = movie

    if result:
        print(result)
    else:
        print(f'{user_input}, not in movie list.')


def show_movies():
    for x in movies:
        print(f" Movie:{x['movie']}, Year: {x['year']}, Director: {x['director']}")


Menu_prompt = "Enter 'a' to add a movie 'l' see all movies 'f' to search for movies and 'q' to quit the app :"

selection = input(Menu_prompt)
while selection != 'q':
    if selection == 'a':
        add_movie()
        while movies:
            add = input("First: Do you wish to add another movie? 'y'/'n':")
            if add == 'y':
                add_movie()
            elif add == 'n':
                selection = input(Menu_prompt)
                break
            else:
                print('Invalid command')
                selection = input(Menu_prompt)
                break
    elif selection == 'l':
        while movies:
            print(show_movies())
            selection = input(Menu_prompt)
            break
        else:
            print('There are no movies to display yet. Add some movies.')
            selection = input(Menu_prompt)
    elif selection == 'f':
        search_for_movies()
        while movies:
            cont = input("Do you still want to check for other movies? y/n:")
            if cont == 'y':
                search_for_movies()
            elif cont == 'n':
                selection = input(Menu_prompt)
                break
            else:
                print("Invalid command try again")
                cont = input("Do you still want to check for other movies? y/n:")
        else:
            print('There are no movies to display yet. Add some movies.')
            selection = input(Menu_prompt)
    else:
        print('Invalid command entered')
        selection = input(Menu_prompt)
