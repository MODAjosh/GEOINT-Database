import geopandas as gpd
from geopy.distance import geodesic
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def calculate_distance_between_points(input_file):
    """
    Calculate the geodesic distance between the first two points in a GeoDataFrame.

    Parameters:
        input_file (str): Path to the shapefile containing point geometries.

    Returns:
        float: Distance between the first two points in meters.
    """
    try:
        # Load geospatial data
        logging.info(f"Loading shapefile from: {input_file}")
        gdf = gpd.read_file(input_file)

        # Ensure the GeoDataFrame contains point geometries
        if not all(gdf.geometry.geom_type == "Point"):
            raise ValueError("The input shapefile must contain only point geometries.")

        # Check that there are at least two points in the dataset
        if len(gdf) < 2:
            raise ValueError("The dataset must contain at least two points.")

        # Extract coordinates of the first two points
        point1 = gdf.geometry.iloc[0].coords[0]
        point2 = gdf.geometry.iloc[1].coords[0]

        # Calculate geodesic distance
        logging.info("Calculating the geodesic distance between the first two points.")
        distance = geodesic(point1, point2).meters

        logging.info(f"Distance between points: {distance:.2f} meters")
        return distance
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        return None

def main():
    # Define the input file path
    input_file = 'processed_data/points.shp'

    # Calculate the distance between the first two points
    distance = calculate_distance_between_points(input_file)

    if distance is not None:
        print(f"Distance between the first two points: {distance:.2f} meters")

if __name__ == "__main__":
    main()
