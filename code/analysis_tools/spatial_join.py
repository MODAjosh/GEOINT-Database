import geopandas as gpd
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def validate_geodataframes(gdf_points, gdf_polygons):
    """
    Validate the GeoDataFrames for spatial join operations.

    Parameters:
        gdf_points (GeoDataFrame): GeoDataFrame containing point geometries.
        gdf_polygons (GeoDataFrame): GeoDataFrame containing polygon geometries.

    Raises:
        ValueError: If any GeoDataFrame is empty or contains invalid geometries.
    """
    if gdf_points.empty:
        raise ValueError("The points GeoDataFrame is empty.")
    if gdf_polygons.empty:
        raise ValueError("The polygons GeoDataFrame is empty.")

    if not gdf_points.geometry.type.isin(['Point']).all():
        raise ValueError("The points GeoDataFrame must contain only Point geometries.")
    if not gdf_polygons.geometry.type.isin(['Polygon', 'MultiPolygon']).all():
        raise ValueError("The polygons GeoDataFrame must contain only Polygon or MultiPolygon geometries.")

def align_crs(gdf_points, gdf_polygons):
    """
    Align the CRS of the points GeoDataFrame with the polygons GeoDataFrame.

    Parameters:
        gdf_points (GeoDataFrame): GeoDataFrame containing point geometries.
        gdf_polygons (GeoDataFrame): GeoDataFrame containing polygon geometries.

    Returns:
        GeoDataFrame: GeoDataFrame with aligned CRS for points.
    """
    if gdf_points.crs != gdf_polygons.crs:
        logging.info("CRS mismatch detected. Aligning CRS of points to polygons.")
        return gdf_points.to_crs(gdf_polygons.crs)
    return gdf_points

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

        # Validate the GeoDataFrames
        validate_geodataframes(gdf_points, gdf_polygons)

        # Align CRS
        gdf_points = align_crs(gdf_points, gdf_polygons)

        # Perform spatial join (find points within polygons)
        logging.info("Performing spatial join to find points within polygons.")
        joined_gdf = gpd.sjoin(gdf_points, gdf_polygons, how='inner', predicate='within')

        # Save the results to a shapefile
        logging.info(f"Saving results to: {output_file}")
        joined_gdf.to_file(output_file)

        logging.info("Spatial join completed and results saved successfully.")

    except FileNotFoundError as e:
        logging.error(f"File not found: {e}")
    except ValueError as e:
        logging.error(f"Validation error: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred during the spatial join process: {e}")

def main():
    # Define file paths
    points_file = 'processed_data/points.shp'
    polygons_file = 'processed_data/polygons.shp'
    output_file = 'processed_data/spatial_joined_results.shp'

    # Perform spatial join
    perform_spatial_join(points_file, polygons_file, output_file)

if __name__ == "__main__":
    main()
