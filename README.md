Bikeshare project:

it's devide into functions , and it's a pref for each function :

1- def get_filters():
 Filter on cities , day and month defined by user 

2- load_data(city,month,day):
  a - load data file into a dataframe
  b - convert the Start Time column to datetime
  c- extract month and day of week from Start Time to create new columns
  d- filter by month if applicable
  e- use the index of the months list to get the corresponding int
  f- filter by month to create the new dataframe
  g -filter by day of week if applicable
  h- filter by day of week to create the new dataframe
       
3-  time_stats(df):
 a- extract hour from the Start Time column to create an hour column
 b- find the most common hour , day and month

4- station_stats(df):
    a- display most commonly used start station
    b- display most commonly used end station
    c- display most frequent combination of start station and end station trip

5- trip_duration_stats(df):
    a- display total travel time
    b- display mean travel time

6-  user_stats(df):
    a- Display counts of user types
    b- Display counts of gender
    c- Display earliest, most recent, and most common year of birth

7- show_row_data (df):
    ask user if he need to display 5 rows of data or no 

8- main function:
   call all above of above functions .


  
