import geopandas as gpd
import rasterio
from rasterio.mask import mask

# Load polygon shapefile (Area of Interest)
polygon_shapefile = 'data/aoi.shp'
aoi = gpd.read_file(polygon_shapefile)

# Load raster data
raster_file = 'data/raw_raster.tif'
with rasterio.open(raster_file) as src:
    # Mask raster using polygon
    geo_json = aoi.geometry.__geo_interface__
    out_image, out_transform = mask(src, geo_json, crop=True)
    
    # Save the clipped raster
    out_raster = 'data/processed/clip_raster_output.tif'
    with rasterio.open(out_raster, 'w', **src.meta) as dest:
        dest.write(out_image)
