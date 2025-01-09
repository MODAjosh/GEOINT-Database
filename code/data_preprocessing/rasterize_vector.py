import geopandas as gpd
import rasterio
from rasterio.features import rasterize
import numpy as np
import logging
from pathlib import Path

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def validate_and_reproject_vector(gdf, target_crs):
    """
    Validate and reproject a GeoDataFrame to match the target CRS.

    Parameters:
        gdf (GeoDataFrame): Input GeoDataFrame.
        target_crs (CRS): Target CRS to align with.

    Returns:
        GeoDataFrame: GeoDataFrame reprojected to the target CRS if necessary.
    """
    if gdf.crs != target_crs:
        logging.info("CRS mismatch detected. Reprojecting vector data to match raster CRS.")
        return gdf.to_crs(target_crs)
    return gdf

def rasterize_vector(vector_gdf, transform, out_shape, dtype=np.uint8, invert=False):
    """
    Rasterize a GeoDataFrame into a numpy array.

    Parameters:
        vector_gdf (GeoDataFrame): Input vector data.
        transform (Affine): Affine transformation matrix of the output raster.
        out_shape (tuple): Shape of the output raster (height, width).
        dtype (numpy dtype): Data type of the output raster.
        invert (bool): Whether to invert the rasterized values (default: False).

    Returns:
        ndarray: Rasterized numpy array.
    """
    try:
        logging.info("Rasterizing vector data.")
        return rasterize(
            [(geom, 1) for geom in vector_gdf.geometry],
            out_shape=out_shape,
            transform=transform,
            fill=0,
            all_touched=True,
            dtype=dtype
        )
    except Exception as e:
        logging.error(f"Error during rasterization: {e}")
        raise

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

        # Validate and reproject vector data CRS
        gdf = validate_and_reproject_vector(gdf, crs)

        # Rasterize vector data
        rasterized_data = rasterize_vector(gdf, transform, out_shape, dtype=dtype)

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
            dest.write(rasterized_data, 1)

        logging.info("Rasterization completed successfully.")

    except FileNotFoundError as e:
        logging.error(f"File not found: {e}")
    except ValueError as e:
        logging.error(f"Validation error: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred during rasterization: {e}")

def main():
    # File paths
    vector_file = 'data/vector_data.shp'
    raster_file = 'data/raw_raster.tif'
    output_raster = 'data/processed/rasterized_output.tif'

    # Rasterize vector data
    rasterize_vector_to_raster(vector_file, raster_file, output_raster)

if __name__ == "__main__":
    main()
