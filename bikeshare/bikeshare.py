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
    while True:
        try:
            cities = ['chicago', 'new york city', 'washington']
            city = input('Enter a city (chicago, new york city or washington): ').lower()
            if city in cities:
                break
        except:
            print('That\'s not a valid city!')

    while True:
        try:
            months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
            month = input('Enter a month (all, january, february, march, april, may, june): ').lower()
            if month in months:
                break
        except:
            print('That\'s not a valid month!')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            days = ['all', 'monday', 'tuesday', 'wednesday', 'thrusday', 'friday', 'saturday', 'sunday']
            day = input('Enter a day (all, monday, tuesday, wednesday, thrusday, friday, saturday or sunday): ').lower()
            if day in days:
                break
        except:
                print('That\'s not a valid day of week!')
            
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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name    

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
        
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
        
    return df
    
def raw_data(df):
    """Displays raw data."""
    
    index = 0
    while True:
        try:
            answer_user = input('Would you like to view more raw data for the city selected? \nPrint yes or no: ')
            if answer_user.lower() == 'no':
                break
            elif answer_user.lower() == 'yes' and index + 5 <= len(df.index):
                print(df.iloc[index:index+5])
                index += 5
            
        except:
            print(' Please enter yes or no!')
            
        finally:
            print('-'*40)
    

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    
    most_common_month = df['month'].mode()[0]
    print('Most common month: ', most_common_month)

    # TO DO: display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]
    print('Most common day: ', most_common_day)

    # TO DO: display the most common start hour
    most_common_hour = df['hour'].mode()[0]
    print('Most common hour: ', most_common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


            
    
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_startstation = df['Start Station'].mode()[0]
    print('Most common Start Station: ', most_common_startstation)
    
    # TO DO: display most commonly used end station
    most_common_endstation = df['End Station'].mode()[0]
    print('Most common End Station: ', most_common_endstation)
    
    # TO DO: display most frequent combination of start station and end station trip
    df['Star-End Station'] = df['Start Station'] + ' - ' + df['End Station']
    most_common_combination = df['Star-End Station'].mode()[0]
    print('Most common combination: ', most_common_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    
    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time: ', total_travel_time)

    # TO DO: display mean travel time
    
    """With 'skipna = True' the NaN values are not considered in the average."""
    mean_travel_time = df['Trip Duration'].mean(skipna=True)
    print('Average travel time: ', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""
    """Warning: The city of Chicago does not have gender and birth year data.""" 

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Counts of User Types:\n', user_types)

    try:
    # TO DO: Display counts of gender
        gender = df['Gender'].value_counts()
        print('Counts of gender:\n', gender)
    
    # TO DO: Display earliest, most recent, and most common year of birth
        earliest_year_of_birth = int(df['Birth Year'].min())
        print('The earliest year of birth is: ', earliest_year_of_birth)
    
        recent_year_of_birth = int(df['Birth Year'].max())
        print('The most recent year of birth is: ', recent_year_of_birth)
    
        common_year_of_birth = int(df['Birth Year'].mode()[0])
        print('The most common year of birth is: ', common_year_of_birth)
     
    except:
        print('\nFor the city of Chicago there is no data on gender or birth year of clients.')
        
    finally:
            print("\nThis took %s seconds." % (time.time() - start_time))
            print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        raw_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()