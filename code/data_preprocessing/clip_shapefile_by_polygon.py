import geopandas as gpd
from pathlib import Path
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def clip_shapefile_by_polygon(shapefile_to_clip, clip_polygon_file, output_file):
    """
    Clip a shapefile using a polygon and save the result.

    Parameters:
        shapefile_to_clip (str): Path to the shapefile to be clipped.
        clip_polygon_file (str): Path to the shapefile containing the clipping polygon.
        output_file (str): Path to save the clipped shapefile.
    """
    try:
        # Load the shapefile to clip
        logging.info(f"Loading shapefile to clip: {shapefile_to_clip}")
        gdf_to_clip = gpd.read_file(shapefile_to_clip)

        # Load the clipping polygon
        logging.info(f"Loading clipping polygon from: {clip_polygon_file}")
        clip_polygon = gpd.read_file(clip_polygon_file)

        # Validate CRS and align if necessary
        if gdf_to_clip.crs != clip_polygon.crs:
            logging.info("CRS mismatch detected. Aligning CRS of the shapefile to clip with the clipping polygon.")
            gdf_to_clip = gdf_to_clip.to_crs(clip_polygon.crs)

        # Perform the clipping operation
        logging.info("Clipping the shapefile using the clipping polygon.")
        clip_geometry = clip_polygon.geometry.unary_union
        clipped_gdf = gdf_to_clip[gdf_to_clip.geometry.intersects(clip_geometry)]

        # Save the clipped shapefile
        output_dir = Path(output_file).parent
        output_dir.mkdir(parents=True, exist_ok=True)
        logging.info(f"Saving clipped shapefile to: {output_file}")
        clipped_gdf.to_file(output_file)

        logging.info("Clipping operation completed successfully.")

    except Exception as e:
        logging.error(f"An error occurred during the clipping process: {e}")

def main():
    # Define input and output file paths
    shapefile_to_clip = 'data/raw_shapefile.shp'
    clip_polygon_file = 'data/aoi.shp'
    output_file = 'data/processed/clipped_shapefile.shp'

    # Clip the shapefile
    clip_shapefile_by_polygon(shapefile_to_clip, clip_polygon_file, output_file)

if __name__ == "__main__":
    main()

