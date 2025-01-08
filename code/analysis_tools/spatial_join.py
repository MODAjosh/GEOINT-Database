import geopandas as gpd
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def perform_spatial_join(points_file, polygons_file, output_file):
    """
    Perform a spatial join to find points within polygons and save the results.

    Parameters:
        points_file (str): Path to the point shapefile.
        polygons_file (str): Path to the polygon shapefile.
        output_file (str): Path to save the resulting shapefile.
    """
    try:
        # Load geospatial datasets
        logging.info(f"Loading points data from: {points_file}")
        gdf_points = gpd.read_file(points_file)
        logging.info(f"Loading polygons data from: {polygons_file}")
        gdf_polygons = gpd.read_file(polygons_file)

        # Ensure both GeoDataFrames have the same CRS
        if gdf_points.crs != gdf_polygons.crs:
            logging.info("CRS mismatch detected. Aligning CRS of points to polygons.")
            gdf_points = gdf_points.to_crs(gdf_polygons.crs)

        # Perform spatial join (find points within polygons)
        logging.info("Performing spatial join to find points within polygons.")
        joined_gdf = gpd.sjoin(gdf_points, gdf_polygons, how='inner', predicate='within')

        # Save the results to a shapefile
        logging.info(f"Saving results to: {output_file}")
        joined_gdf.to_file(output_file)

        logging.info("Spatial join completed and results saved successfully.")

    except Exception as e:
        logging.error(f"An error occurred during the spatial join process: {e}")

def main():
    # Define file paths
    points_file = 'processed_data/points.shp'
    polygons_file = 'processed_data/polygons.shp'
    output_file = 'processed_data/spatial_joined_results.shp'

    # Perform spatial join
    perform_spatial_join(points_file, polygons_file, output_file)

if __name__ == "__main__":
    main()

