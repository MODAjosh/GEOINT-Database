import os
import geopandas as gpd
from pathlib import Path
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def calculate_buffer(input_file, output_file, buffer_distance=100):
    """
    Calculate buffer zones around geometries in a shapefile.

    Parameters:
        input_file (str): Path to the input shapefile.
        output_file (str): Path to save the output shapefile with buffers.
        buffer_distance (float): Distance for the buffer zone (default: 100 meters).
    """
    try:
        # Load geospatial data
        logging.info(f"Loading shapefile from: {input_file}")
        gdf = gpd.read_file(input_file)

        # Check CRS (Coordinate Reference System)
        if gdf.crs is None or 'units' not in gdf.crs or gdf.crs['units'] != 'm':
            raise ValueError("Shapefile CRS is not in meters. Ensure CRS is in meters for a proper buffer calculation.")

        # Calculate buffer zones
        logging.info(f"Calculating buffer zones with distance: {buffer_distance} meters.")
        gdf['buffer'] = gdf.geometry.buffer(buffer_distance)

        # Save buffer zones to a new shapefile
        logging.info(f"Saving buffer zones to: {output_file}")
        gdf[['buffer']].to_file(output_file)

        logging.info("Buffer zones have been successfully calculated and saved.")
    except Exception as e:
        logging.error(f"An error occurred: {e}")

def main():
    # Define file paths
    input_file = 'processed_data/merged_shapefile.shp'
    output_dir = 'processed_data'
    output_file = os.path.join(output_dir, 'buffer_zones.shp')

    # Ensure output directory exists
    Path(output_dir).mkdir(parents=True, exist_ok=True)

    # Calculate buffer zones
    calculate_buffer(input_file, output_file, buffer_distance=100)

if __name__ == "__main__":
    main()
