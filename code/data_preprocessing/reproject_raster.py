import rasterio
from rasterio.warp import calculate_default_transform, reproject, Resampling
import logging
from pathlib import Path

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

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
            # Calculate transformation, width, and height for the new CRS
            logging.info(f"Calculating transform for target CRS: {target_crs}")
            transform, width, height = calculate_default_transform(
                src.crs, target_crs, src.width, src.height, *src.bounds
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

    except Exception as e:
        logging.error(f"An error occurred during reprojection: {e}")

def main():
    # Define input and output file paths
    src_file = 'raw_data/landsat_2020.tif'
    dst_file = 'processed_data/landsat_2020_reprojected.tif'

    # Reproject the raster
    reproject_raster(src_file, dst_file)

if __name__ == "__main__":
    main()

