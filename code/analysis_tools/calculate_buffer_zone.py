import os
import geopandas as gpd
from pathlib import Path
from pyproj import CRS
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def ensure_crs_in_meters(gdf):
    """
    Ensures the GeoDataFrame's CRS is in meters. Reprojects if necessary.

    Parameters:
        gdf (GeoDataFrame): The input GeoDataFrame.

    Returns:
        GeoDataFrame: A GeoDataFrame with a CRS in meters.
    """
    if gdf.crs is None:
        raise ValueError("Input file does not have a defined CRS.")

    crs = CRS.from_user_input(gdf.crs)
    if not crs.is_projected or crs.axis_info[0].unit_name != 'metre':
        logging.warning("CRS is not in meters. Reprojecting to EPSG:3857 (Web Mercator).")
        gdf = gdf.to_crs(epsg=3857)
    return gdf

def calculate_buffer(gdf, buffer_distance):
    """
    Calculates buffer zones around geometries.

    Parameters:
        gdf (GeoDataFrame): The input GeoDataFrame.
        buffer_distance (float): Distance for the buffer zone.

    Returns:
        GeoDataFrame: A GeoDataFrame with buffered geometries.
    """
    logging.info(f"Creating buffer zones with a distance of {buffer_distance} meters.")
    gdf['geometry'] = gdf.geometry.buffer(buffer_distance)
    return gdf

def process_shapefile(input_file, output_file, buffer_distance=100):
    """
    Loads a shapefile, calculates buffer zones, and saves the result.

    Parameters:
        input_file (str): Path to the input shapefile.
        output_file (str): Path to save the output file with buffers.
        buffer_distance (float): Distance for the buffer zone (default: 100 meters).
    """
    try:
        # Load geospatial data
        logging.info(f"Loading input file: {input_file}")
        gdf = gpd.read_file(input_file)

        # Ensure CRS is in meters
        gdf = ensure_crs_in_meters(gdf)

        # Calculate buffer zones
        gdf = calculate_buffer(gdf, buffer_distance)

        # Save the buffered geometries
        logging.info(f"Saving output to: {output_file}")
        gdf.to_file(output_file, driver="GPKG")  # GeoPackage format

        logging.info("Process completed successfully.")
    except FileNotFoundError:
        logging.error(f"Input file not found: {input_file}")
        raise
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        raise

def run_from_gui(input_file, buffer_distance, output_file):
    """
    Interface for running the buffer process from a GUI.

    Parameters:
        input_file (str): Path to the input shapefile.
        buffer_distance (float): Distance for the buffer zone.
        output_file (str): Path to save the output file with buffers.
    """
    try:
        process_shapefile(input_file, output_file, buffer_distance)
        logging.info("Process completed successfully through GUI.")
    except Exception as e:
        logging.error(f"Error while running from GUI: {e}")

def main():
    """
    Main function to define file paths and execute the buffer zone process via command-line.
    """
    import argparse

    parser = argparse.ArgumentParser(description="Calculate buffer zones for a shapefile.")
    parser.add_argument('--input', required=True, help="Path to the input shapefile")
    parser.add_argument('--buffer', required=False, type=float, default=100, help="Buffer distance in meters (default: 100)")
    parser.add_argument('--output', required=True, help="Path to save the output file")
    args = parser.parse_args()

    try:
        process_shapefile(args.input, args.output, args.buffer)
    except Exception as e:
        logging.error(f"Error while running from command line: {e}")

if __name__ == "__main__":
    main()
