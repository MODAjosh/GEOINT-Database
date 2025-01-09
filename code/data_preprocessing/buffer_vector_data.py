import geopandas as gpd
from pathlib import Path
from pyproj import CRS
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def validate_and_reproject_crs(gdf):
    """
    Validate the CRS of a GeoDataFrame and reproject to a projected CRS if needed.

    Parameters:
        gdf (GeoDataFrame): Input GeoDataFrame.

    Returns:
        GeoDataFrame: GeoDataFrame with a projected CRS.
    """
    try:
        if gdf.crs is None:
            raise ValueError("The input vector file has no CRS defined. Define a CRS for accurate buffering.")

        if not gdf.crs.is_projected:
            logging.warning("The CRS is not projected. Reprojecting to EPSG:3857 (Web Mercator) for accurate buffering.")
            gdf = gdf.to_crs(epsg=3857)
        return gdf
    except Exception as e:
        logging.error(f"Error validating CRS: {e}")
        raise

def create_buffered_geometries(vector_file, output_file, buffer_distance=500):
    """
    Create a buffer around each geometry in a vector file and save the result.

    Parameters:
        vector_file (str): Path to the input vector file.
        output_file (str): Path to save the buffered geometries.
        buffer_distance (float): Distance for the buffer in the CRS units (e.g., meters).
    """
    try:
        # Load the vector data
        logging.info(f"Loading vector data from: {vector_file}")
        gdf = gpd.read_file(vector_file)

        # Validate and reproject CRS if needed
        gdf = validate_and_reproject_crs(gdf)

        # Create a buffer around each geometry
        logging.info(f"Creating a buffer of {buffer_distance} units around each geometry.")
        gdf['buffered_geometry'] = gdf.geometry.buffer(buffer_distance)

        # Create a GeoDataFrame with buffered geometries
        buffered_gdf = gpd.GeoDataFrame(
            gdf.drop(columns='geometry'),  # Drop original geometry
            geometry='buffered_geometry',  # Set buffered geometries as the new geometry
            crs=gdf.crs  # Retain the original CRS
        )

        # Ensure output directory exists
        output_dir = Path(output_file).parent
        output_dir.mkdir(parents=True, exist_ok=True)

        # Save the buffered geometries to a new file
        logging.info(f"Saving buffered geometries to: {output_file}")
        buffered_gdf.to_file(output_file)

        logging.info("Buffering completed and file saved successfully.")

    except FileNotFoundError:
        logging.error(f"The input file does not exist: {vector_file}")
    except Exception as e:
        logging.error(f"An error occurred: {e}")

def main():
    # Define input and output file paths
    vector_file = 'data/vector_data.shp'
    output_file = 'data/processed/buffered_vector_data.shp'

    # Create buffered geometries
    create_buffered_geometries(vector_file, output_file, buffer_distance=500)

if __name__ == "__main__":
    main()
