# Geospatial Toolkit

## Overview
The Geospatial Toolkit is a Python-based graphical user interface (GUI) designed to streamline the execution of various geospatial processing tasks. The toolkit is implemented using Tkinter and provides a convenient interface for running geospatial scripts such as buffer analysis, NDVI calculation, and raster clipping.

## Features
- **Dynamic Script Integration**: Load and execute various geospatial scripts dynamically.
- **Custom Input Dialogs**: Each script prompts for the necessary input parameters using an intuitive form.
- **Log Window**: Real-time logging of script execution, including outputs and errors.
- **Tooltip Support**: Provides detailed tooltips for user inputs and buttons.

## Requirements
- Python 3.7+
- Required Python libraries:
  - `tkinter`
  - `os`
  - `subprocess`

## Installation
1. Clone the repository containing the toolkit and associated scripts.
   ```bash
   git clone https://github.com/your-repo/geospatial-toolkit.git
   ```

2. Install the required dependencies (if not already available):
   ```bash
   pip install tk
   ```

3. Place all geospatial processing scripts in their respective directories under the `code/analysis_tools` or `code/data_preprocessing` folders.

## Usage
1. Run the main script:
   ```bash
   python geospatial_toolkit.py
   ```

2. The GUI will display a list of available tools. Click on a tool to open its input dialog.

3. Provide the required inputs, such as file paths and parameters, and click **Run Script**.

4. Monitor the log window for real-time updates on the script's execution.

## Directory Structure
```
Geospatial-Toolkit/
├── code/
│   ├── analysis_tools/
│   │   ├── buffer_analysis.py
│   │   ├── ndvi_calculation.py
│   │   ├── ...
│   ├── data_preprocessing/
│   │   ├── clip_raster_by_polygon.py
│   │   ├── reproject_raster.py
│   │   ├── ...
├── geospatial_toolkit.py
├── README.md
```

## Customization
### Adding New Scripts
1. Place your new script in the appropriate folder (e.g., `code/analysis_tools`).
2. Update the `SCRIPTS` dictionary in the `geospatial_toolkit.py` file:
   ```python
   SCRIPTS["Your Script Name"] = {
       "script": os.path.join(BASE_DIR, "code", "analysis_tools", "your_script.py"),
       "inputs": [
           {"label": "Input File", "placeholder": "input.shp", "type": "file", "tooltip": "Select the input shapefile."},
           {"label": "Parameter", "placeholder": "value", "type": "number", "tooltip": "Provide the parameter value."}
       ]
   }
   ```

3. Restart the toolkit to reflect the changes.

## Troubleshooting
### Script File Not Found
- Ensure the `BASE_DIR` variable in the script correctly points to the directory containing the `code` folder.
- Confirm the script file exists in the specified folder.

### Missing Dependencies
- Verify that all required Python libraries are installed using `pip install`.

### Input Validation Errors
- Check that all required fields are filled in correctly.
- Ensure that file paths are valid and accessible.

## Contributing
Contributions are welcome! Feel free to submit issues or pull requests to enhance the toolkit.

## License
This project is licensed under the MIT License.

