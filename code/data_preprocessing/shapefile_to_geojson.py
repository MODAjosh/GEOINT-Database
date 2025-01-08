import geopandas as gpd
import logging
from pathlib import Path

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def convert_shapefile_to_geojson(input_shapefile, output_geojson):
    """
    Convert a shapefile to GeoJSON format and save the result.

    Parameters:
        input_shapefile (str): Path to the input shapefile.
        output_geojson (str): Path to save the GeoJSON file.
    """
    try:
        logging.info(f"Loading shapefile: {input_shapefile}")
        gdf = gpd.read_file(input_shapefile)

        # Ensure the output directory exists
        output_dir = Path(output_geojson).parent
        output_dir.mkdir(parents=True, exist_ok=True)

        # Convert and save as GeoJSON
        logging.info(f"Converting shapefile to GeoJSON and saving to: {output_geojson}")
        gdf.to_file(output_geojson, driver='GeoJSON')

        logging.info("Conversion to GeoJSON completed successfully.")
    except Exception as e:
        logging.error(f"An error occurred during conversion: {e}")

def main():
    # File paths
    shapefile = 'shapefiles/your_shapefile.shp'
    output_geojson = 'processed_data/your_data.geojson'

    # Convert shapefile to GeoJSON
    convert_shapefile_to_geojson(shapefile, output_geojson)

if __name__ == "__main__":
    main()
