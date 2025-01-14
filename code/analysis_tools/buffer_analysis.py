import os
import argparse
import geopandas as gpd
from pathlib import Path
from pyproj import CRS
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define the processed data directory
# Note: Update this path for different environments or users
PROCESSED_DATA_DIR = r"C:\Users\Josh\Documents\GitHub\GEOINT-Database\data\processed_data"
Path(PROCESSED_DATA_DIR).mkdir(parents=True, exist_ok=True)


def ensure_crs_in_meters(gdf):
    """
    Ensures the GeoDataFrame has a CRS in meters. Reprojects if necessary.
    :param gdf: GeoDataFrame
    :return: GeoDataFrame with CRS in meters
    """
    if gdf.crs is None:
        raise ValueError("The GeoDataFrame does not have a defined CRS.")

    crs = CRS.from_user_input(gdf.crs)
    if not crs.is_projected or crs.axis_info[0].unit_name != 'metre':
        logging.warning("CRS is not in meters. Reprojecting to EPSG:3857.")
        gdf = gdf.to_crs(epsg=3857)
    return gdf


def create_buffer(gdf, distance):
    """
    Creates a buffer around the geometries in the GeoDataFrame.
    :param gdf: GeoDataFrame
    :param distance: Buffer distance in meters
    :return: GeoDataFrame with buffered geometries
    """
    logging.info(f"Buffering geometries with a {distance}-meter buffer.")
    gdf['geometry'] = gdf.geometry.buffer(distance)
    return gdf


def run_buffer_analysis(input_file, buffer_distance, output_file_name):
    """
    Executes the buffer analysis process.
    :param input_file: Path to the input shapefile
    :param buffer_distance: Buffer distance in meters
    :param output_file_name: Name of the output file to be saved in processed_data
    """
    output_file = os.path.join(PROCESSED_DATA_DIR, output_file_name)

    if not os.path.exists(input_file):
        raise FileNotFoundError(f"Input file does not exist: {input_file}")

    logging.info(f"Loading shapefile from: {input_file}")
    gdf = gpd.read_file(input_file)

    gdf = ensure_crs_in_meters(gdf)
    gdf = create_buffer(gdf, buffer_distance)

    logging.info(f"Saving buffered geometries to: {output_file}")
    gdf.to_file(output_file, driver='GPKG')

    logging.info("Process completed successfully.")


def main():
    """
    Main function to load a shapefile, buffer geometries, and save the result.
    """
    parser = argparse.ArgumentParser(description="Buffer geometries in a shapefile.")
    parser.add_argument('--input', required=True, help="Path to the input shapefile")
    parser.add_argument('--buffer', required=True, type=float, help="Buffer distance in meters")
    parser.add_argument('--output', required=True, help="Name of the output file (to be saved in processed_data)")
    args = parser.parse_args()

    try:
        run_buffer_analysis(args.input, args.buffer, args.output)
    except Exception as e:
        logging.error(f"An error occurred: {e}", exc_info=True)


if __name__ == "__main__":
    main()
