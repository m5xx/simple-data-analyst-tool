import pandas as pd
import matplotlib.pyplot as plt

def load_data(file_path):
    # Load data from the CSV file into a pandas DataFrame
    data = pd.read_csv(file_path)
    return data

def basic_data_analysis(data):
    # Perform basic data analysis
    summary_stats = data.describe()
    return summary_stats

def plot_data(data):
    # Visualize the data
    data.plot(x='Date', y='Revenue', kind='line', marker='o', title='Revenue Trend')
    plt.xlabel('Date')
    plt.ylabel('Revenue')
    plt.show()

def main():
    # Get the input file from the user
    file_path = input("Enter the path to the CSV file: ")

    # Load the data
    data = load_data(file_path)

    # Display basic data analysis
    print("\nBasic Data Analysis:")
    print(basic_data_analysis(data))

    # Plot the data
    plot_data(data)

if __name__ == "__main__":
    main()
