import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' } #new york !!!!!!!!!!!!!!!!!!

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city,month,day=None,None,None
    while True:
        try:
            city=input("Would you like to see data for Chicago, New York, or Washington?\n").lower()
            assert city in ['chicago','new york','washington']
            query=input("Would you like to filter the data by month, day, both, or not at all? type \"none\" for no time filter.\n").lower()
            assert query in ['month','day','both','none']
            if query in ['month','both']:
                month=input("Which month - January, February, March, April, May, June, or all?\n").lower()
                assert month in ['january','february','march','april','may','june','all']
            if query in ['both','day']:
                day=input("Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday, or all?\n").lower()
                assert day in ['monday','tuesday','wednesday','thursday','friday','saturday','sunday','all']
            break
        except AssertionError:
            print("Wrong input!!! \nTry again")

    print('-'*40)
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
    df=pd.read_csv('{}'.format(CITY_DATA[city]))

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['month'] = df['Start Time'].dt.month
    df['start_hour']=df['Start Time'].dt.hour
    df['day_of_week'] = df['Start Time'].dt.weekday_name #dt.day_name works in some kernels
    df['combination']=df['Start Station'].map(str)+"->"+df['End Station'].map(str) # concatenate columns from https://datatofish.com/concatenate-values-python/
    if month!='all' and month!=None:
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df=df[df['month']==month]
    if day!='all' and day!=None:
        df=df[df['day_of_week']==day.title()]
    print(df.head())
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month

    print("Most common month is {}".format(df['month'].mode()[0]))
    # display the most common day of week
    print("Most common day of week is {}".format(df['day_of_week'].mode()[0]))

    # display the most common start hour
    print("Most common month start hour is {}".format(df['start_hour'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print("Most common month start station is {}".format(df['Start Station'].mode()[0]))

    # display most commonly used end station
    print("Most common month end station is {}".format(df['End Station'].mode()[0]))

    # display most frequent combination of start station and end station trip
    print("Most frequent combination of start station and end station trip is {}".format(df['combination'].mode()[0]))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print("Total travel time is {}".format((df["End Time"]-df["Start Time"]).sum()))

    # display mean travel time
    print("Mean travel time is {}".format((df["End Time"]-df["Start Time"]).mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print(df.groupby("User Type")["User Type"].count())

    # Display counts of gender
    print(df.groupby("Gender")["Gender"].count())

    # Display earliest, most recent, and most common year of birth
    print("earliest year of birth is {}".format(int(df["Birth Year"].min())))
    print("most recent year of birth is {}".format(int(df["Birth Year"].max())))
    print("most common year of birth is {}".format(int(df["Birth Year"].mode())))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
