import rasterio
import numpy as np
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def calculate_and_save_ndvi(red_band, nir_band, output_file):
    """
    Calculate the NDVI from red and NIR raster bands and save the result.

    Parameters:
        red_band (str): Path to the red band raster file.
        nir_band (str): Path to the NIR band raster file.
        output_file (str): Path to save the NDVI raster.
    """
    try:
        logging.info(f"Opening red band: {red_band}")
        logging.info(f"Opening NIR band: {nir_band}")

        with rasterio.open(red_band) as red_src, rasterio.open(nir_band) as nir_src:
            # Check if both rasters have the same dimensions and georeferencing
            if red_src.shape != nir_src.shape:
                raise ValueError("The red and NIR bands must have the same dimensions.")
            if red_src.crs != nir_src.crs:
                raise ValueError("The red and NIR bands must have the same CRS.")

            # Read the red and NIR bands
            logging.info("Reading raster data.")
            red = red_src.read(1)
            nir = nir_src.read(1)

            # Calculate NDVI, handling division by zero
            logging.info("Calculating NDVI.")
            np.seterr(divide='ignore', invalid='ignore')  # Suppress warnings for invalid operations
            ndvi = (nir - red) / (nir + red)
            ndvi = np.nan_to_num(ndvi, nan=-9999)  # Replace NaN values with -9999

            # Save the NDVI result to a new raster file
            logging.info(f"Saving NDVI to: {output_file}")
            with rasterio.open(
                output_file, 'w',
                driver='GTiff',
                height=red_src.height,
                width=red_src.width,
                count=1,
                dtype=ndvi.dtype,
                crs=red_src.crs,
                transform=red_src.transform
            ) as dst:
                dst.write(ndvi, 1)

        logging.info("NDVI calculation and saving completed successfully.")

    except Exception as e:
        logging.error(f"An error occurred: {e}")

def main():
    # Define file paths
    red_band = 'raw_data/landsat_red.tif'
    nir_band = 'raw_data/landsat_nir.tif'
    output_file = 'processed_data/ndvi.tif'

    # Perform NDVI calculation and save the result
    calculate_and_save_ndvi(red_band, nir_band, output_file)

if __name__ == "__main__":
    main()
