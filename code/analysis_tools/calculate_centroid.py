import os
import geopandas as gpd
from pathlib import Path
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def calculate_centroids(input_file, output_file):
    """
    Calculate centroids of polygons in a shapefile.

    Parameters:
        input_file (str): Path to the input shapefile containing polygons.
        output_file (str): Path to save the output shapefile with centroids.
    """
    try:
        # Load geospatial data
        logging.info(f"Loading shapefile from: {input_file}")
        gdf = gpd.read_file(input_file)

        # Check if geometries are valid polygons
        if not gdf.geometry.is_valid.all():
            raise ValueError("Invalid geometries detected. Please validate or fix the geometries before proceeding.")

        if not all(gdf.geometry.geom_type == "Polygon") and not all(gdf.geometry.geom_type == "MultiPolygon"):
            raise ValueError("Input file must contain only polygon or multipolygon geometries.")

        # Calculate centroids
        logging.info("Calculating centroids for the polygons.")
        gdf['centroid'] = gdf.geometry.centroid

        # Create a new GeoDataFrame for centroids
        centroids_gdf = gpd.GeoDataFrame(gdf[['centroid']], geometry='centroid', crs=gdf.crs)

        # Save centroids to a new shapefile
        logging.info(f"Saving centroids to: {output_file}")
        centroids_gdf.to_file(output_file)

        logging.info("Centroids have been successfully calculated and saved.")
    except Exception as e:
        logging.error(f"An error occurred: {e}")

def main():
    # Define file paths
    input_file = 'processed_data/merged_shapefile.shp'
    output_dir = 'processed_data'
    output_file = os.path.join(output_dir, 'centroids.shp')

    # Ensure the output directory exists
    Path(output_dir).mkdir(parents=True, exist_ok=True)

    # Calculate centroids
    calculate_centroids(input_file, output_file)

if __name__ == "__main__":
    main()
