import geopandas as gpd
from shapely.geometry import Point, Polygon

# Load a shapefile or GeoJSON
gdf = gpd.read_file('processed_data/merged_shapefile.shp')

# Example: Calculating the area of polygons (if the shapefile contains polygons)
gdf['area'] = gdf.geometry.area

# Example: Check if a point is inside a polygon
point = Point(-93.244, 38.871)  # Example coordinates (longitude, latitude)

# Assuming the first geometry in the GeoDataFrame is a polygon
polygon = gdf.geometry.iloc[0]
is_within = polygon.contains(point)

# Print results
print(f"Point is inside polygon: {is_within}")
print(gdf[['geometry', 'area']])
