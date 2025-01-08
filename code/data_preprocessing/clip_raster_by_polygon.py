import geopandas as gpd
import rasterio
from rasterio.mask import mask
from pathlib import Path
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def clip_raster_with_polygon(raster_file, polygon_file, output_file):
    """
    Clip a raster file using a polygon shapefile and save the result.

    Parameters:
        raster_file (str): Path to the input raster file.
        polygon_file (str): Path to the polygon shapefile.
        output_file (str): Path to save the clipped raster.
    """
    try:
        # Load the polygon shapefile
        logging.info(f"Loading polygon shapefile from: {polygon_file}")
        aoi = gpd.read_file(polygon_file)

        # Validate the CRS and reproject if necessary
        logging.info("Validating CRS of the polygon and raster.")
        with rasterio.open(raster_file) as src:
            raster_crs = src.crs
            if aoi.crs != raster_crs:
                logging.info("CRS mismatch detected. Reprojecting AOI to match raster CRS.")
                aoi = aoi.to_crs(raster_crs)

            # Convert AOI geometry to GeoJSON format for masking
            logging.info("Converting AOI geometry to GeoJSON format.")
            geo_json = [aoi.geometry.unary_union.__geo_interface__]

            # Perform the mask operation
            logging.info("Clipping raster with the AOI polygon.")
            out_image, out_transform = mask(src, geo_json, crop=True)

            # Update metadata for the output raster
            out_meta = src.meta.copy()
            out_meta.update({
                "driver": "GTiff",
                "height": out_image.shape[1],
                "width": out_image.shape[2],
                "transform": out_transform
            })

            # Ensure output directory exists
            output_dir = Path(output_file).parent
            output_dir.mkdir(parents=True, exist_ok=True)

            # Save the clipped raster
            logging.info(f"Saving clipped raster to: {output_file}")
            with rasterio.open(output_file, 'w', **out_meta) as dest:
                dest.write(out_image, 1)

        logging.info("Clipping operation completed successfully.")

    except Exception as e:
        logging.error(f"An error occurred during raster clipping: {e}")

def main():
    # Define input and output file paths
    raster_file = 'data/raw_raster.tif'
    polygon_file = 'data/aoi.shp'
    output_file = 'data/processed/clip_raster_output.tif'

    # Perform the raster clipping
    clip_raster_with_polygon(raster_file, polygon_file, output_file)

if __name__ == "__main__":
    main()
