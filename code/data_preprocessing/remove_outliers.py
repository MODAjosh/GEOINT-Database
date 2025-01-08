import pandas as pd
import logging
from pathlib import Path
import matplotlib.pyplot as plt

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def remove_outliers(df, column):
    """
    Remove outliers from a specific column in a DataFrame using the IQR method.

    Parameters:
        df (pd.DataFrame): Input DataFrame.
        column (str): The column from which to remove outliers.

    Returns:
        pd.DataFrame: DataFrame with outliers removed.
    """
    try:
        logging.info(f"Removing outliers from column: {column}")
        Q1 = df[column].quantile(0.25)
        Q3 = df[column].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        logging.info(f"Calculated bounds for {column} - Lower: {lower_bound}, Upper: {upper_bound}")
        return df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]
    except Exception as e:
        logging.error(f"An error occurred while removing outliers from column {column}: {e}")
        return df  # Return the original DataFrame if an error occurs

def visualize_outliers(original_df, cleaned_df, column, output_dir):
    """
    Visualize the data distribution before and after outlier removal using boxplots.

    Parameters:
        original_df (pd.DataFrame): Original DataFrame before outlier removal.
        cleaned_df (pd.DataFrame): Cleaned DataFrame after outlier removal.
        column (str): Column to visualize.
        output_dir (str): Directory to save the visualizations.
    """
    try:
        logging.info(f"Creating boxplot visualization for column: {column}")
        plt.figure(figsize=(10, 6))

        # Plot original and cleaned data
        plt.boxplot(
            [original_df[column].dropna(), cleaned_df[column].dropna()],
            labels=["Original Data", "Cleaned Data"],
            patch_artist=True,
            boxprops=dict(facecolor="lightblue", color="blue"),
            medianprops=dict(color="red"),
        )

        plt.title(f"Outlier Visualization for '{column}'")
        plt.ylabel(column)
        plt.grid(axis="y", linestyle="--", alpha=0.7)

        # Save the visualization
        output_file = Path(output_dir) / f"outlier_visualization_{column}.png"
        plt.savefig(output_file)
        plt.close()
        logging.info(f"Visualization saved to: {output_file}")
    except Exception as e:
        logging.error(f"An error occurred while creating visualization for column {column}: {e}")

def clean_data(input_file, output_file, columns_to_clean, output_dir):
    """
    Clean the data by removing outliers from specified columns and save the result.

    Parameters:
        input_file (str): Path to the input CSV file.
        output_file (str): Path to save the cleaned data.
        columns_to_clean (list): List of column names to clean.
        output_dir (str): Directory to save visualizations.
    """
    try:
        # Load the data
        logging.info(f"Loading data from: {input_file}")
        data = pd.read_csv(input_file)
        original_data = data.copy()

        # Remove outliers for each specified column and visualize
        for column in columns_to_clean:
            if column in data.columns:
                cleaned_data = remove_outliers(data, column)
                visualize_outliers(original_data, cleaned_data, column, output_dir)
                data = cleaned_data
            else:
                logging.warning(f"Column {column} not found in the dataset. Skipping outlier removal for this column.")

        # Ensure output directory exists
        output_dir = Path(output_file).parent
        output_dir.mkdir(parents=True, exist_ok=True)

        # Save the cleaned data
        logging.info(f"Saving cleaned data to: {output_file}")
        data.to_csv(output_file, index=False)

        logging.info("Outlier removal, visualization, and data cleaning completed successfully.")
    except Exception as e:
        logging.error(f"An error occurred during data cleaning: {e}")

def main():
    # File paths
    input_file = 'raw_data/sensor_data.csv'
    output_file = 'processed_data/cleaned_sensor_data.csv'
    visualization_dir = 'processed_data/visualizations'

    # Columns to clean
    columns_to_clean = ['sensor_reading']

    # Clean the data
    clean_data(input_file, output_file, columns_to_clean, visualization_dir)

if __name__ == "__main__":
    main()
