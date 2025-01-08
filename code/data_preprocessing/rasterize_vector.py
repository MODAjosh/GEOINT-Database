import geopandas as gpd
import rasterio
from rasterio.features import geometry_mask
import numpy as np
import logging
from pathlib import Path

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def rasterize_vector_to_raster(vector_file, raster_file, output_raster):
    """
    Rasterize vector data using the specifications of an input raster and save the output.

    Parameters:
        vector_file (str): Path to the input vector file (e.g., shapefile or GeoJSON).
        raster_file (str): Path to the reference raster file for specifications.
        output_raster (str): Path to save the rasterized output.
    """
    try:
        logging.info(f"Loading vector data from: {vector_file}")
        gdf = gpd.read_file(vector_file)

        # Load reference raster for specs
        logging.info(f"Loading reference raster: {raster_file}")
        with rasterio.open(raster_file) as src:
            out_shape = (src.height, src.width)
            transform = src.transform
            crs = src.crs
            dtype = np.uint8

        # Check CRS compatibility
        if gdf.crs != crs:
            logging.info("CRS mismatch detected. Reprojecting vector data to match raster CRS.")
            gdf = gdf.to_crs(crs)

        # Create rasterized mask
        logging.info("Rasterizing vector data.")
        mask = geometry_mask(
            [geometry for geometry in gdf.geometry],
            transform=transform,
            invert=True,
            out_shape=out_shape
        )

        # Ensure output directory exists
        output_dir = Path(output_raster).parent
        output_dir.mkdir(parents=True, exist_ok=True)

        # Save the rasterized output
        logging.info(f"Saving rasterized output to: {output_raster}")
        with rasterio.open(
            output_raster,
            'w',
            driver='GTiff',
            count=1,
            dtype=dtype,
            crs=crs,
            transform=transform,
            width=out_shape[1],
            height=out_shape[0]
        ) as dest:
            dest.write(mask.astype(dtype), 1)

        logging.info("Rasterization completed successfully.")

    except Exception as e:
        logging.error(f"An error occurred during rasterization: {e}")

def main():
    # File paths
    vector_file = 'data/vector_data.shp'
    raster_file = 'data/raw_raster.tif'
    output_raster = 'data/processed/rasterized_output.tif'

    # Rasterize vector data
    rasterize_vector_to_raster(vector_file, raster_file, output_raster)

if __name__ == "__main__":
    main()
