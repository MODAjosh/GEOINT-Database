import geopandas as gpd
import logging
from pathlib import Path

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def validate_geodataframe(gdf, input_path):
    """
    Validate that the GeoDataFrame contains valid data.

    Parameters:
        gdf (GeoDataFrame): GeoDataFrame to validate.
        input_path (str): File path for logging purposes.

    Raises:
        ValueError: If the GeoDataFrame is empty or invalid.
    """
    if gdf.empty:
        raise ValueError(f"The GeoDataFrame loaded from {input_path} is empty. Ensure the shapefile contains valid data.")

def ensure_output_directory(output_path):
    """
    Ensure the output directory exists.

    Parameters:
        output_path (str): Path to the output file.
    """
    output_dir = Path(output_path).parent
    output_dir.mkdir(parents=True, exist_ok=True)

def convert_shapefile_to_geojson(input_shapefile, output_geojson):
    """
    Convert a shapefile to GeoJSON format and save the result.

    Parameters:
        input_shapefile (str): Path to the input shapefile.
        output_geojson (str): Path to save the GeoJSON file.
    """
    try:
        # Load the shapefile
        logging.info(f"Loading shapefile: {input_shapefile}")
        gdf = gpd.read_file(input_shapefile)

        # Validate the GeoDataFrame
        validate_geodataframe(gdf, input_shapefile)

        # Ensure the output directory exists
        ensure_output_directory(output_geojson)

        # Convert and save as GeoJSON
        logging.info(f"Converting shapefile to GeoJSON and saving to: {output_geojson}")
        gdf.to_file(output_geojson, driver='GeoJSON')

        logging.info("Conversion to GeoJSON completed successfully.")
    except FileNotFoundError:
        logging.error(f"File not found: {input_shapefile}")
    except ValueError as e:
        logging.error(f"Validation error: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred during conversion: {e}")

def main():
    # File paths
    shapefile = 'shapefiles/your_shapefile.shp'
    output_geojson = 'processed_data/your_data.geojson'

    # Convert shapefile to GeoJSON
    convert_shapefile_to_geojson(shapefile, output_geojson)

if __name__ == "__main__":
    main()
