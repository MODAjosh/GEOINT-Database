import os
import geopandas as gpd
from pathlib import Path
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    # Define file paths
    input_file = 'data/shapefiles/my_shapefile.shp'
    output_dir = 'results'
    output_file = os.path.join(output_dir, 'buffered_geometries.shp')

    # Ensure the output directory exists
    Path(output_dir).mkdir(parents=True, exist_ok=True)

    try:
        # Load geospatial data
        logging.info(f"Loading shapefile from: {input_file}")
        gdf = gpd.read_file(input_file)
        
        # Check CRS (Coordinate Reference System)
        if gdf.crs is None or 'units' not in gdf.crs or gdf.crs['units'] != 'm':
            raise ValueError("Shapefile CRS is not in meters. Ensure CRS is in meters for a 100-meter buffer.")

        # Create a 100-meter buffer around each feature
        logging.info("Creating 100-meter buffer around each feature.")
        gdf['buffer'] = gdf.geometry.buffer(100)

        # Save the resulting buffered geometries
        logging.info(f"Saving buffered geometries to: {output_file}")
        gdf.to_file(output_file)

        logging.info("Process completed successfully.")
    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
