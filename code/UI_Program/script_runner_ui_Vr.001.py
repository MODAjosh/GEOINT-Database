import tkinter as tk
from tkinter import simpledialog, messagebox, scrolledtext
import subprocess


# Define the script list
SCRIPTS = {
    "Buffer Analysis": "buffer_analysis.py",
    "Calculate Buffer Zone": "calculate_buffer_zone.py",
    "Calculate Centroid": "calculate_centroid.py",
    "Calculate Distance": "calculate_distance.py",
    "Calculate Slope": "calculate_slope.py",
    "Clip Raster by Shapefile": "clip_raster_by_shapefile.py",
    "Extract Statistics": "extract_statistics.py",
    "NDVI Calculation": "ndvi_calculation.py",
    "Perform Geospatial Analysis": "perform_geospatial_analysis.py",
    "Buffer Vector Data": "buffer_vector_data.py",
    "Clip Raster by Polygon": "clip_raster_by_polygon.py",
    "Clip Shapefile by Polygon": "clip_shapefile_by_polygon.py",
    "Merge Data": "merge_data.py",
    "Normalize Raster": "normalize_raster.py",
    "Rasterize Vector": "rasterize_vector.py",
    "Reformat to GeoTIFF": "reformat_to_geotiff.py",
    "Remove Outliers": "remove_outliers.py",
    "Reproject Raster": "reproject_raster.py",
    "Shapefile to GeoJSON": "shapefile_to_geojson.py",
}


# Function to log messages
def log_message(message):
    log_window.configure(state="normal")
    log_window.insert(tk.END, message + "\n")
    log_window.configure(state="disabled")
    log_window.yview(tk.END)


# Function to run a script
def run_script(script_name):
    script_path = SCRIPTS.get(script_name)
    if not script_path:
        messagebox.showerror("Error", f"Script '{script_name}' not found.")
        return
    
    # Prompt the user for arguments
    args = simpledialog.askstring(
        "Input Arguments",
        f"Enter arguments for '{script_name}' (separated by spaces):"
    )
    if args is None:  # User canceled
        return

    try:
        # Log the start of execution
        log_message(f"Running {script_name} with arguments: {args if args else '(no arguments)'}")
        
        # Run the script with arguments
        command = ["python", script_path] + args.split()
        result = subprocess.run(command, capture_output=True, text=True)
        
        # Log the output and errors
        if result.stdout:
            log_message(f"Output from {script_name}:\n{result.stdout}")
        if result.stderr:
            log_message(f"Errors from {script_name}:\n{result.stderr}")

        messagebox.showinfo("Execution Complete", f"Finished running {script_name}. Check the log for details.")
    except Exception as e:
        log_message(f"Error: Failed to run {script_name}. {str(e)}")
        messagebox.showerror("Error", f"Failed to run script '{script_name}'.\n\n{str(e)}")


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
