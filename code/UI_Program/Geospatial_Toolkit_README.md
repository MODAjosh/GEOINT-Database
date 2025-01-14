# Geospatial Toolkit

The **Geospatial Toolkit** is a Python-based graphical user interface (GUI) application for performing a variety of geospatial analyses. The toolkit is built using `Tkinter` and allows users to run geospatial scripts such as buffer analysis, distance calculations, centroid calculations, and more.

## Features
- Perform geospatial analyses with ease using a user-friendly GUI.
- Supports scripts for:
  - Buffer Analysis
  - Calculate Centroid
  - Calculate Distance
  - Calculate Slope
  - Clip Raster/Shapefiles
  - NDVI Calculations
  - Spatial Joins
  - Data Preprocessing (e.g., Merging, Rasterization, Reprojection)
- Execution logs displayed in the GUI.
- Tooltips for guiding users through input fields.

## Prerequisites
Before using the toolkit, ensure the following:
- **Python 3.7+** is installed on your system.
- Required Python libraries are installed. Run the following command to install dependencies:
  ```bash
  pip install tkinter geopandas pyproj argparse
  ```

## Directory Structure
The directory is structured as follows:
```
GEOINT-Database/
├── code/
│   ├── analysis_tools/
│   │   ├── buffer_analysis.py
│   │   ├── calculate_centroid.py
│   │   ├── calculate_distance.py
│   │   └── ...
│   ├── data_preprocessing/
│   │   ├── clip_raster_by_polygon.py
│   │   ├── merge_data.py
│   │   └── ...
├── data/
│   ├── processed_data/   # Output files will be saved here
│   └── ...
└── README.md
```

## Usage
1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/<your-repo>/GEOINT-Database.git
   ```
2. Navigate to the directory containing the `Geospatial Toolkit` script.
3. Update the `BASE_DIR` variable in the script to point to the local path of the repository:
   ```python
   BASE_DIR = r"C:\Users\<YourUsername>\Documents\GitHub\GEOINT-Database"
   ```
4. Run the script:
   ```bash
   python geospatial_toolkit.py
   ```
5. The GUI will launch. Select a tool from the menu, provide the required inputs, and execute the script.

## Input Format
Each tool requires specific inputs, as described below:

### 1. Buffer Analysis
- **Input File**: A shapefile (`.shp`) containing geometries.
- **Buffer Distance**: Distance in meters for the buffer.
- **Output File**: Path to save the buffered output.

### 2. Calculate Centroid
- **Input File**: A shapefile (`.shp`) containing polygon geometries.
- **Output File**: Path to save the centroid output.

### 3. Calculate Distance
- **Input File**: A shapefile (`.shp`) containing point geometries.
- **Index of Point A**: The index of the first point (e.g., `0`).
- **Index of Point B**: The index of the second point (e.g., `1`).

...and more tools as specified in the script.

## Logs
Execution logs are displayed within the GUI for each tool. Logs include:
- Inputs provided.
- Commands executed.
- Script output (success/errors).

## Troubleshooting
- **Error: `Script file does not exist`**  
  Ensure the paths to the script files in the `SCRIPTS` dictionary are correct.
  
- **Error: Missing Dependencies**  
  Ensure all required Python libraries are installed using `pip`.

## Contributions
Contributions to improve the toolkit are welcome! Fork the repository, make your changes, and submit a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact
For any questions or support, reach out to `<Your Contact Email>`.

---
Happy Mapping!
