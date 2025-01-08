import geopandas as gpd
from shapely.geometry import Point, Polygon
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def calculate_polygon_areas(gdf):
    """
    Calculate the area of polygons in a GeoDataFrame.

    Parameters:
        gdf (GeoDataFrame): The GeoDataFrame containing polygon geometries.

    Returns:
        GeoDataFrame: The updated GeoDataFrame with a new 'area' column.
    """
    try:
        # Ensure geometries are polygons
        if not all(gdf.geometry.geom_type.isin(['Polygon', 'MultiPolygon'])):
            raise ValueError("GeoDataFrame contains non-polygon geometries.")

        # Calculate area for polygons
        logging.info("Calculating areas for polygons.")
        gdf['area'] = gdf.geometry.area
        return gdf
    except Exception as e:
        logging.error(f"An error occurred while calculating areas: {e}")
        return gdf

def check_point_within_polygon(gdf, point_coords):
    """
    Check if a point is inside the first polygon in the GeoDataFrame.

    Parameters:
        gdf (GeoDataFrame): The GeoDataFrame containing polygon geometries.
        point_coords (tuple): The coordinates of the point (longitude, latitude).

    Returns:
        bool: True if the point is inside the polygon, False otherwise.
    """
    try:
        # Create a Point object
        point = Point(point_coords)
        logging.info(f"Checking if point {point_coords} is within the first polygon.")

        # Ensure the first geometry is a polygon
        polygon = gdf.geometry.iloc[0]
        if polygon.geom_type not in ['Polygon', 'MultiPolygon']:
            raise ValueError("The first geometry is not a polygon.")

        return polygon.contains(point)
    except Exception as e:
        logging.error(f"An error occurred while checking point containment: {e}")
        return False

def main():
    # Load the shapefile or GeoJSON
    input_file = 'processed_data/merged_shapefile.shp'
    logging.info(f"Loading file: {input_file}")
    gdf = gpd.read_file(input_file)

    # Calculate the area of polygons
    gdf = calculate_polygon_areas(gdf)

    # Example point to check
    point_coords = (-93.244, 38.871)  # Example coordinates (longitude, latitude)

    # Check if the point is within the first polygon
    is_within = check_point_within_polygon(gdf, point_coords)

    # Print results
    logging.info(f"Point is inside polygon: {is_within}")
    print(f"Point is inside polygon: {is_within}")
    print(gdf[['geometry', 'area']])

if __name__ == "__main__":
    main()
