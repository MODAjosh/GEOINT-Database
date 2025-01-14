import geopandas as gpd
from geopy.distance import geodesic
import logging
import argparse

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def ensure_geographic_crs(gdf):
    """
    Ensures the GeoDataFrame has a geographic CRS.

    Parameters:
        gdf (GeoDataFrame): Input GeoDataFrame.

    Returns:
        GeoDataFrame: GeoDataFrame with a geographic CRS.
    """
    if gdf.crs is None:
        raise ValueError("The GeoDataFrame does not have a defined CRS.")

    if not gdf.crs.is_geographic:
        raise ValueError("The GeoDataFrame CRS is not geographic. Expected a CRS with latitude and longitude (e.g., EPSG:4326).")

    return gdf


def calculate_distance_between_points(gdf, index1=0, index2=1):
    """
    Calculate the geodesic distance between two points in a GeoDataFrame.

    Parameters:
        gdf (GeoDataFrame): GeoDataFrame containing point geometries.
        index1 (int): Index of the first point.
        index2 (int): Index of the second point.

    Returns:
        float: Distance between the two points in meters.
    """
    # Ensure the GeoDataFrame contains point geometries
    if not gdf.geometry.type.isin(["Point"]).all():
        raise ValueError("The GeoDataFrame must contain only point geometries.")

    # Ensure CRS is geographic
    ensure_geographic_crs(gdf)

    # Validate indices
    if index1 >= len(gdf) or index2 >= len(gdf):
        raise IndexError("Indices are out of bounds for the GeoDataFrame.")

    # Extract coordinates of the two points
    point1 = gdf.geometry.iloc[index1].coords[0]
    point2 = gdf.geometry.iloc[index2].coords[0]

    # Log the coordinates being processed
    logging.info(f"Point 1 coordinates: {point1}")
    logging.info(f"Point 2 coordinates: {point2}")

    # Calculate geodesic distance
    logging.info(f"Calculating geodesic distance between points at index {index1} and {index2}.")
    distance = geodesic(point1, point2).meters

    logging.info(f"Distance between points: {distance:.2f} meters")
    return distance


def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Calculate the distance between two points in a shapefile.")
    parser.add_argument("--input", required=True, help="Path to the input shapefile")
    parser.add_argument("--index1", required=True, type=int, help="Index of the first point")
    parser.add_argument("--index2", required=True, type=int, help="Index of the second point")
    args = parser.parse_args()

    try:
        # Load the GeoDataFrame
        logging.info(f"Loading input file: {args.input}")
        gdf = gpd.read_file(args.input)

        # Calculate the distance between the two points
        distance = calculate_distance_between_points(gdf, args.index1, args.index2)

        if distance is not None:
            print(f"Distance between the points: {distance:.2f} meters")
    except FileNotFoundError:
        logging.error(f"Input file not found: {args.input}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
