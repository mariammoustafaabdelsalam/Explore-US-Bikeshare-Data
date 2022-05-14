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

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('choose on of this city chicago ,new york city or washington:')
        if city  not in CITY_DATA :
            print('not valid city')

        else:
            break


    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        months=['january', 'february', 'march', 'april', 'may', 'june','all']
        month = input('choose month from january, february, march, april, may, june or all:')
        if month in months :
            break


        else:
            print('not valid month')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        days = ['saturday','sunday' , 'monday' ,'tuseday','wednesday','thursday','friday','all']
        day = input ('choose day from saturday,sunday , monday ,tuseday,wednesday,thursday,friday or all:')
        if day in days  :
            break


        else:
            print('not valid day')


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
        df - pandas DataFrame containing city data filtered by month and day
    """

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month =  months.index(month) + 1

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
    most_month=df['month'].mode()[0]
    print('the most common month :{}'.format(most_month))

    # TO DO: display the most common day of week
    most_day = df['day_of_week'].mode()[0]
    print('the most common day of week:{}'.format(most_day))


    # TO DO: display the most common start hour
    most_start_hour =df['hour'].mode()[0]
    print('the most common start hour:{}'.format(most_start_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_start_station= df['Start Station'].mode()[0]
    print('most commonly used start station: {}'.format(most_start_station))

    # TO DO: display most commonly used end station
    most_end_station= df['End Station'].mode()[0]
    print('most commonly used end station: {}'.format(most_end_station))
    # TO DO: display most frequent combination of start station and end station trip
    start_end_trip = (df['Start Station']+'--'+df['End Station']).mode()[0]
    print('most frequent combination of start station and end station trip: {}'.format(start_end_trip))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def trip_duration_stats(df):

    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = sum(df['Trip Duration'])
    print('total travel time in sec:{}, in min:{} ,in hour {}'.format(total_time,total_time/60,total_time/3600))

    # TO DO: display mean travel time
    mean_time = df['Trip Duration'].mean()
    print('mean travel time in sec:{} , in min:{} ,in hour {}'.format(mean_time,mean_time/60,mean_time/3600))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type = df['User Type'].value_counts()
    print('counts of user types:\n{}'.format(user_type))

    # TO DO: Display counts of gender
    if 'Gender' in df:
        gender = df['Gender'].value_counts()
        print('counts of gender:\n{}'.format(gender))
    else:
        print('No Gender data for this city')
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest = int(df['Birth Year'].min())
        print('earliest year of birth:{}'.format( earliest))
        print('most recent year of birth:',int(df['Birth Year'].max()))
        print('most common year of birth:',int(df['Birth Year'].mode()[0]))
    else:
        print('No Birth Year data for this city')
def  display_data(df):
    start_time = time.time()
    #TO DO : display rows of data
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
    start_loc = 0
    while True:
        if view_data.lower() == 'yes':
            print(df.iloc[start_loc:start_loc+5])
            start_loc += 5
            view_data = input("Do you wish to continue?: ").lower()
        else:
            print('thank you')
            break

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
        display_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            print('I hope the program helped you')
            print('good bye')
            break
if __name__ == "__main__":
	main()
