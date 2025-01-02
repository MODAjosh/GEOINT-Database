import pandas as pd

# Load your data (assuming it's in a CSV file format)
data = pd.read_csv('raw_data/sensor_data.csv')

# Define an outlier removal function
def remove_outliers(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    return df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]

# Remove outliers from a specific column
cleaned_data = remove_outliers(data, 'sensor_reading')

# Save the cleaned data
cleaned_data.to_csv('processed_data/cleaned_sensor_data.csv', index=False)

print("Outliers have been removed and cleaned data saved.")

