import geopandas as gpd
from pathlib import Path
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def validate_and_align_crs(gdf, target_crs):
    """
    Validate the CRS of a GeoDataFrame and reproject it to the target CRS if necessary.

    Parameters:
        gdf (GeoDataFrame): The GeoDataFrame to validate.
        target_crs (CRS): The target CRS to align to.

    Returns:
        GeoDataFrame: Reprojected GeoDataFrame if CRS mismatch exists, or the original GeoDataFrame.
    """
    if gdf.crs != target_crs:
        logging.warning("CRS mismatch detected. Reprojecting to match the target CRS.")
        return gdf.to_crs(target_crs)
    return gdf

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

        if gdf_to_clip.empty:
            raise ValueError("The shapefile to clip is empty. Please provide a valid shapefile.")

        # Load the clipping polygon
        logging.info(f"Loading clipping polygon from: {clip_polygon_file}")
        clip_polygon = gpd.read_file(clip_polygon_file)

        if clip_polygon.empty:
            raise ValueError("The clipping polygon shapefile is empty. Please provide a valid polygon shapefile.")

        # Validate and align CRS
        logging.info("Validating and aligning CRS.")
        gdf_to_clip = validate_and_align_crs(gdf_to_clip, clip_polygon.crs)

        # Perform the clipping operation
        logging.info("Performing the clipping operation.")
        clip_geometry = clip_polygon.geometry.unary_union
        clipped_gdf = gdf_to_clip[gdf_to_clip.geometry.intersects(clip_geometry)]

        if clipped_gdf.empty:
            logging.warning("No geometries from the shapefile intersect with the clipping polygon.")

        # Ensure the output directory exists
        output_dir = Path(output_file).parent
        output_dir.mkdir(parents=True, exist_ok=True)

        # Save the clipped shapefile
        logging.info(f"Saving clipped shapefile to: {output_file}")
        clipped_gdf.to_file(output_file)

        logging.info("Clipping operation completed successfully.")

    except FileNotFoundError as e:
        logging.error(f"File not found: {e}")
    except ValueError as e:
        logging.error(f"Validation error: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred during the clipping process: {e}")

def main():
    # Define input and output file paths
    shapefile_to_clip = 'data/raw_shapefile.shp'
    clip_polygon_file = 'data/aoi.shp'
    output_file = 'data/processed/clipped_shapefile.shp'

    # Perform the clipping operation
    clip_shapefile_by_polygon(shapefile_to_clip, clip_polygon_file, output_file)

if __name__ == "__main__":
    main()
