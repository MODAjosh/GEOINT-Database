import geopandas as gpd
import rasterio
from rasterio.mask import mask
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def validate_shapefile(gdf):
    """
    Validate that the GeoDataFrame contains only valid polygon geometries.

    Parameters:
        gdf (GeoDataFrame): GeoDataFrame to validate.

    Returns:
        geometry (list): A unified geometry list for raster masking.

    Raises:
        ValueError: If the GeoDataFrame contains invalid geometries.
    """
    if gdf.empty:
        raise ValueError("The shapefile is empty. Please provide a valid shapefile with polygon geometries.")
    
    if not gdf.geometry.is_valid.all():
        raise ValueError("The shapefile contains invalid geometries. Please fix or validate the shapefile.")

    if not gdf.geometry.type.isin(["Polygon", "MultiPolygon"]).all():
        raise ValueError("The shapefile must contain only Polygon or MultiPolygon geometries.")
    
    # Combine all geometries into a single geometry for masking
    return [gdf.geometry.unary_union]

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

        # Validate shapefile geometries
        geometry = validate_shapefile(gdf)

        # Load the raster file
        logging.info(f"Loading raster file: {raster_file}")
        with rasterio.open(raster_file) as src:
            # Clip the raster using the shapefile geometry
            logging.info("Clipping raster with the shapefile geometry.")
            out_image, out_transform = mask(src, geometry, crop=True, nodata=src.nodata)

            # Save the clipped raster
            logging.info(f"Saving clipped raster to: {output_file}")
            with rasterio.open(
                output_file,
                'w',
                driver='GTiff',
                height=out_image.shape[1],
                width=out_image.shape[2],
                count=src.count,
                dtype=out_image.dtype,
                crs=src.crs,
                transform=out_transform,
                nodata=src.nodata
            ) as dst:
                dst.write(out_image, 1)

        logging.info("Raster clipping completed successfully.")
    except FileNotFoundError as e:
        logging.error(f"File not found: {e}")
    except ValueError as e:
        logging.error(f"Validation error: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

def main():
    # Define file paths
    raster_file = 'processed_data/dem.tif'
    shapefile = 'processed_data/clip_polygon.shp'
    output_file = 'processed_data/clipped_dem.tif'

    # Perform raster clipping
    clip_raster_with_shapefile(raster_file, shapefile, output_file)

if __name__ == "__main__":
    main()
