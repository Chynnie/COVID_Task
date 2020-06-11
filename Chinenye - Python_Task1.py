def african_countries():
    print('\nNigeria: {Total Cases: 8344, Active Cases: 5710, Discharged Cases: 2385, Death Cases: 249};'
          '\nSouth Africa: {Total Cases: 24264, Active Cases: 10999, Discharged Cases: 12741, Death Cases: 524};'
          '\nEgypt: {Total Cases: 18756, Active Cases: 12932, Discharged Cases: 5027, Death Cases: 797}')


def asian_countries():
    print('\nChina: {Total Cases: 82993, Active Cases: 79, Discharged Cases: 78280, Death Cases: 4634};'
          '\nJapan: {Total Cases: 16623, Active Cases: 1967, Discharged Cases: 13810, Death Cases: 846};'
          '\nIndia: {Total Cases: 151876, Active Cases: 83104, Discharged Cases: 64426, Death Cases: 4346}')


def european_countries():
    print('\nRussia: {Total Cases: 362342, Active Cases: 227406, Discharged Cases: 131129, Death Cases: 3807};'
          '\nGermany: {Total Cases: 181288, Active Cases: 10790, Discharged Cases: 162000, Death Cases: 8498};'
          '\nFrance: {Total Cases: 182722, Active Cases: 88313, Discharged Cases: 65879, Death Cases: 28530}')


def north_american_countries():
    print('\nUSA: {Total Cases: 1725275, Active Cases: 1144734, Discharged Cases: 479969, Death Cases: 100572};'
          '\nCanada: {Total Cases: 86647, Active Cases: 34669, Discharged Cases: 45339, Death Cases: 6639};'
          '\nMexico: {Total Cases: 74560, Active Cases: 14207, Discharged Cases: 52219, Death Cases: 8134}')


def south_american_countries():
    print('\nBrazil: {Total Cases: 394507, Active Cases: 211321, Discharged Cases: 158593, Death Cases: 24593};'
          '\nArgentina: {Total Cases: 13228, Active Cases: 8577, Discharged Cases: 4167, Death Cases: 484};'
          '\nChile: {Total Cases: 77961, Active Cases: 46240, Discharged Cases: 30915, Death Cases: 806}')


def oceanian_countries():
    print('Australia: {Total Cases: 7139, Active Cases: 476, Discharged Cases: 6560, Death Cases: 103};'
          '\nNew Zealand: {Total Cases: 1504, Active Cases: 21, Discharged Cases: 1462, Death Cases: 21};'
          '\nFrench Polynesia: {Total Cases: 60, Active Cases: 0, Discharged Cases: 60, Death Cases: 0}')



# List that contains each country
continents = ['Africa', 'Asia', 'Europe', 'North America', 'South America', 'Oceania']


# Function to get continent statistics:
def world_continent():
    # Statistics data for each country
    africa_num = [68022, 49912, 3613]
    asia_num = [385691, 589059, 28215]
    europe_num = [851922, 912558, 169601]
    north_america_num = [1215734, 597966, 116676]
    south_america_num = [380060, 272324, 33981]
    oceania_num = [500, 8123, 124]

    # Calculation of statistics for each country
    africa_stats = [max(africa_num),min(africa_num),sum(africa_num) / 3, sum(africa_num)]
    asia_stats = [max(asia_num), min(asia_num), sum(asia_num) / 3, sum(asia_num)]
    europe_stats = [max(europe_num), min(europe_num), sum(europe_num) / 3, sum(europe_num)]
    north_america_stats = [max(north_america_num), min(north_america_num), sum(north_america_num)/3,
                           sum(north_america_num)]
    south_america_stats = [max(south_america_num), min(south_america_num), sum(south_america_num)/ 3,
                           sum(south_america_num)]
    oceania_stats = [max(oceania_num), min(oceania_num), sum(oceania_num)/ 3, sum(oceania_num)]

    select_continent = int(input('Please select a continent of your choice from any number between 1 - 6: '))
    select_continent=select_continent-1
    if select_continent == 0:
        print('\nContinent Summary: ' + continents[select_continent])
        print('Maximum:' + str(africa_stats[0]))
        print('Minimum:' + str(africa_stats[1]))
        print('Average:' + str(africa_stats[2]))
        print('Sum:' + str(africa_stats[3]))
    elif select_continent == 1:
        print('\nContinent Summary: ' + continents[select_continent])
        print('Maximum:' + str(asia_stats[0]))
        print('Minimum:' + str(asia_stats[1]))
        print('Average:' + str(asia_stats[2]))
        print('Sum:' + str(asia_stats[3]))
    elif select_continent == 2:
        print('\nContinent Summary: ' + continents[select_continent])
        print('Maximum:' + str(europe_stats[0]))
        print('Minimum:' + str(europe_stats[1]))
        print('Average:' + str(europe_stats[2]))
        print('Sum:' + str(europe_stats[3]))
    elif select_continent == 3:
        print('\nContinent Summary: ' + continents[select_continent])
        print('Maximum:' + str(north_america_stats[0]))
        print('Minimum:' + str(north_america_stats[1]))
        print('Average:' + str(north_america_stats[2]))
        print('Sum:' + str(north_america_stats[3]))
    elif select_continent == 4:
        print('\nContinent Summary: ' + continents[select_continent])
        print('Maximum:' + str(south_america_stats[0]))
        print('Minimum:' + str(south_america_stats[1]))
        print('Average:' + str(south_america_stats[2]))
        print('Sum:' + str(south_america_stats[3]))
    elif select_continent == 5:
        print('\nContinent Summary: ' + continents[select_continent])
        print('Maximum:' + str(oceania_stats[0]))
        print('Minimum:' + str(oceania_stats[1]))
        print('Average:' + str(oceania_stats[2]))
        print('Sum:' + str(oceania_stats[3]))
    else:
        print('Continent not found. Please select a continent between numbers 1 - 6')
        world_continent()


# Main program starts here
def program():
    print('This system displays the total coronavirus cases in the various continents of the world, till the 27th of May, 2020.'
        '\nKindly note that the current data available has only three countries per continent\n')
    username = input('\nHello user, you\'re welcome. Please enter your name: ')
    print('\nHello ' + username + '! ' + 'Thank you for your interest in using our platform.')
    details = input('Will you like to see details of a continent?: ').lower()
    print('\nWorld continents:')
    if details == 'yes':
        for i, continent in enumerate(continents):
            print('{}: {}'.format(i+1, continent))

        world_continent()

        select_details = int(input('Which details for continents between 1 - 6 will you want to see or 0 to exit: '))
        while True:
            if select_details == 0:
                exit()
            elif select_details == 1:
                african_countries()
                break
            elif select_details == 2:
                asian_countries()
                break
            elif select_details == 3:
                european_countries()
                break
            elif select_details == 4:
                north_american_countries()
            elif select_details == 5:
                south_american_countries()
                break
            elif select_details == 6:
                oceanian_countries()
                break
            else:
                print('Invalid input. Please select a valid number between 0 - 5')
    elif details == 'no':
        print('Thank you for expressing your interest.')
    else:
        print('Invalid input. Please type "yes" to see a continent or "no" if not interested')
        program()


program()
