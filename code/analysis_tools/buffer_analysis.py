import os
import argparse
import geopandas as gpd
from pathlib import Path
from pyproj import CRS
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


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


def main():
    """
    Main function to load a shapefile, buffer geometries, and save the result.
    """
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Buffer geometries in a shapefile.")
    parser.add_argument('--input', required=True, help="Path to the input shapefile")
    parser.add_argument('--buffer', required=True, type=float, help="Buffer distance in meters")
    parser.add_argument('--output', required=True, help="Path to save the output file")
    args = parser.parse_args()

    input_file = args.input
    buffer_distance = args.buffer
    output_file = args.output

    # Ensure the input file exists
    if not os.path.exists(input_file):
        logging.error(f"Input file does not exist: {input_file}")
        return

    try:
        # Load geospatial data
        logging.info(f"Loading shapefile from: {input_file}")
        gdf = gpd.read_file(input_file)

        # Ensure CRS is in meters or reproject if needed
        gdf = ensure_crs_in_meters(gdf)

        # Create the buffer
        gdf = create_buffer(gdf, buffer_distance)

        # Ensure output directory exists
        output_dir = os.path.dirname(output_file)
        Path(output_dir).mkdir(parents=True, exist_ok=True)

        # Save the resulting buffered geometries
        logging.info(f"Saving buffered geometries to: {output_file}")
        gdf.to_file(output_file, driver='GPKG')

        logging.info("Process completed successfully.")
    except Exception as e:
        logging.error(f"An error occurred: {e}", exc_info=True)


if __name__ == "__main__":
    main()
