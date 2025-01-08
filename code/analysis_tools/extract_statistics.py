import rasterio
import numpy as np
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def calculate_raster_statistics(raster_file):
    """
    Calculate and print basic statistics (mean, median, max, min) for a raster file.

    Parameters:
        raster_file (str): Path to the input raster file.
    """
    try:
        logging.info(f"Opening raster file: {raster_file}")
        with rasterio.open(raster_file) as src:
            # Read the first band of raster data
            logging.info("Reading raster data.")
            data = src.read(1)
            
            # Handle nodata values if they exist
            nodata_value = src.nodata
            if nodata_value is not None:
                logging.info(f"Raster has nodata value: {nodata_value}. Ignoring nodata values in calculations.")
                data = np.where(data == nodata_value, np.nan, data)

            # Calculate statistics, ignoring nan values
            mean_value = np.nanmean(data)
            median_value = np.nanmedian(data)
            max_value = np.nanmax(data)
            min_value = np.nanmin(data)

            # Log and print the statistics
            logging.info("Calculating statistics.")
            logging.info(f"Mean: {mean_value}")
            logging.info(f"Median: {median_value}")
            logging.info(f"Max: {max_value}")
            logging.info(f"Min: {min_value}")

            print(f"Mean: {mean_value}")
            print(f"Median: {median_value}")
            print(f"Max: {max_value}")
            print(f"Min: {min_value}")

    except Exception as e:
        logging.error(f"An error occurred: {e}")

def main():
    # Define the raster file path
    raster_file = 'processed_data/dem.tif'

    # Calculate statistics
    calculate_raster_statistics(raster_file)

if __name__ == "__main__":
    main()
