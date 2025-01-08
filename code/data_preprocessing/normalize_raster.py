import rasterio
import numpy as np
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def normalize_raster(raster_file, output_file):
    """
    Normalize the values of a raster file to the range [0, 1] and save the result.

    Parameters:
        raster_file (str): Path to the input raster file.
        output_file (str): Path to save the normalized raster file.
    """
    try:
        logging.info(f"Opening raster file: {raster_file}")
        with rasterio.open(raster_file) as src:
            # Read the first band of the raster
            data = src.read(1)

            # Handle nodata values if present
            nodata = src.nodata
            if nodata is not None:
                logging.info(f"Nodata value detected: {nodata}. Ignoring nodata values during normalization.")
                valid_mask = data != nodata
            else:
                valid_mask = np.ones_like(data, dtype=bool)

            # Calculate min and max of valid data
            min_value = np.min(data[valid_mask])
            max_value = np.max(data[valid_mask])

            logging.info(f"Min value: {min_value}, Max value: {max_value}")

            # Normalize data to the range [0, 1]
            normalized_data = np.zeros_like(data, dtype=np.float32)
            normalized_data[valid_mask] = (data[valid_mask] - min_value) / (max_value - min_value)

            # Replace nodata values with original nodata value
            if nodata is not None:
                normalized_data[~valid_mask] = nodata

            # Save the normalized raster
            logging.info(f"Saving normalized raster to: {output_file}")
            meta = src.meta.copy()
            meta.update({
                "dtype": "float32",
                "driver": "GTiff"
            })

            with rasterio.open(output_file, 'w', **meta) as dest:
                dest.write(normalized_data, 1)

        logging.info("Normalization and saving completed successfully.")

    except Exception as e:
        logging.error(f"An error occurred: {e}")

def main():
    raster_file = 'data/raw_raster.tif'
    output_file = 'data/processed/normalized_raster.tif'
    normalize_raster(raster_file, output_file)

if __name__ == "__main__":
    main()
