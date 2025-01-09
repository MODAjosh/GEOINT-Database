import rasterio
import numpy as np
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def calculate_raster_statistics(raster_file):
    """
    Calculate basic statistics (mean, median, max, min) for a raster file.

    Parameters:
        raster_file (str): Path to the input raster file.

    Returns:
        dict: A dictionary containing raster statistics (mean, median, max, min).
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

            # Check if the raster data contains valid values
            if np.isnan(data).all():
                raise ValueError("The raster contains only nodata values. Statistics cannot be computed.")

            # Calculate statistics, ignoring nan values
            logging.info("Calculating statistics.")
            stats = {
                "mean": np.nanmean(data),
                "median": np.nanmedian(data),
                "max": np.nanmax(data),
                "min": np.nanmin(data),
            }

            # Log the statistics
            for key, value in stats.items():
                logging.info(f"{key.capitalize()}: {value}")

            return stats

    except FileNotFoundError:
        logging.error(f"File not found: {raster_file}")
    except rasterio.errors.RasterioIOError as e:
        logging.error(f"Rasterio error occurred: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

    return None

def print_statistics(stats):
    """
    Print raster statistics in a user-friendly format.

    Parameters:
        stats (dict): Dictionary containing raster statistics.
    """
    if stats:
        print("Raster Statistics:")
        print(f"Mean: {stats['mean']}")
        print(f"Median: {stats['median']}")
        print(f"Max: {stats['max']}")
        print(f"Min: {stats['min']}")
    else:
        print("No statistics available.")

def main():
    # Define the raster file path
    raster_file = 'processed_data/dem.tif'

    # Calculate statistics
    stats = calculate_raster_statistics(raster_file)

    # Print statistics
    print_statistics(stats)

if __name__ == "__main__":
    main()
