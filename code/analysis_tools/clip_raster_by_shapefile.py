import geopandas as gpd
import rasterio
from rasterio.mask import mask
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def clip_raster_with_shapefile(raster_file, shapefile, output_file):
    """
    Clip a raster file using a polygon shapefile and save the result.

    Parameters:
        raster_file (str): Path to the input raster file.
        shapefile (str): Path to the shapefile containing the polygon geometry.
        output_file (str): Path to save the clipped raster.
    """
    try:
        # Load the shapefile
        logging.info(f"Loading shapefile: {shapefile}")
        gdf = gpd.read_file(shapefile)

        # Ensure the shapefile contains valid polygon geometries
        if not all(gdf.geometry.geom_type.isin(['Polygon', 'MultiPolygon'])):
            raise ValueError("The shapefile must contain only polygon geometries.")

        # Load the raster file
        logging.info(f"Loading raster file: {raster_file}")
        with rasterio.open(raster_file) as src:
            # Create a single geometry from the shapefile
            geometry = [gdf.geometry.unary_union]

            # Mask the raster with the shapefile geometry
            logging.info("Clipping raster with the shapefile geometry.")
            out_image, out_transform = mask(src, geometry, crop=True)

            # Save the clipped raster
            logging.info(f"Saving clipped raster to: {output_file}")
            with rasterio.open(
                output_file, 'w',
                driver='GTiff',
                height=out_image.shape[1],
                width=out_image.shape[2],
                count=1,
                dtype=out_image.dtype,
                crs=src.crs,
                transform=out_transform
            ) as dst:
                dst.write(out_image, 1)

        logging.info("Raster clipping completed successfully.")
    except Exception as e:
        logging.error(f"An error occurred: {e}")

def main():
    # Define file paths
    raster_file = 'processed_data/dem.tif'
    shapefile = 'processed_data/clip_polygon.shp'
    output_file = 'processed_data/clipped_dem.tif'

    # Perform raster clipping
    clip_raster_with_shapefile(raster_file, shapefile, output_file)

if __name__ == "__main__":
    main()

