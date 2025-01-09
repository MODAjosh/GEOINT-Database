import rasterio
import logging
from pathlib import Path

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def validate_raster(src):
    """
    Validate the input raster to ensure it contains valid data.

    Parameters:
        src (DatasetReader): Opened raster dataset.

    Raises:
        ValueError: If the raster dataset is empty or invalid.
    """
    if src.count == 0:
        raise ValueError("The input raster has no bands. Ensure the file contains valid data.")

def extract_metadata(src):
    """
    Extract metadata from the input raster.

    Parameters:
        src (DatasetReader): Opened raster dataset.

    Returns:
        dict: Metadata for the output raster.
    """
    return {
        "driver": "GTiff",
        "count": src.count,
        "dtype": src.dtypes[0],
        "crs": src.crs,
        "transform": src.transform,
        "width": src.width,
        "height": src.height
    }

def convert_raster_to_geotiff(input_raster, output_raster):
    """
    Convert an input raster to GeoTIFF format and save the result.

    Parameters:
        input_raster (str): Path to the input raster file.
        output_raster (str): Path to save the GeoTIFF output.
    """
    try:
        logging.info(f"Opening input raster: {input_raster}")
        with rasterio.open(input_raster) as src:
            # Validate the raster data
            validate_raster(src)

            # Ensure output directory exists
            output_dir = Path(output_raster).parent
            output_dir.mkdir(parents=True, exist_ok=True)

            # Extract metadata for the output raster
            metadata = extract_metadata(src)

            # Write data to GeoTIFF
            logging.info(f"Converting raster to GeoTIFF format and saving to: {output_raster}")
            with rasterio.open(output_raster, 'w', **metadata) as dest:
                for i in range(1, src.count + 1):  # Iterate over all bands
                    logging.info(f"Processing band {i} of {src.count}")
                    dest.write(src.read(i), i)

        logging.info("Conversion to GeoTIFF completed successfully.")

    except FileNotFoundError:
        logging.error(f"File not found: {input_raster}")
    except ValueError as e:
        logging.error(f"Validation error: {e}")
    except rasterio.errors.RasterioIOError as e:
        logging.error(f"Rasterio error occurred: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred during conversion: {e}")

def main():
    # Define file paths
    input_raster = 'data/raw_raster.xyz'
    output_raster = 'data/processed/output_raster.tif'

    # Convert raster to GeoTIFF
    convert_raster_to_geotiff(input_raster, output_raster)

if __name__ == "__main__":
    main()
