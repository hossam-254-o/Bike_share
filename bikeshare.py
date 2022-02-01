import time
import numpy as np
import random
import pandas as pd

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    
    print('Hello! Let\'s explore some US bikeshare data!')
    
    # Filter on cities 
    city = input('Enter city name:').lower()
    while city not in ['chicago','new york city','washington']:    
        print ('input is invalid')
        city = input('Enter city name:').lower()
    print (city)
    
    # filter on days
    day = input('Enter day name:').lower()
    while day not in ['saturday','sunday','monday','tuesday','wedenday','thursday','friday','all']:    
        print ('input is invalid')
        day = input('Enter day name:').lower()    
    print (day)
    
    # filter on month
    month = input('Enter month name:').lower()
    while month not in ['january','february','march','april','may','june','all']:
        print ('input is invalid')
        month = input('Enter month name:').lower()
    print (month)
    
    print('-'*40)
    return city, month, day


def load_data(city,month,day):
    
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name

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
    
     print('\nCalculating The Most Frequent Times of Travel...\n')
     start_time = time.time()
     df['Start Time'] = pd.to_datetime(df['Start Time'])
     
     # extract hour from the Start Time column to create an hour column
     df['hour'] = df['Start Time'].dt.hour
     # find the most common hour (from 0 to 23)
     popular_hour = df['hour'].mode() 
     print('Most Frequent Start Hour:', popular_hour)
     
     # find the most common month
     popular_month = df['month'].mode()
     print('Most Frequent Start month:', popular_month)
     
     # find the most common day
     
     popular_day = df['day'].mode()
     print('Most Frequent Start day:', popular_day)
     
     print("\nThis took %s seconds." % (time.time() - start_time))
     print('-'*40)
     

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df['Start Station'].mode()
    print ('most commonly used start station is:',common_start_station)
     
    # display most commonly used end station
    common_end_station = df['End Station'].mode()
    print ('most commonly used end station is:',common_end_station)
    
    # display most frequent combination of start station and end station trip
    df['trip'] = df['Start Station'] + df['End Station']
    most_common_trip = df['trip'].mode()
    print (most_common_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print ('total travel time = ' , total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print ('Average travel time = ' , mean_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_count = df['User Type'].value_counts() 
    print (user_count)
    
    #Display counts of gender
    try :
        print('gender count is : \n' , df["Gender"].value_counts())
    except:
        print ('No column called gender ')

    #Display earliest, most recent, and most common year of birth
    try :
        print('earliest Birth year is : \n' , df["Birth year"].min())
        print('most recent Birth year is : \n' , df["Birth year"].max())
        print('most common Birth year is : \n' , df["Birth year"].mode()[0])
    except:
        print ('No column called Birth year ')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def show_row_data (df):
    respone = input("Do you want to show five rows ? \n")
    
    while respone == 'yes':
        n = np.random.randint(0,300001,5)
        print (df.loc[n])
        
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        show_row_data(city)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
    


    
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
      




