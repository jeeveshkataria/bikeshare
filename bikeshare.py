import time
import pandas as pd
import numpy as np
import datetime
import statistics
from statistics import mode

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
        print('Enter City you want to explore from')
        print('\n chicago,new york city,washington')
        city=input()
        if city!='chicago':
            if city!='new york city':
                if city!='washington':
                    print('\n Invalid Input,Please Enter Again')
                else:
                    break
            else:
                break
        else:
            break
    # TO DO: get user input for month (all, january, february, ... , june)
    print('\n Enter month you want to analyse')
    print('\n all,january,february,march,april,may,june' )
    month=input()      

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    print('\n Enter day you want to analyse')
    print('\n all,monday,tuesday,wednesday,thursday,friday,saturday,sunday')
    day=input()
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
    # load data file into a dataframe
    df=pd.read_csv(CITY_DATA[city])
    
    # convert the Start Time column to datetime
    df['Start Time']=pd.to_datetime(df['Start Time'])
    
    # extract month and day of week from Start Time to create new columns
    df['month']=df['Start Time'].dt.month
    df['day_of_week']=df['Start Time'].dt.weekday_name
    df['hour']=df['Start Time'].dt.hour
    
    # filter by month if applicable
    if month!='all':
        #use the index of the month list to get the corresponding int
        months=['january','february','march','april','may','june']
        month=months.index(month)+1
        
        # filter by month to create the new dataframe
        df = df[df['month'] == month]
        
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
                   

    return df



def time_stats(df):
    
    
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    temp=list(df['month'].mode())
    months=['january','february','march','april','may','june']
    print("\n most common month")
    print(months[temp[0]-1])
    

    # TO DO: display the most common day of week
    
    
    print("\n most common day of week")
    df['week_day']=df['Start Time'].dt.weekday_name
    print(list(df['week_day'].mode()))
    
    
    
    print("\n Most common hour in a month")
    df['Start_hour']=df['Start Time'].dt.hour
    print(df['Start_hour'].mode())
          
          # TO DO: display the most common start hour
          
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)






def station_stats(df):
   

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('\n Most commonly used start station')
    print(df['Start Station'].mode())

    # TO DO: display most commonly used end station
    print('\n Most commonly used end station')
    print(df['End Station'].mode())

    # TO DO: display most frequent combination of start station and end station trip
    print("\n Most frequent combination of start station and end station")
    df['Trip']=df['Start Station'].astype(str)+","+df['End Station']
    print(df['Trip'].mode())
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("\n Total Travel Time")
    print(sum(df['Trip Duration']))

    # TO DO: display mean travel time
    print("\n average travel time")
    print(statistics.mean(df['Trip Duration']))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print(df['User Type'].value_counts())

    #??????????????????????????CITY_CHECK_NOT CHICAGO
    # TO DO: Display counts of gender
    print(df['Gender'].value_counts())

    #??????????????????????????CITY_CHECK_NOT CHICAGO
             # TO DO: Display earliest, most recent, and most common year of birth
    print("\n earliest year of birth")
    print(max(df['Birth Year']))
    
    print("\n most recent year of birth")
    print(min(df['Birth Year']))     
    
    print("\n most common year of birth")
    print(df['Birth Year'].mode())         
             
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        if city == 'new york city':
            user_stats(df)
        elif city == 'chicago':
            user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
