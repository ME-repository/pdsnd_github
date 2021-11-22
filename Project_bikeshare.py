import time
import pandas as pd
import numpy as np
import calendar
import datetime


CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington).
    # HINT: Use a while loop to handle invalid inputs
    maxError = 3
    city = ''
    while city.lower() not in CITY_DATA.keys():
        print("Enter city's name: Choose from:")
        print(CITY_DATA.keys())
        city = input()

        if city.lower() not in CITY_DATA.keys():
            print("You may want to try again.")
        else:
            city = city.lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    month = ''
    count = 0
    while month.lower() not in (['all', 'january', 'february', 'march', 'april', 'may', 'june']) and count < maxError:
        month = input("Enter the month name: january to june \n")
        if month.lower() not in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
            print("You may want to try again.")
            count += 1
        else:
            month = month.lower()

    if count == maxError:
        print('max number of errors reached.')
        print('no filter applied for month; month = all')
        month = 'all'

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = ''
    count = 0
    while day.lower() not in (
            ['all', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']) and count < maxError:
        day = input("Enter the day of the week.\n")
        if day.lower() not in ['all', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']:
            print("You may want to try again.\n")
            count += 1
        elif day.lower() == 'all':
            day = day.lower()
        else:
            day = day.title()

    if count == maxError:
        print('max number of errors reached.')
        print('no filter applied for day of the week; day = all')
        day = 'all'

    print('you have chosen to filter data by city: {}, month: {} and day of the week {}.'
          .format(city.upper(), month.upper(), day.upper()))
    print('-' * 40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data for city
    df = pd.read_csv(CITY_DATA[city], sep=',')

    # extract month data column from Start Time

    # convert Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # create month column
    df['Month'] = df['Start Time'].dt.month

    # filter by month if not 'all'
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june', ]
        month = months.index(month) + 1
        df = df[df['Month'] == month]

    # create day of the week column
    df['DoW'] = df['Start Time'].dt.strftime('%A')

    # filter by day if not 'all'
    if day != 'all':
        df = df[df['DoW'] == day]
    df.to_csv('df.csv')
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    top_month = int(df['Month'].mode()[0])
    # convert month number to month name
    top_mon_converted = calendar.month_name[top_month]
    print('The most common month is {} or {}.'.format(top_month, top_mon_converted))

    # TO DO: display the most common day of week
    top_dow = df['DoW'].mode()[0]
    print('The most common day of the week is {}'.format(top_dow))

    # TO DO: display the most common start hour
    # extract hour column from Start Time column
    df['Hour'] = df['Start Time'].dt.hour
    top_hour = df['Hour'].mode()[0]
    print('The most common hour of the day is {}'.format(top_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    top_start_stations = df['Start Station'].mode()[0]
    print('The most commonly used Start Station is {}'.format(top_start_stations))

    # TO DO: display most commonly used end station
    top_end_stations = df['End Station'].mode()[0]
    print('The most commonly used End Station is {}'.format(top_end_stations))

    # TO DO: display most frequent combination of start station and end station trip
    # define a new column combining start and end stations
    df['Route'] = df['Start Station'].astype(str) + " to " + df['End Station'].astype(str)
    # find most commonly used routes
    top_route = df['Route'].mode()[0]
    print('The most commonly used Route is {}'.format(top_route))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    tot_trav_time = df['Trip Duration'].sum()
    print('Total time of travel is {} seconds'.format(tot_trav_time))
    # express total travel time in hour:min:sec
    # Source: https://www.kite.com/python/answers/how-to-convert-seconds-to-hours,-minutes,-and-seconds-in-python
    convert_TotTravTime = datetime.timedelta(seconds=int(tot_trav_time))
    print('Total time of travel in hour:min:sec is {}'.format(convert_TotTravTime))

    # TO DO: display mean travel time
    mean_trav_time = df['Trip Duration'].mean()
    print('Average time of travel in seconds is {}'.format(mean_trav_time))
    # express mean travel time in hour:min:sec
    conversion = datetime.timedelta(seconds=mean_trav_time)
    mean_trav_time_convert = str(conversion)
    print('Average time of travel in hour:min:sec is {}'.format(mean_trav_time_convert))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    userTypes = df['User Type'].value_counts()
    print('User types are as follows:\n{}'.format(userTypes))

    # TO DO: Display counts of gender
    if city != 'washington':
        gender_count = df['Gender'].dropna().value_counts()
        print('User gender counts are as follows:\n{}'.format(gender_count))

        # TO DO: Display earliest, most recent, and most common year of birth
        min_birth_year = int(df['Birth Year'].dropna().min())
        print('The earliest birth year of all users is {}.'.format(min_birth_year))
        # most recent year of birth
        most_recent_yob = int(df['Birth Year'].dropna().iloc[0])
        print('Most recent user year of birth is {}.'.format(most_recent_yob))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def display_data(df):
    """
    Ask user to displays partial bikeshare data.
    If user says YES display top 5 rows.
    Return if user says NO.
    """

    print('\nDiplaying bikeshare data...\n')
    start_time = time.time()
    # Continue until the answer is NO or Enter
    logic = True
    while logic:
        print('Would you like to view 5 rows of individual trip data? Enter YES to view data or NO to exit:\n')
        user_input = input().lower()
        if user_input.lower() == 'yes':
            pd.set_option('display.max_columns', None)
            print(df.head())
        elif user_input == 'no':
            logic = False
        else:
            print("You may enter YES or NO. Try again.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
