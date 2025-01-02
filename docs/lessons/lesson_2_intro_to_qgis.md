# Lesson 2: Introduction to QGIS

## What is QGIS?

**QGIS** (Quantum Geographic Information System) is a free and open-source Geographic Information System (GIS) that enables users to view, edit, and analyze geospatial data. It is one of the most popular GIS tools used in both professional and academic settings, due to its versatility and the fact that it supports numerous file formats and geospatial data types, including vector and raster data.

QGIS is used for mapping, spatial analysis, data management, and visualization, making it a powerful tool for Geospatial Intelligence (GEOINT) professionals.

## Key Features of QGIS:
1. **Layer Management**: QGIS supports working with various types of data, such as vector (points, lines, polygons) and raster (images, satellite data).
2. **Spatial Analysis**: QGIS provides a range of tools for spatial analysis, including buffering, overlay analysis, and proximity analysis.
3. **Georeferencing**: You can align raster data with real-world coordinates using QGIS's georeferencing tools.
4. **Map Styling and Cartography**: QGIS provides advanced cartographic features, enabling the creation of professional maps for presentations or publications.
5. **Plugin Support**: QGIS has a robust plugin system, allowing users to extend its functionality with custom tools and features.

### Applications of QGIS:
- **Mapping**: Create detailed, custom maps for various purposes (urban planning, resource management, disaster response, etc.).
- **Geospatial Analysis**: Perform spatial queries, proximity analysis, and analyze trends in geographic data.
- **Data Management**: Store and manage large datasets, both vector and raster, for use in decision-making processes.

## Getting Started with QGIS:
In this lesson, we will focus on how to get started with QGIS, exploring its interface, basic tools, and simple functions to load, visualize, and manipulate geospatial data.

### 1. **Installing QGIS**
To begin, you need to install QGIS on your system. Follow these steps:

- Visit the [QGIS Download Page](https://qgis.org/en/site/).
- Download the latest version of QGIS for your operating system (Windows, macOS, Linux).
- Follow the installation instructions based on your OS.

Once QGIS is installed, open the application and get ready to explore its interface.

### 2. **Understanding the QGIS Interface**
Upon opening QGIS, you'll be greeted by the main interface, which consists of the following parts:

- **Menu Bar**: Contains drop-down menus for various functions like file management, project settings, and map creation.
- **Toolbars**: Contain commonly used tools for zooming, selecting, editing, and analyzing data.
- **Layers Panel**: Displays the different layers (data) currently loaded in the project. Layers are the building blocks of your map.
- **Map Canvas**: The central area where your map is displayed.
- **Status Bar**: Displays information about the current project, such as the coordinate system, scale, and position of the map.

### 3. **Loading Data into QGIS**
To begin working with geospatial data in QGIS, you first need to load a dataset. QGIS supports multiple formats, including shapefiles (.shp), GeoJSON (.geojson), and raster data formats (such as .tiff).

Steps to load a dataset:
1. **Add Vector Data**: 
   - Click on the **"Add Vector Layer"** button in the toolbar (or use **Layer → Add Layer → Add Vector Layer**).
   - Browse to a folder containing your data (e.g., a shapefile or GeoJSON file).
   - Select the file and click **Open**.
   
2. **Add Raster Data**: 
   - Click on the **"Add Raster Layer"** button in the toolbar (or use **Layer → Add Layer → Add Raster Layer**).
   - Browse and select a raster file (e.g., GeoTIFF or satellite imagery).
   
Once the data is loaded, it will appear in the Layers Panel and on the Map Canvas.

### 4. **Basic Data Visualization**
After loading your data, you can manipulate how it appears on the map. QGIS provides several tools to style and customize your data:

- **Changing Layer Style**: Right-click on a layer in the Layers Panel, select **Properties**, and then go to the **Symbology** tab to change the color, size, and other visual properties of the layer.
- **Zoom and Pan**: Use the zoom tools in the toolbar to zoom in/out and the hand tool to pan across the map.

### 5. **Basic Geospatial Analysis in QGIS**
QGIS provides many built-in tools for spatial analysis. Here are a few common tools:

- **Buffer Tool**: Create a buffer zone around features (points, lines, or polygons) to analyze proximity.
  - Go to **Vector → Geoprocessing Tools → Buffer**.
  - Select the layer you want to buffer and specify the buffer distance.
  
- **Overlay Tool**: Combine two vector layers to analyze their relationships.
  - Go to **Vector → Geoprocessing Tools → Intersection** or **Union** to combine layers.
  
- **Clip Tool**: Clip one layer using another to isolate a specific region.
  - Go to **Vector → Geoprocessing Tools → Clip**.

### 6. **Saving and Exporting Data**
Once you have completed your work, you can save the project and export the data.

- **Saving a Project**: Go to **File → Save As** and give your project a name. This will save the entire QGIS project, including the layout and loaded layers.
  
- **Exporting Data**: Right-click on a layer in the Layers Panel, select **Export → Save Features As** to export the data in different formats (e.g., shapefile, GeoJSON).

## Activities for this Lesson:
1. **Install QGIS** and open the application.
2. **Load a sample vector dataset** (e.g., urban area boundaries or city locations) into QGIS.
3. **Style the vector layer** by changing the color and size of the points or polygons.
4. **Zoom and pan** to explore the map in detail.
5. **Use the Buffer tool** to create a buffer around a selected feature, such as a city or building.
6. **Export the layer** to a new file format (e.g., shapefile or GeoJSON).

## Additional Resources:
- [QGIS Tutorials](https://www.qgistutorials.com/en/)
- [QGIS Documentation](https://docs.qgis.org/)
- [QGIS User Manual](https://docs.qgis.org/latest/en/docs/user_manual/)
- [GeoPandas Documentation](https://geopandas.org/)
- [QGIS Training Resources](https://www.qgis.org/en/site/forusers/trainingmaterial.html)

## Conclusion:
In this lesson, you were introduced to **QGIS**, a powerful and open-source GIS tool. You learned how to install QGIS, navigate its interface, and load and style geospatial data. You also gained a basic understanding of how to perform simple geospatial analysis using QGIS tools.

In the next lesson, we will cover **Advanced Spatial Analysis in QGIS**, where we will dive deeper into more complex analysis techniques such as raster operations and geospatial queries.

