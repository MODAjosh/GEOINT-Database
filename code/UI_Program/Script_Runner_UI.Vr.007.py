import tkinter as tk
from tkinter import messagebox, filedialog, scrolledtext, Toplevel, Label, Entry, Button
import subprocess
import os

# Tooltip class for Tkinter
class ToolTip:
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tooltip = None
        self.widget.bind("<Enter>", self.show_tooltip)
        self.widget.bind("<Leave>", self.hide_tooltip)

    def show_tooltip(self, event):
        x = self.widget.winfo_rootx() + 10
        y = self.widget.winfo_rooty() + 10
        self.tooltip = Toplevel(self.widget)
        self.tooltip.wm_overrideredirect(True)
        self.tooltip.geometry(f"+{x}+{y}")
        label = Label(self.tooltip, text=self.text, background="lightyellow", relief="solid", padx=5, pady=5)
        label.pack()

    def hide_tooltip(self, event):
        if self.tooltip:
            self.tooltip.destroy()

# Function to log messages in a ScrolledText widget
def log_message(log_widget, message):
    log_widget.configure(state="normal")
    log_widget.insert(tk.END, message + "\n")
    log_widget.configure(state="disabled")
    log_widget.yview(tk.END)

# Function to validate inputs
def validate_inputs(inputs, input_types):
    for key, value in inputs.items():
        if not value.strip():
            messagebox.showwarning("Validation Error", f"The field '{key}' cannot be empty.")
            return False
        if input_types[key] == "number" and not value.isdigit():
            messagebox.showwarning("Validation Error", f"The field '{key}' must be a number.")
            return False
        if input_types[key] == "file" and not os.path.exists(value):
            messagebox.showwarning("Validation Error", f"The file '{value}' does not exist.")
            return False
    return True

# Function to run a script
def run_script(script_name, script_info):
    open_input_dialog(script_name, script_info)

# Function to create a custom input dialog
def open_input_dialog(script_name, script_info):
    def submit_inputs():
        inputs = {field["label"]: entries[field["label"]].get() for field in script_info["inputs"]}
        if not validate_inputs(inputs, input_types):
            return

        log_message(log_window, f"Inputs for {script_name}: {inputs}")
        run_script_with_inputs(script_info["script"], inputs, log_window)

    dialog = Toplevel(root)
    dialog.title(f"Inputs for {script_name}")
    dialog.geometry("590x400")  # Dialog size is set here
    dialog.resizable(True, True)

    entries = {}
    input_types = {}
    for idx, field in enumerate(script_info["inputs"]):
        Label(dialog, text=field["label"]).grid(row=idx, column=0, pady=5, padx=5, sticky="e")
        entry = Entry(dialog, width=30)
        entry.insert(0, field.get("placeholder", ""))
        entry.grid(row=idx, column=1, pady=5, padx=5)
        entries[field["label"]] = entry
        input_types[field["label"]] = field["type"]

        if field["type"] == "file":
            browse_button = Button(dialog, text="Browse", command=lambda e=entry: browse_file(e))
            browse_button.grid(row=idx, column=2, padx=5, pady=5)

        ToolTip(entry, field.get("tooltip", ""))

    log_label = Label(dialog, text="Execution Log", font=("Helvetica", 10, "bold"))
    log_label.grid(row=len(script_info["inputs"]), column=0, columnspan=3, pady=10)

    log_window = scrolledtext.ScrolledText(dialog, wrap=tk.WORD, width=70, height=10, state="disabled", bg="black", fg="white")
    log_window.grid(row=len(script_info["inputs"]) + 1, column=0, columnspan=3, pady=5)

    Button(dialog, text="Run Script", command=submit_inputs).grid(row=len(script_info["inputs"]) + 2, columnspan=3, pady=10)

# Function to execute the script with user inputs
def run_script_with_inputs(script_path, inputs, log_widget):
    if not os.path.exists(script_path):
        messagebox.showerror("Error", f"The script file '{script_path}' does not exist.")
        return

    args = [value for key, value in inputs.items()]

    try:
        log_message(log_widget, f"Running {script_path} with inputs: {inputs}")
        command = ["python", script_path] + args
        result = subprocess.run(command, capture_output=True, text=True)

        if result.stdout:
            log_message(log_widget, f"Output:\n{result.stdout}")
        if result.stderr:
            log_message(log_widget, f"Errors:\n{result.stderr}")

        messagebox.showinfo("Execution Complete", f"Finished running {script_path}. Check the log for details.")
    except Exception as e:
        log_message(log_widget, f"Error: {str(e)}")
        messagebox.showerror("Error", f"Failed to run script.\n\n{str(e)}")

# Function to open a file dialog for file selection
def browse_file(entry):
    file_path = filedialog.askopenfilename(title="Select a File", filetypes=[("All Files", "*.*")])
    if file_path:
        entry.delete(0, tk.END)
        entry.insert(0, file_path)

# Define scripts
SCRIPTS = {
    "Buffer Analysis": {
        "script": "buffer_analysis.py",
        "inputs": [
            {"label": "Input File", "placeholder": "input.shp", "type": "file", "tooltip": "Select the input shapefile."},
            {"label": "Buffer Distance", "placeholder": "100", "type": "number", "tooltip": "Enter buffer distance."},
            {"label": "Output File", "placeholder": "output.shp", "type": "text", "tooltip": "Specify the output file."}
        ]
    },
    "Calculate Centroid": {
        "script": "calculate_centroid.py",
        "inputs": [
            {"label": "Input File", "placeholder": "input.shp", "type": "file", "tooltip": "Select the input shapefile."},
            {"label": "Output File", "placeholder": "output_centroid.shp", "type": "text", "tooltip": "Specify the output file."}
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

# Initialize Tkinter
root = tk.Tk()
root.title("Geospatial Toolkit")
root.geometry("200x750")

header = tk.Label(root, text="Geospatial Toolkit", font=("Helvetica", 16), anchor="center")
header.pack(pady=10)

canvas = tk.Canvas(root)
scroll_y = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
scrollable_frame = tk.Frame(canvas)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.update_idletasks()
canvas.configure(scrollregion=canvas.bbox("all"), yscrollcommand=scroll_y.set)

canvas.pack(side="left", fill="both", expand=True)
scroll_y.pack(side="right", fill="y")

for script_name, script_info in SCRIPTS.items():
    btn = tk.Button(scrollable_frame, text=script_name, command=lambda s=script_name: run_script(s, SCRIPTS[s]))
    btn.pack(pady=5)
    btn.configure(anchor="center")
    ToolTip(btn, f"Click to run {script_name} analysis")

root.mainloop()
