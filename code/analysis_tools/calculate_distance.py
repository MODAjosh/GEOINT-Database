import geopandas as gpd
from geopy.distance import geodesic

# Load point data (example: two coordinates)
gdf = gpd.read_file('processed_data/points.shp')

# Example: Calculate the distance between the first and second points in the dataset
point1 = gdf.geometry.iloc[0].coords[0]
point2 = gdf.geometry.iloc[1].coords[0]

# Calculate the distance between the two points
distance = geodesic(point1, point2).meters

print(f"Distance between points: {distance} meters")
