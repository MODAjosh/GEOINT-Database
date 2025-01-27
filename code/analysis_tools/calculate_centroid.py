import os
import geopandas as gpd
from pathlib import Path
from pyproj import CRS
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def ensure_projected_crs(gdf):
    """
    Ensures the GeoDataFrame has a projected CRS. Raises an error if CRS is not defined.

    Parameters:
        gdf (GeoDataFrame): Input GeoDataFrame.

    Returns:
        GeoDataFrame: GeoDataFrame with a projected CRS.
    """
    if gdf.crs is None:
        raise ValueError("The GeoDataFrame does not have a defined CRS.")

    crs = CRS.from_user_input(gdf.crs)
    if not crs.is_projected:
        logging.warning("CRS is not projected. Reprojecting to EPSG:3857 (Web Mercator).")
        gdf = gdf.to_crs(epsg=3857)
    return gdf


def calculate_centroids(gdf):
    """
    Calculates centroids of polygon geometries in a GeoDataFrame.

    Parameters:
        gdf (GeoDataFrame): Input GeoDataFrame with polygons.

    Returns:
        GeoDataFrame: A new GeoDataFrame with centroids.
    """
    if not gdf.geometry.is_valid.all():
        raise ValueError("Invalid geometries detected. Please validate or fix the geometries before proceeding.")

    if not gdf.geometry.type.isin(["Polygon", "MultiPolygon"]).all():
        raise ValueError("Input GeoDataFrame must contain only Polygon or MultiPolygon geometries.")

    logging.info("Calculating centroids for the polygons.")
    centroids = gdf.geometry.centroid

    centroids_gdf = gpd.GeoDataFrame(gdf.drop(columns='geometry'), geometry=centroids, crs=gdf.crs)
    return centroids_gdf


def process_centroids(input_file, output_file):
    """
    Loads a shapefile, calculates centroids, and saves the result.

    Parameters:
        input_file (str): Path to the input shapefile.
        output_file (str): Path to save the output file with centroids.
    """
    try:
        logging.info(f"Loading input file: {input_file}")
        gdf = gpd.read_file(input_file)

        gdf = ensure_projected_crs(gdf)
        centroids_gdf = calculate_centroids(gdf)

        logging.info(f"Saving centroids to: {output_file}")
        centroids_gdf.to_file(output_file, driver="GPKG")

        logging.info(f"Centroids successfully calculated and saved to {output_file}.")
    except FileNotFoundError:
        logging.error(f"Input file not found: {input_file}")
        raise
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}", exc_info=True)
        raise


def run_from_gui(input_file, output_file):
    """
    Interface for running the centroid process from a GUI.

    Parameters:
        input_file (str): Path to the input shapefile.
        output_file (str): Path to save the output file with centroids.
    """
    try:
        process_centroids(input_file, output_file)
        logging.info("Process completed successfully through GUI.")
    except Exception as e:
        logging.error(f"Error while running from GUI: {e}")


def main():
    """
    Main function to execute centroid calculation via command line.
    """
    import argparse

    parser = argparse.ArgumentParser(description="Calculate centroids for a shapefile.")
    parser.add_argument('--input', required=True, help="Path to the input shapefile")
    parser.add_argument('--output', required=True, help="Path to save the output file with centroids")
    args = parser.parse_args()

    try:
        process_centroids(args.input, args.output)
    except Exception as e:
        logging.error(f"Error while running from command line: {e}")


if __name__ == "__main__":
    main()
