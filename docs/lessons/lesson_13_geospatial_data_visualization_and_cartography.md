# Lesson 13: Geospatial Data Visualization and Cartography

## Overview

Effective visualization of geospatial data is crucial for communicating insights and making informed decisions. Maps are a powerful tool for visualizing spatial patterns and relationships, and understanding how to design and present maps in a clear, engaging way is a key skill for geospatial professionals.

In this lesson, we will explore key techniques and tools for visualizing geospatial data. Topics include cartographic principles, symbology, creating thematic maps, and using advanced visualization techniques like 3D maps and interactive visualizations. We will also discuss best practices for map design to ensure that your maps effectively communicate your analysis.

In this lesson, we will cover:
- Cartographic principles for effective map design
- Symbolization and classification of data
- Creating thematic maps in QGIS
- Visualizing 3D data and interactive maps
- Tools for geospatial data visualization in Python and QGIS

---

## 1. Cartographic Principles for Effective Map Design

Good map design is essential for communicating geospatial data effectively. Cartographic principles ensure that maps are clear, easy to interpret, and aesthetically pleasing. Key principles include:

### Key Concepts:
- **Clarity**: Maps should be simple and easy to understand. Avoid clutter by limiting the number of layers and symbols.
- **Scale**: The scale of a map should be chosen based on the data and the purpose of the map. Ensure that the map's scale is appropriate for the level of detail you want to show.
- **Legend and Symbology**: A clear legend and appropriate symbology are essential for helping viewers understand the map’s features and what the data represents.
- **Color Theory**: Use color to convey information effectively. For example, use color gradients for continuous data and discrete color categories for classified data.

#### Hands-On Example: Creating a Simple Map in QGIS
1. Open QGIS and load a shapefile (e.g., population density data).
2. Apply appropriate symbology using color ramps to represent population density.
3. Add a legend and title, ensuring the map is clear and informative.
4. Export the map as an image or PDF for sharing.

**Resource**: [QGIS Map Design Principles](https://docs.qgis.org/latest/en/docs/user_manual/)

---

## 2. Symbolization and Classification of Data

Symbolization is the process of visually representing spatial data with different symbols, colors, and patterns. The choice of symbology depends on the type of data you are visualizing and the purpose of your map.

### Types of Data and Symbolization:
- **Point Data**: For representing discrete features such as buildings or trees, use symbols like dots, icons, or markers.
- **Line Data**: For roads, rivers, or other linear features, use line styles such as dashed, solid, or thick lines.
- **Polygon Data**: For areas like parks or administrative boundaries, use fill colors, patterns, or outlines.

### Classification Methods:
- **Quantitative Classification**: For continuous data, such as elevation or temperature, use color ramps or graduated symbols to represent data ranges.
- **Qualitative Classification**: For categorical data, such as land use or administrative regions, use distinct colors or patterns for each category.

#### Hands-On Example: Classifying and Symbolizing Data in QGIS
1. Load a shapefile of land-use data into QGIS.
2. Apply a qualitative color scheme to represent different land-use types (e.g., residential, commercial, industrial).
3. Adjust the symbology to ensure that the map is visually distinct and easy to understand.

**Resource**: [Symbology in QGIS](https://docs.qgis.org/latest/en/docs/user_manual/working_with_vector/symbology.html)

---

## 3. Creating Thematic Maps in QGIS

Thematic maps focus on a specific theme or dataset, such as population density, income levels, or land use. These maps are used to convey specific insights and can help identify trends, patterns, and relationships in the data.

### Key Techniques:
- **Choropleth Maps**: A type of thematic map where areas are shaded based on the value of a specific variable (e.g., population density).
- **Proportional Symbol Maps**: Uses symbols (e.g., circles) whose size varies according to a data value (e.g., crime rate or business locations).
- **Dot Density Maps**: Represents data with dots, where each dot corresponds to a certain number of units (e.g., population).

#### Hands-On Example: Creating a Choropleth Map in QGIS
1. Load a dataset containing numerical data (e.g., income levels by county).
2. Style the polygons (e.g., counties) with a color ramp to represent different income levels.
3. Add a legend to explain the color scheme and export the map for presentation.

**Resource**: [Creating Thematic Maps in QGIS](https://docs.qgis.org/latest/en/docs/user_manual/working_with_vector/thematic_maps.html)

---

## 4. Visualizing 3D Data

3D visualization is a powerful way to represent geospatial data, especially when working with elevation or terrain data. In QGIS, 3D visualization can be used to create realistic representations of terrain, buildings, or other features.

### Techniques:
- **3D Terrain Visualization**: Use Digital Elevation Models (DEMs) to create 3D terrain models. The elevation data is visualized in 3D to show mountains, valleys, and other terrain features.
- **3D City Models**: Create 3D models of cities and urban areas using 3D building data (e.g., from LiDAR or photogrammetry).

#### Hands-On Example: Creating 3D Terrain Visualization in QGIS
1. Load a DEM dataset into QGIS.
2. Enable the 3D map view in QGIS to visualize the terrain in three dimensions.
3. Adjust the lighting and shading to create realistic 3D terrain effects.

**Resource**: [QGIS 3D Visualization](https://docs.qgis.org/latest/en/docs/user_manual/3d.html)

---

## 5. Interactive Maps

Interactive maps allow users to engage with geospatial data dynamically. They can zoom, pan, and click on features to retrieve information, making them ideal for web-based applications and dashboards.

### Tools for Interactive Maps:
- **QGIS Web Map Export**: QGIS allows you to export maps to interactive web maps using plugins like **QGIS2Web** or **Leaflet**.
- **Python (Folium)**: A Python library used to create interactive maps for use in web applications and notebooks.
- **ArcGIS Online**: A web-based platform for creating interactive maps and sharing geospatial data.

#### Hands-On Example: Creating an Interactive Map with QGIS2Web
1. Load your geospatial data into QGIS.
2. Use the **QGIS2Web** plugin to export your map to an interactive web format.
3. Open the map in a web browser and interact with it (e.g., click on features to see more information).

**Resource**: [QGIS2Web Plugin](https://plugins.qgis.org/plugins/qgis2web/)

---

## 6. Geospatial Data Visualization in Python

Python offers powerful libraries for geospatial data visualization. Two common libraries for this purpose are **Folium** and **Matplotlib**.

- **Folium**: A Python library that makes it easy to create interactive maps, particularly useful for creating maps with Leaflet.
- **Matplotlib**: A versatile plotting library that can be used to create static maps, charts, and other visualizations.

#### Hands-On Example: Creating an Interactive Map with Folium
1. Install the Folium library in Python: `pip install folium`.
2. Create a map centered on a specific location (e.g., a city or park).
3. Add markers, popups, and other elements to the map.

```python
import folium

# Create a map centered on a location
m = folium.Map(location=[40.7128, -74.0060], zoom_start=12)

# Add a marker
folium.Marker([40.7128, -74.0060], popup="New York City").add_to(m)

# Save map as HTML file
m.save("nyc_map.html")
