import rasterio
from rasterio.warp import calculate_default_transform, reproject, Resampling
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
        ValueError: If the raster dataset is invalid or has no bands.
    """
    if src.count == 0:
        raise ValueError("The input raster has no bands. Ensure the file contains valid data.")

def calculate_transform(src_crs, target_crs, width, height, bounds):
    """
    Calculate the transform, width, and height for the target CRS.

    Parameters:
        src_crs (CRS): Source CRS of the raster.
        target_crs (str): Target CRS in EPSG code format.
        width (int): Width of the source raster.
        height (int): Height of the source raster.
        bounds (tuple): Bounds of the source raster.

    Returns:
        tuple: (Affine transform, width, height) for the target CRS.
    """
    try:
        logging.info(f"Calculating transform for target CRS: {target_crs}")
        return calculate_default_transform(src_crs, target_crs, width, height, *bounds)
    except Exception as e:
        logging.error(f"Error calculating transform: {e}")
        raise

def reproject_raster(src_file, dst_file, target_crs='EPSG:4326', resampling_method=Resampling.nearest):
    """
    Reproject a raster to a target CRS and save the result.

    Parameters:
        src_file (str): Path to the input raster file.
        dst_file (str): Path to save the reprojected raster file.
        target_crs (str): EPSG code for the target CRS (default is 'EPSG:4326').
        resampling_method (Resampling): Resampling method (default is Resampling.nearest).
    """
    try:
        logging.info(f"Opening source raster: {src_file}")
        with rasterio.open(src_file) as src:
            # Validate the raster data
            validate_raster(src)

            # Calculate transformation, width, and height for the new CRS
            transform, width, height = calculate_transform(
                src.crs, target_crs, src.width, src.height, src.bounds
            )

            # Create metadata for the destination file
            dst_meta = src.meta.copy()
            dst_meta.update({
                'crs': target_crs,
                'transform': transform,
                'width': width,
                'height': height
            })

            # Ensure output directory exists
            output_dir = Path(dst_file).parent
            output_dir.mkdir(parents=True, exist_ok=True)

            # Reproject and save the raster
            logging.info(f"Reprojecting raster and saving to: {dst_file}")
            with rasterio.open(dst_file, 'w', **dst_meta) as dst:
                for i in range(1, src.count + 1):
                    logging.info(f"Reprojecting band {i} of {src.count}")
                    reproject(
                        source=rasterio.band(src, i),
                        destination=rasterio.band(dst, i),
                        src_transform=src.transform,
                        src_crs=src.crs,
                        dst_transform=transform,
                        dst_crs=target_crs,
                        resampling=resampling_method
                    )

        logging.info("Reprojection completed successfully.")

    except FileNotFoundError:
        logging.error(f"File not found: {src_file}")
    except ValueError as e:
        logging.error(f"Validation error: {e}")
    except rasterio.errors.RasterioIOError as e:
        logging.error(f"Rasterio error: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred during reprojection: {e}")

def main():
    # Define input and output file paths
    src_file = 'raw_data/landsat_2020.tif'
    dst_file = 'processed_data/landsat_2020_reprojected.tif'

    # Reproject the raster
    reproject_raster(src_file, dst_file)

if __name__ == "__main__":
    main()
