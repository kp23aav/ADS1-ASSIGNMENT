

import pandas as pd
import matplotlib.pyplot as plt


# Specify the file path to your CSV file
path = r'hotel_bookings.csv'


# Load the CSV file into a pandas DataFrame
df = pd.read_csv(path)
df.head()


def plot_guest_arrivals(dataframe):
    # Month mapping
    month_mapping = {
        'January': 1,
        'February': 2,
        'March': 3,
        'April': 4,
        'May': 5,
        'June': 6,
        'July': 7,
        'August': 8,
        'September': 9,
        'October': 10,
        'November': 11,
        'December': 12
    }

    # Replace the month names with numbers
    df['arrival_date_month_index'] = df['arrival_date_month'].replace(month_mapping)

    # Create a new column for the arrival date
    df['arrival_date'] = pd.to_datetime(df[['arrival_date_year', 'arrival_date_month_index', 'arrival_date_day_of_month']].rename(columns={'arrival_date_year': 'year', 'arrival_date_month_index': 'month', 'arrival_date_day_of_month': 'day'}))

    # Calculate the total number of guests
    df['total_guests'] = df['adults'] + df['children'] + df['babies']

    # Filter out canceled bookings
    not_cancelled = df[df['is_canceled'] == 0]

    # Group by arrival date and sum the total guests
    guests_arrival = not_cancelled.groupby('arrival_date')['total_guests'].sum()

    # Set the figure size
    plt.figure(figsize=(20, 6))
    
    guests_arrival.plot()

    # Add title
    plt.title('Total Guests Arrivals Over Time')

    # Add labels
    plt.xlabel('Date')
    plt.ylabel('Total Guests Arrived')

    # Add grid lines
    plt.grid(True, linestyle='--', alpha=0.7)

    # Customize the style
    plt.style.use('seaborn-darkgrid')

    # Show the plot
    plt.show()
    
    # Set the figure size
    plt.figure(figsize=(20, 6))

    # Plot total guests
    plt.plot(guests_arrival.index, guests_arrival, label='Total Guests', linewidth=2)

    # Plot number of adults
    adults_arrival = not_cancelled.groupby('arrival_date')['adults'].sum()
    plt.plot(adults_arrival.index, adults_arrival, label='Number of Adults', linestyle='--', linewidth=2)

    # Add title
    plt.title('Guest Arrivals Over Time')

    # Add labels
    plt.xlabel('Date')
    plt.ylabel('Count')

    # Add legend
    plt.legend()

    # Add grid lines
    plt.grid(True, linestyle='--', alpha=0.7)

    # Customize the style
    plt.style.use('seaborn-darkgrid')

    # Show the plot
    plt.show()

# Example usage with a DataFrame named 'your_dataframe'
plot_guest_arrivals(df)



def plot_market_segment_distribution(file_path):
    # Load the CSV file into a pandas DataFrame
    df = pd.read_csv(file_path)

    # Set the figure size
    plt.figure(figsize=(12, 6))

    # Plot the bar chart
    df['market_segment'].value_counts().plot(kind='bar', color='skyblue')

    # Add title and labels
    plt.title('Distribution of Market Segments')
    plt.xlabel('Market Segment')
    plt.ylabel('Count')

    # Rotate x-axis labels for better visibility
    plt.xticks(rotation=45)

    # Show the plot
    plt.show()

def plot_scatter_total_guests_vs_adr(file_path):
    # Load the CSV file into a pandas DataFrame
    df = pd.read_csv(file_path)

    # Set the figure size
    plt.figure(figsize=(10, 6))
    df['total_guests'] = df['adults'] + df['children'] + df['babies']

    # Create a scatter plot
    plt.scatter(df['total_guests'], df['adr'], alpha=0.5, color='orange')

    # Add title and labels
    plt.title('Scatter Plot: Total Guests vs. Average Daily Rate')
    plt.xlabel('Total Guests')
    plt.ylabel('Average Daily Rate')

    # Show the plot
    plt.grid(True)
    plt.show()

# Specify the file path to your CSV file
file_path = r'hotel_bookings.csv'

# Call each function with the file path

plot_market_segment_distribution(file_path)
plot_scatter_total_guests_vs_adr(file_path)
