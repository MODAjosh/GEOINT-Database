import rasterio
import logging
from pathlib import Path

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

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
            # Ensure output directory exists
            output_dir = Path(output_raster).parent
            output_dir.mkdir(parents=True, exist_ok=True)

            # Copy metadata and write to a GeoTIFF file
            logging.info(f"Converting raster to GeoTIFF format and saving to: {output_raster}")
            with rasterio.open(
                output_raster,
                'w',
                driver='GTiff',
                count=src.count,
                dtype=src.dtypes[0],
                crs=src.crs,
                transform=src.transform,
                width=src.width,
                height=src.height
            ) as dest:
                for i in range(1, src.count + 1):  # Iterate over all bands
                    dest.write(src.read(i), i)

        logging.info("Conversion to GeoTIFF completed successfully.")

    except Exception as e:
        logging.error(f"An error occurred during conversion: {e}")

def main():
    # Define file paths
    input_raster = 'data/raw_raster.xyz'
    output_raster = 'data/processed/output_raster.tif'

    # Convert raster to GeoTIFF
    convert_raster_to_geotiff(input_raster, output_raster)

if __name__ == "__main__":
    main()
