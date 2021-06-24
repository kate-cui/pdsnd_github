import time
import pandas as pd

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTH_DATA=['january','februry','march','april','may','june','all']

DAY_DATA=['monday','tuesday','wednesday','thuresday','friday','saturday','sunday','all']

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
    city=input('Enter your city: \n').lower()
    while city not in CITY_DATA.keys():
        print('please choose your city among:/n 1.chicago,2.new york city,3.washington')
        city=input('Enter your city: \n').lower()
    print(city,'as your city')
           

    # TO DO: get user input for month (all, january, february, ... , june)
    month=input('Enter your month: \n').lower()
    while month not in MONTH_DATA:
        print('please choose your month between january to june, or input all for all months')
        month=input('Enter your month: \n').lower()
    print(month,'as your month')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day=input('Enter your day: \n').lower()
    while day not in DAY_DATA:
        print('please choose your day of a week, or input all for all week')
        day=input('Enter your day: \n').lower()
    print(day,'as your day')


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
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.day_name()
    df['hour']=df['Start Time'].dt.hour
    if month != 'all':
        months=['january','februry','march','april','may','june']
        month=months.index(month)+1
        df = df[df['month'] == month]
    if day != 'all':
        df = df[df['day'] == day]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    most_common_month=df['month'].mode()[0]
    print('the most common month is',most_common_month)
    # TO DO: display the most common day of week
    df['day'] = df['Start Time'].dt.day_name()
    most_common_day=df['day'].mode()[0]
    print('The most common day in a week is',most_common_day)

    # TO DO: display the most common start hour
    df['hour']=df['Start Time'].dt.hour
    most_common_hour=df['hour'].mode()[0]
    print('The most common hour in a day is',most_common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station=df['Start Station'].mode()[0]
    print('The most commonly used start station is', common_start_station)

    # TO DO: display most commonly used end station
    common_end_station=df['End Station'].mode()[0]
    print('The most commonly used end station is', common_end_station)


    # TO DO: display most frequent combination of start station and end station trip
    df['combination_station']=df['Start Station'].str.cat(df['End Station'],sep=' to ')
    common_comb_station = df['combination_station'].mode()[0]
    print('The most frequent combination of start station and end station trip is \n',common_comb_station)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time=df['Trip Duration'].sum()
    
    print('The total travel time is',total_time,'in second')
    # TO DO: display mean travel time
    mean_time=df['Trip Duration'].mean()
    print('The mean travel time is',mean_time,'in second')
          
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type=df['User Type'].value_counts()
    print('The count of user type is \n', user_type)

    # TO DO: Display counts of gender
    if 'Gender' in df:
        gender_count=df['Gender'].value_counts()
        print('The count of gender type is \n', gender_count, '\n')
    else:
        print('There is no gender information \n')


    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest=df['Birth Year'].min()
        print('The earlist year is: ',earliest)

        most_recent=df['Birth Year'].max()
        print('the most recent year is', most_recent)

        most_common_year=df['Birth Year'].mode()[0]
        print('The most common year of birth is',most_common_year)
    else:  
        print('There is no birth information')
          
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    raw_data = 0
    while True:
        answer = input("Do you want to see the raw data? Yes or No \n").lower()
        if answer not in ['yes', 'no']:
            answer = input("You wrote the wrong word. Please type Yes or No. \n").lower()
        elif answer == 'yes':
            raw_data += 5
        print(df.iloc[raw_data : raw_data + 5])
        again = input("Do you want to see more? Yes or No \n").lower()
        if again == 'no':
            break
        elif answer != 'no':
         return
    print('-'*80)


def main():

    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        display_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
     
            

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
