import geopandas as gpd
from pathlib import Path
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def validate_and_align_crs(gdf1, gdf2):
    """
    Validate and align the CRS of two GeoDataFrames.

    Parameters:
        gdf1 (GeoDataFrame): The first GeoDataFrame.
        gdf2 (GeoDataFrame): The second GeoDataFrame.

    Returns:
        GeoDataFrame: The second GeoDataFrame reprojected to match the CRS of the first GeoDataFrame, if needed.
    """
    if gdf1.crs != gdf2.crs:
        logging.warning("CRS mismatch detected. Reprojecting the second GeoDataFrame to match the first.")
        return gdf2.to_crs(gdf1.crs)
    return gdf2

def validate_geodataframe(gdf, file_path):
    """
    Validate that a GeoDataFrame is not empty and contains valid geometries.

    Parameters:
        gdf (GeoDataFrame): The GeoDataFrame to validate.
        file_path (str): The file path for logging purposes.

    Raises:
        ValueError: If the GeoDataFrame is empty or invalid.
    """
    if gdf.empty:
        raise ValueError(f"The GeoDataFrame loaded from {file_path} is empty. Ensure the file contains valid data.")

def merge_shapefiles(shapefile1, shapefile2, output_file):
    """
    Merge two shapefiles or GeoJSONs into a single GeoDataFrame and save the result.

    Parameters:
        shapefile1 (str): Path to the first shapefile or GeoJSON.
        shapefile2 (str): Path to the second shapefile or GeoJSON.
        output_file (str): Path to save the merged shapefile.
    """
    try:
        # Load the shapefiles
        logging.info(f"Loading shapefile: {shapefile1}")
        gdf1 = gpd.read_file(shapefile1)
        validate_geodataframe(gdf1, shapefile1)

        logging.info(f"Loading shapefile: {shapefile2}")
        gdf2 = gpd.read_file(shapefile2)
        validate_geodataframe(gdf2, shapefile2)

        # Validate and align CRS
        logging.info("Validating and aligning CRS if necessary.")
        gdf2 = validate_and_align_crs(gdf1, gdf2)

        # Merge the two GeoDataFrames
        logging.info("Merging the two shapefiles.")
        merged_gdf = gpd.GeoDataFrame(pd.concat([gdf1, gdf2], ignore_index=True), crs=gdf1.crs)

        # Ensure the output directory exists
        output_dir = Path(output_file).parent
        output_dir.mkdir(parents=True, exist_ok=True)

        # Save the merged GeoDataFrame
        logging.info(f"Saving merged shapefile to: {output_file}")
        merged_gdf.to_file(output_file)

        logging.info("Merging operation completed successfully.")

    except FileNotFoundError as e:
        logging.error(f"File not found: {e}")
    except ValueError as e:
        logging.error(f"Validation error: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred during the merging process: {e}")

def main():
    # Define file paths
    shapefile1 = 'shapefiles/your_shapefile1.shp'
    shapefile2 = 'shapefiles/your_shapefile2.shp'
    output_file = 'processed_data/merged_shapefile.shp'

    # Merge the shapefiles
    merge_shapefiles(shapefile1, shapefile2, output_file)

if __name__ == "__main__":
    main()
