import geopandas as gpd

# Load multiple shapefiles or GeoJSONs to merge
shapefile1 = 'shapefiles/your_shapefile1.shp'
shapefile2 = 'shapefiles/your_shapefile2.shp'

gdf1 = gpd.read_file(shapefile1)
gdf2 = gpd.read_file(shapefile2)

# Merge the two GeoDataFrames
merged_gdf = gdf1.append(gdf2, ignore_index=True)

# Save the merged GeoDataFrame
merged_gdf.to_file('processed_data/merged_shapefile.shp')

print("Data has been merged and saved to processed_data/merged_shapefile.shp.")

