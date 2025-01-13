import tkinter as tk
from tkinter import messagebox, simpledialog, scrolledtext, Toplevel, Label, Entry, Button
import subprocess

# Define the script list with specific input fields
SCRIPTS = {
    # Analysis Tools
    "Buffer Analysis": {
        "script": "buffer_analysis.py",
        "inputs": [
            {"label": "Input File (Shapefile)", "placeholder": "e.g., input.shp", "type": "file"},
            {"label": "Buffer Distance (meters)", "placeholder": "e.g., 100", "type": "number"},
            {"label": "Output File", "placeholder": "e.g., output.shp", "type": "text"}
        ]
    },
    "Calculate Buffer Zone": {
        "script": "calculate_buffer_zone.py",
        "inputs": [
            {"label": "Input File (Shapefile)", "placeholder": "e.g., input.shp", "type": "file"},
            {"label": "Buffer Distance (meters)", "placeholder": "e.g., 100", "type": "number"},
            {"label": "Output File", "placeholder": "e.g., output_buffered.gpkg", "type": "text"}
        ]
    },
    "Calculate Distance": {
        "script": "calculate_distance.py",
        "inputs": [
            {"label": "Input File (Shapefile with Points)", "placeholder": "e.g., points.shp", "type": "file"},
            {"label": "Index of Point A", "placeholder": "e.g., 0", "type": "number"},
            {"label": "Index of Point B", "placeholder": "e.g., 1", "type": "number"}
        ]
    },
    "Calculate Centroid": {
        "script": "calculate_centroid.py",
        "inputs": [
            {"label": "Input File (Shapefile)", "placeholder": "e.g., input.shp", "type": "file"},
            {"label": "Output File", "placeholder": "e.g., output_centroid.gpkg", "type": "text"}
        ]
    },
    "Calculate Slope": {
        "script": "calculate_slope.py",
        "inputs": [
            {"label": "Input Raster File", "placeholder": "e.g., dem.tif", "type": "file"},
            {"label": "Output File", "placeholder": "e.g., slope.tif", "type": "text"},
            {"label": "Slope Format", "placeholder": "percent, degrees, or raw", "type": "text"}
        ]
    },
    "Clip Raster by Shapefile": {
        "script": "clip_raster_by_shapefile.py",
        "inputs": [
            {"label": "Input Raster File", "placeholder": "e.g., dem.tif", "type": "file"},
            {"label": "Shapefile for Clipping", "placeholder": "e.g., boundary.shp", "type": "file"},
            {"label": "Output File", "placeholder": "e.g., clipped_dem.tif", "type": "text"}
        ]
    },
    "Extract Statistics": {
        "script": "extract_statistics.py",
        "inputs": [
            {"label": "Input Raster File", "placeholder": "e.g., input.tif", "type": "file"},
            {"label": "Output File", "placeholder": "e.g., statistics.json", "type": "text"}
        ]
    },
    "NDVI Calculation": {
        "script": "ndvi_calculation.py",
        "inputs": [
            {"label": "Red Band File", "placeholder": "e.g., red_band.tif", "type": "file"},
            {"label": "NIR Band File", "placeholder": "e.g., nir_band.tif", "type": "file"},
            {"label": "Output NDVI File", "placeholder": "e.g., ndvi_output.tif", "type": "text"}
        ]
    },
    "Perform Geospatial Analysis": {
        "script": "perform_geospatial_analysis.py",
        "inputs": [
            {"label": "Input Shapefile", "placeholder": "e.g., polygons.shp", "type": "file"},
            {"label": "Point Coordinates", "placeholder": "e.g., -93.244,38.871", "type": "text"},
            {"label": "Output File", "placeholder": "e.g., analysis_results.shp", "type": "text"}
        ]
    },
    "Spatial Join": {
        "script": "spatial_join.py",
        "inputs": [
            {"label": "Points Shapefile", "placeholder": "e.g., points.shp", "type": "file"},
            {"label": "Polygons Shapefile", "placeholder": "e.g., polygons.shp", "type": "file"},
            {"label": "Output File", "placeholder": "e.g., spatial_join_results.shp", "type": "text"}
        ]
    },

    # Preprocessing Tools
  #None of the following tools have been touched
    "Buffer Vector Data": {
        "script": "buffer_vector_data.py",
        "inputs": [
            {"label": "Input Vector File", "placeholder": "e.g., input.shp", "type": "file"},
            {"label": "Buffer Distance", "placeholder": "e.g., 200", "type": "number"},
            {"label": "Output File", "placeholder": "e.g., buffered_output.shp", "type": "text"}
        ]
    },
    "Clip Raster by Polygon": {
        "script": "clip_raster_by_polygon.py",
        "inputs": [
            {"label": "Input Raster File", "placeholder": "e.g., input.tif", "type": "file"},
            {"label": "Polygon File", "placeholder": "e.g., polygon.shp", "type": "file"},
            {"label": "Output File", "placeholder": "e.g., clipped_raster.tif", "type": "text"}
        ]
    },
    "Clip Shapefile by Polygon": {
        "script": "clip_shapefile_by_polygon.py",
        "inputs": [
            {"label": "Input Shapefile", "placeholder": "e.g., input.shp", "type": "file"},
            {"label": "Clipping Polygon", "placeholder": "e.g., clip_polygon.shp", "type": "file"},
            {"label": "Output File", "placeholder": "e.g., clipped_shapefile.shp", "type": "text"}
        ]
    },
    "Merge Data": {
        "script": "merge_data.py",
        "inputs": [
            {"label": "Input File 1", "placeholder": "e.g., file1.shp", "type": "file"},
            {"label": "Input File 2", "placeholder": "e.g., file2.shp", "type": "file"},
            {"label": "Output File", "placeholder": "e.g., merged_output.shp", "type": "text"}
        ]
    },
    "Normalize Raster": {
        "script": "normalize_raster.py",
        "inputs": [
            {"label": "Input Raster File", "placeholder": "e.g., input.tif", "type": "file"},
            {"label": "Output File", "placeholder": "e.g., normalized.tif", "type": "text"}
        ]
    },
    "Rasterize Vector": {
        "script": "rasterize_vector.py",
        "inputs": [
            {"label": "Input Vector File", "placeholder": "e.g., input.shp", "type": "file"},
            {"label": "Output Raster File", "placeholder": "e.g., rasterized_output.tif", "type": "text"}
        ]
    },
    "Reformat to GeoTIFF": {
        "script": "reformat_to_geotiff.py",
        "inputs": [
            {"label": "Input File", "placeholder": "e.g., input.data", "type": "file"},
            {"label": "Output GeoTIFF File", "placeholder": "e.g., output.tif", "type": "text"}
        ]
    },
        "Remove Outliers": {
            "script": "remove_outliers.py",
            "inputs": [
                {"label": "Input Data File", "placeholder": "e.g., data.csv", "type": "file"},
                {"label": "Threshold Value", "placeholder": "e.g., 1.5", "type": "number"},
                {"label": "Output File", "placeholder": "e.g., cleaned_data.csv", "type": "text"}
            ]
        },
        "Reproject Raster": {
            "script": "reproject_raster.py",
            "inputs": [
                {"label": "Input Raster File", "placeholder": "e.g., input.tif", "type": "file"},
                {"label": "Target CRS", "placeholder": "e.g., EPSG:4326", "type": "text"},
                {"label": "Output File", "placeholder": "e.g., reprojected_output.tif", "type": "text"}
            ]
        },
        "Shapefile to GeoJSON": {
            "script": "shapefile_to_geojson.py",
            "inputs": [
                {"label": "Input Shapefile", "placeholder": "e.g., input.shp", "type": "file"},
                {"label": "Output GeoJSON File", "placeholder": "e.g., output.geojson", "type": "text"}
            ]
        }
    }
}

# Function to log messages
def log_message(message):
    log_window.configure(state="normal")
    log_window.insert(tk.END, message + "\n")
    log_window.configure(state="disabled")
    log_window.yview(tk.END)


# Function to run a script
def run_script(script_name):
    script_info = SCRIPTS.get(script_name)
    if not script_info:
        messagebox.showerror("Error", f"Script '{script_name}' not found.")
        return
    
    # Open a custom dialog for inputs
    open_input_dialog(script_name, script_info)


# Function to create a custom input dialog
def open_input_dialog(script_name, script_info):
    def submit_inputs():
        # Gather inputs from the dialog
        inputs = {field["label"]: entries[field["label"]].get() for field in script_info["inputs"]}
        if any(value.strip() == "" for value in inputs.values()):
            messagebox.showwarning("Warning", "All fields must be filled out.")
            return
        
        # Close the dialog and run the script
        dialog.destroy()
        run_script_with_inputs(script_info["script"], inputs)

    # Create a new top-level window for the input dialog
    dialog = Toplevel(root)
    dialog.title(f"Inputs for {script_name}")
    dialog.geometry("400x300")

    # Create input fields
    entries = {}
    for idx, field in enumerate(script_info["inputs"]):
        Label(dialog, text=field["label"]).grid(row=idx, column=0, pady=5, padx=5, sticky="e")
        entry = Entry(dialog, width=30)
        entry.insert(0, field["placeholder"])
        entry.grid(row=idx, column=1, pady=5, padx=5)
        entries[field["label"]] = entry

    # Add a submit button
    Button(dialog, text="Run Script", command=submit_inputs).grid(row=len(script_info["inputs"]), columnspan=2, pady=10)


# Function to execute the script with user inputs
def run_script_with_inputs(script_path, inputs):
    # Convert inputs to command-line arguments
    args = []
    for key, value in inputs.items():
        args.append(value)

    try:
        # Log the start of execution
        log_message(f"Running {script_path} with inputs: {inputs}")
        
        # Run the script with inputs
        command = ["python", script_path] + args
        result = subprocess.run(command, capture_output=True, text=True)
        
        # Log the output and errors
        if result.stdout:
            log_message(f"Output from {script_path}:\n{result.stdout}")
        if result.stderr:
            log_message(f"Errors from {script_path}:\n{result.stderr}")

        messagebox.showinfo("Execution Complete", f"Finished running {script_path}. Check the log for details.")
    except Exception as e:
        log_message(f"Error: Failed to run {script_path}. {str(e)}")
        messagebox.showerror("Error", f"Failed to run script '{script_path}'.\n\n{str(e)}")


# Initialize the Tkinter window
root = tk.Tk()
root.title("Geospatial Analysis Toolkit")
root.geometry("600x800")

# Add a header
header = tk.Label(root, text="Geospatial Analysis Toolkit", font=("Helvetica", 16))
header.pack(pady=10)

# Add a frame for buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

# Add buttons for each script
for script_name in SCRIPTS.keys():
    btn = tk.Button(button_frame, text=script_name, command=lambda s=script_name: run_script(s), width=40)
    btn.pack(pady=5)

# Add a logging section
log_label = tk.Label(root, text="Execution Log", font=("Helvetica", 14))
log_label.pack(pady=5)

log_window = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=70, height=20, state="disabled", bg="black", fg="white")
log_window.pack(pady=10)

# Add a quit button
quit_button = tk.Button(root, text="Quit", command=root.quit, width=40, bg="red", fg="white")
quit_button.pack(pady=10)

# Run the Tkinter main loop
root.mainloop()
