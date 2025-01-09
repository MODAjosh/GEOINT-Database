import geopandas as gpd
from shapely.geometry import Point
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def validate_geometries(gdf, geom_types):
    """
    Validate that the geometries in a GeoDataFrame match the specified types.

    Parameters:
        gdf (GeoDataFrame): The GeoDataFrame to validate.
        geom_types (list): A list of acceptable geometry types (e.g., ['Polygon', 'MultiPolygon']).

    Returns:
        bool: True if all geometries are valid, False otherwise.
    """
    if not gdf.geometry.type.isin(geom_types).all():
        raise ValueError(f"GeoDataFrame contains invalid geometries. Expected types: {geom_types}")

def calculate_polygon_areas(gdf):
    """
    Calculate the area of polygons in a GeoDataFrame.

    Parameters:
        gdf (GeoDataFrame): The GeoDataFrame containing polygon geometries.

    Returns:
        GeoDataFrame: The updated GeoDataFrame with a new 'area' column.
    """
    try:
        # Validate geometries
        validate_geometries(gdf, ['Polygon', 'MultiPolygon'])

        # Calculate area for polygons
        logging.info("Calculating areas for polygons.")
        gdf['area'] = gdf.geometry.area
        logging.info("Area calculation completed successfully.")
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

        is_within = polygon.contains(point)
        logging.info(f"Point containment check completed. Result: {is_within}")
        return is_within
    except IndexError:
        logging.error("GeoDataFrame is empty. Cannot check point containment.")
        return False
    except Exception as e:
        logging.error(f"An error occurred while checking point containment: {e}")
        return False

def main():
    # Load the shapefile or GeoJSON
    input_file = 'processed_data/merged_shapefile.shp'
    logging.info(f"Loading file: {input_file}")
    try:
        gdf = gpd.read_file(input_file)

        # Ensure GeoDataFrame is not empty
        if gdf.empty:
            logging.error("The input GeoDataFrame is empty.")
            return

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
    except FileNotFoundError:
        logging.error(f"File not found: {input_file}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
