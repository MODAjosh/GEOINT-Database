import geopandas as gpd

# Load shapefile to clip
shapefile_to_clip = 'data/raw_shapefile.shp'
gdf_to_clip = gpd.read_file(shapefile_to_clip)

# Load clipping polygon (e.g., shapefile with area of interest)
clip_polygon_file = 'data/aoi.shp'
clip_polygon = gpd.read_file(clip_polygon_file)

# Clip the shapefile using the polygon
clipped_gdf = gdf_to_clip[gdf_to_clip.geometry.intersects(clip_polygon.geometry.iloc[0])]

# Save the clipped shapefile
clipped_gdf.to_file('data/processed/clipped_shapefile.shp')
