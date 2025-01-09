import rasterio
import numpy as np
import logging
from rasterio.enums import Resampling

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def calculate_slope(dem_data, x_res, y_res, output_format):
    """
    Calculate the slope from a DEM raster.

    Parameters:
        dem_data (ndarray): 2D array of DEM elevation values.
        x_res (float): Resolution of the raster in the x-direction.
        y_res (float): Resolution of the raster in the y-direction.
        output_format (str): Desired slope output format ('percent', 'degrees', or 'raw').

    Returns:
        ndarray: 2D array of slope values in the chosen format.
    """
    logging.info("Calculating slope.")
    x_slope = np.gradient(dem_data, axis=1) / x_res
    y_slope = np.gradient(dem_data, axis=0) / y_res
    slope = np.sqrt(x_slope**2 + y_slope**2)

    # Convert slope based on the chosen format
    if output_format == "degrees":
        logging.info("Converting slope to degrees.")
        slope = np.arctan(slope) * (180 / np.pi)
    elif output_format == "percent":
        logging.info("Converting slope to percent.")
        slope = slope * 100
    elif output_format == "raw":
        logging.info("Keeping raw gradient values.")
    else:
        raise ValueError(f"Invalid slope format: {output_format}. Choose 'percent', 'degrees', or 'raw'.")

    return slope

def process_dem(src_file, slope_file, output_format):
    """
    Process the DEM file to calculate slope and save it to a new raster file.

    Parameters:
        src_file (str): Path to the input DEM file.
        slope_file (str): Path to save the slope raster file.
        output_format (str): Desired slope output format ('percent', 'degrees', or 'raw').
    """
    try:
        # Open the source DEM file
        logging.info(f"Opening DEM file: {src_file}")
        with rasterio.open(src_file) as src:
            # Read the DEM data
            dem_data = src.read(1)
            x_res, y_res = src.res

            # Calculate slope
            slope = calculate_slope(dem_data, x_res, y_res, output_format)

            # Write the slope to a new raster file
            logging.info(f"Saving slope raster to: {slope_file}")
            with rasterio.open(
                slope_file,
                'w',
                driver='GTiff',
                height=slope.shape[0],
                width=slope.shape[1],
                count=1,
                dtype=slope.dtype,
                crs=src.crs,
                transform=src.transform,
                nodata=src.nodata  # Preserve nodata value if present
            ) as dst:
                dst.write(slope, 1)

        logging.info("Slope calculation complete and saved successfully.")
    except Exception as e:
        logging.error(f"An error occurred: {e}")

def main():
    # File paths
    src_file = 'processed_data/dem.tif'
    slope_file = 'processed_data/slope.tif'

    # Prompt the user for the output slope format
    print("Choose the slope format for the calculation:")
    print("1. Percent (e.g., 100 for 100%)")
    print("2. Degrees (e.g., 45°)")
    print("3. Raw gradient values (default, no conversion)")

    choice = input("Enter your choice (1, 2, or 3): ").strip()
    if choice == "1":
        output_format = "percent"
    elif choice == "2":
        output_format = "degrees"
    elif choice == "3":
        output_format = "raw"
    else:
        print("Invalid choice. Defaulting to raw gradient values.")
        output_format = "raw"

    # Process the DEM to calculate slope
    process_dem(src_file, slope_file, output_format)

if __name__ == "__main__":
    main()
