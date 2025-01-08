import geopandas as gpd
from pathlib import Path
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

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

        logging.info(f"Loading shapefile: {shapefile2}")
        gdf2 = gpd.read_file(shapefile2)

        # Validate CRS and align if necessary
        if gdf1.crs != gdf2.crs:
            logging.info("CRS mismatch detected. Aligning CRS of the second shapefile to the first shapefile.")
            gdf2 = gdf2.to_crs(gdf1.crs)

        # Merge the two GeoDataFrames
        logging.info("Merging the two shapefiles.")
        merged_gdf = gpd.GeoDataFrame(pd.concat([gdf1, gdf2], ignore_index=True), crs=gdf1.crs)

        # Save the merged GeoDataFrame
        output_dir = Path(output_file).parent
        output_dir.mkdir(parents=True, exist_ok=True)
        logging.info(f"Saving merged shapefile to: {output_file}")
        merged_gdf.to_file(output_file)

        logging.info("Merging operation completed successfully.")

    except Exception as e:
        logging.error(f"An error occurred during the merging process: {e}")

def main():
    # Define file paths
    shapefile1 = 'shapefiles/your_shapefile1.shp'
    shapefile2 = 'shapefiles/your_shapefile2.shp'
    output_file = 'processed_data/merged_shapefile.shp'

    # Merge the shapefiles
    merge_shapefiles(shapefile1, shapefile2, output_file)

if __name__ == "__main__":
    main()
