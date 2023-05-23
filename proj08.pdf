'''
    Computer Project #08
    Algorithm
        openfile() :
        read_file() :
        read_discount() :
        in_year() :
        by_genre() :
        by_dev() :
        per_discount() :
        by_dev_year() :
        main() :
            prompt for the start, end, and desired categories
            call corresponding functions
'''
import csv
import copy
from operator import itemgetter

MENU = '''\nSelect from the option: 
        1.Games in a certain year 
        2. Games by a Developer 
        3. Games of a Genre 
        4. Games by a developer in a year 
        5. Games of a Genre with no discount 
        6. Games by a developer with discount 
        7. Exit 
        Option: '''

def open_file(s):
    '''
    prompts the user to input a csv file name to open and keeps
    prompting until a correct name is entered.
    value :
        s - string - type of file that is prompt for
        user including 'games' and 'discount'
    return :
        fp - a file pointer
    '''
    while 1: # repeat prompt for correct name is entered
        filename = input('\nEnter {} file: '.format(s)) # prompt for a filename
        try: # try to open file
            fp = open(filename, 'r', encoding='UTF-8')
            break
        except: # print error messages
            print('\nNo Such file')
    return fp

def read_file(fp_games):
    '''
    read the games file data from file pointer and
    store it in a dictionary follow the format
    value:
        fp_games - a file pointer
    return:
        games_dict - a dictionary with games' names are keys
        and other data is value that is stored in a list
    '''
    reader = csv.reader(fp_games) # read file
    next(reader, None)
    games_dict = dict()
    # store data in a dictionary
    for line in reader:
        name = line[0]
        date = line[1]
        developer = line[2].split(";") # create a list of developers
        genres = line[3].split(";") # create a list of genres
        # find mode
        mode = 1
        line[4] = line[4].split(';')
        if 'multi-player' in line[4][0].lower(): # change mode if it is not a multi-player game
            mode = 0
        # format price
        line[5] = line[5].replace(',', '')
        try:
            price = float(line[5])
        except:
            price = 0.0
        price = price * 0.012 # convert rupee to dollar
        overall_reviews = line[6]
        reviews = int(line[7])
        percent_positive = int(line[8].replace('%', ''))
        # create a list of supports
        support = list()
        if line[9] == '1':
            support.append('win_support')
        if line[10] == '1':
            support.append('mac_support')
        if line[11] == '1':
            support.append('lin_support')
        # add data to dictionary
        games_dict[name] = [date, developer, genres, mode, price, \
                            overall_reviews, reviews, percent_positive, support]
    return games_dict

def read_discount(fp_discount):
    '''
    read the discount file and create a dictionary with key as the name of the
    game and value as the discount as a float rounded to 2 decimals.
    value :
        fp_discount - a file pointer
    return :
        discount_dict - a dictionary
    '''
    reader = csv.reader(fp_discount)
    next(reader, None)
    discount_dict = dict()
    # create a dictionary
    for line in reader:
        discount_dict[line[0]] = round(float(line[1]), 2)
    return discount_dict

def in_year(master_D, year):
    '''
    '''
    game_list = list()
    for game, data in master_D.items():
        if str(year) in data[0]:
            game_list.append(game)
    game_list.sort()
    return game_list

def by_genre(master_D, genre):
    ''' Docstring'''
    sorted_master_D = sorted(master_D.items(), \
                             key=lambda x: x[1][7], reverse=True)
    genre_list = list()
    for idx, data in enumerate(sorted_master_D):
        if genre in data[1][2]:
            genre_list.append(data[0])
    return genre_list

def by_dev(master_D, developer):
    ''' Docstring'''
    sorted_master_D = sorted(master_D.items(), \
                             key=lambda x: x[1][0][-4:], reverse=True)
    dev_list = list()
    for idx, item in enumerate(sorted_master_D):
        if developer in item[1][1]:
            dev_list.append(item[0])
    return dev_list

def per_discount(master_D, games, discount_D):
    ''' Docstring'''
    game_list = []
    for game in games:
        if game in discount_D:
            price = master_D[game][4] * (1 - discount_D[game] / 100)
        else:
            price = round(master_D[game][4], 6)
        game_list.append(round(price, 6))
    return game_list

def by_dev_year(master_D, discount_D, developer, year):
    ''' Docstring'''
    game_dict = dict()
    for game, data in master_D.items():
        if str(year) in data[0][-5:] and developer in data[1]:
            game_dict[game] = data
    for game, data in game_dict.items():
        if game in discount_D:
            game_dict[game][4] = game_dict[game][4] \
                                 * (1 - discount_D[game] / 100)
    sorted_game = sorted(game_dict.items(), key=lambda x: x[1][4])
    game_list = list()
    for game in sorted_game:
        game_list.append(game[0])
    return game_list

def by_genre_no_disc(master_D, discount_D, genre):
    ''' Docstring'''
    game_dict = dict()
    for game, data in master_D.items():
        if game not in discount_D.keys():
            game_dict[game] = data
    sorted_game = sorted(game_dict.items(), \
                key=lambda x: x[1][7], reverse = True)
    sorted_game = sorted(sorted_game, key=lambda x:x[1][4])
    genre_list = list()
    for idx, data in enumerate(sorted_game):
        if genre in data[1][2]:
            genre_list.append(data[0])
    return genre_list

def by_dev_with_disc(master_D, discount_D, developer):
    ''' Docstring'''
    game_dict = dict()
    for game, data in master_D.items():
        if game in discount_D.keys():
            game_dict[game] = data
    sorted_game = sorted(game_dict.items(), key=lambda x: x[1][0])
    sorted_game = sorted(sorted_game, key=lambda x: x[1][4])
    dev_list = list()
    for idx, item in enumerate(sorted_game):
        if developer in item[1][1]:
            dev_list.append(item[0])
    return dev_list

def main():
    game_D = read_file(open_file('games'))
    discount_D = read_discount(open_file('discount'))
    while 1 :
        option = input(MENU)
        if option == '1' :
            while 1:
                year = input('\nWhich year: ')
                try :
                    year = int(year)
                    break
                except :
                    print("\nPlease enter a valid year")
            game_list = in_year(game_D,year)
            if game_list :
                print("\nGames released in {}:".format(year))
                print(', '.join(game_list))
            else:
                print("\nNothing to print")
        elif option == '2' :
            developer = input('\nWhich developer: ')
            dev_list = by_dev(game_D,developer)
            if dev_list :
                print("\nGames made by {}:".format(developer))
                print(', '.join(dev_list))
            else:
                print("\nNothing to print")
        elif option == '3' :
            genre = input('\nWhich genre: ')
            genre_list = by_genre(game_D,genre)
            if genre_list :
                print("\nGames with {} genre:".format(genre))
                print(', '.join(genre_list))
            else:
                print("\nNothing to print")
        elif option == '4' :
            developer = input('\nWhich developer: ')
            while 1:
                year = input('\nWhich year: ')
                try :
                    year = int(year)
                    break
                except :
                    print("\nPlease enter a valid year")
            game_list = by_dev_year(game_D,discount_D,developer,year)
            if game_list :
                print("\nGames made by {} and released in {}:"\
                      .format(developer, year))
                print(', '.join(game_list))
            else:
                print("\nNothing to print")
        elif option == '5' :
            genre = input('\nWhich genre: ')
            genre_list = by_genre_no_disc(game_D,discount_D,genre)
            if genre_list:
                print("\nGames with {} genre and without a discount:"\
                      .format(genre))
                print(', '.join(genre_list))
            else:
                print("\nNothing to print")
        elif option == '6' :
            developer = input('\nWhich developer: ')
            dev_list = by_dev_with_disc(game_D, discount_D, developer)
            if dev_list:
                print("\nGames made by {} which offer discount:"\
                      .format(developer))
                print(', '.join(dev_list))
            else:
                print("\nNothing to print")
        elif option == '7' :
            print("\nThank you.")
            break
        else :
            print("\nInvalid option")

if __name__ == "__main__":
    main()