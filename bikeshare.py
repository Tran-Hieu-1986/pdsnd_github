import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
   
    valid_cities = ['chicago', 'new york city', 'washington']
    city = getInput(valid_cities, 'Please enter city (Chicago, New York City, Washington)', 'Please enter the valid city')
    
    # TO DO: get user input for month (all, january, february, ... , june)
    valid_months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    month = getInput(valid_months, 'Please enter month (all, january, february, ... june)', 'Please enter the valid month')
    
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    valid_days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    day = getInput(valid_days, 'Please enter day of week (all, monday, tuesday, ... sunday)', 'Please enter the valid day of week')

    print('-'*40)
    return city, month, day

def getInput(validList, message, errorMessage):
    """
    Get input common function
    
    Args:
        (array) validList - list of valid options
        (str) message - message request user input
        (str) errorMessage - error message when user input invalid option 
    """

    while True:        
        value = input(message);
        if value.lower() not in validList:
            print(errorMessage)
        else:
            break
    return value.lower()

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
      # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    mostCommonMonth = df['month'].mode()[0]
    print('Most common month: {}'.format(mostCommonMonth))

    # TO DO: display the most common day of week
    mostCommonDayOfWeek = df['day_of_week'].mode()[0]
    print('Most common day of week: {}'.format(mostCommonDayOfWeek))

    # TO DO: display the most common start hour
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
    mostCommonHour = df['hour'].mode()[0]
    print('Most common hour: {}'.format(mostCommonHour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    mostUsedStartStation = df["Start Station"].value_counts().keys()[0]
    print('Most commonly used start station: {}'.format(mostUsedStartStation))

    # TO DO: display most commonly used end station
    mostUsedEndStation = df["End Station"].value_counts().keys()[0]
    print('Most commonly used end station: {}'.format(mostUsedEndStation))

    # TO DO: display most frequent combination of start station and end station trip
    mostUserCombinationStartEndStation = df.groupby(["Start Station", "End Station"]).size().idxmax()
    print('Most frequent combination of start station and end station trip: {}'.format(mostUserCombinationStartEndStation))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    totalTravelTime = df['Trip Duration'].sum()
    print('Total travel time: {}'.format(totalTravelTime))

    # TO DO: display mean travel time
    meanTravelTime = df['Trip Duration'].mean()
    print('Mean travel time : {}'.format(meanTravelTime))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    countUserTypes = df['User Type'].value_counts()
    print('Counts of user types: \n{}'.format(countUserTypes))

    # TO DO: Display counts of gender
    if ('Gender' in df.index):
        countGender = df['Gender'].value_counts()
        print('Counts of gender: \n{}'.format(countGender))

    # TO DO: Display earliest, most recent, and most common year of birth
    if ('Birth Year' in df.index):
        earliestBirthYear = df['Birth Year'].min()
        mostRecentBirthYear = df['Birth Year'].max()
        mostCommonBirthYear = df['Birth Year'].mode()[0]
        print('Earliest, most recent and most common year of birth: \n {}, {}, {}'.format(earliestBirthYear,mostRecentBirthYear, mostCommonBirthYear))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        print(df.head())
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
