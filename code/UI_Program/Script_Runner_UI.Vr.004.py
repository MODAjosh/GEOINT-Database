import tkinter as tk
from tkinter import messagebox, scrolledtext, Toplevel, Label, Entry, Button
import subprocess

# Define the script categories and their corresponding tools
SCRIPTS = {
    "Data Analysis": {
        "Buffer Analysis": {
            "script": "buffer_analysis.py",
            "inputs": [
                {"label": "Input File (Shapefile)", "placeholder": "e.g., input.shp", "type": "file"},
                {"label": "Buffer Distance (meters)", "placeholder": "e.g., 100", "type": "number"},
                {"label": "Output File", "placeholder": "e.g., output.shp", "type": "text"}
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
        "Extract Statistics": {
            "script": "extract_statistics.py",
            "inputs": [
                {"label": "Input Raster File", "placeholder": "e.g., input.tif", "type": "file"},
                {"label": "Output File", "placeholder": "e.g., statistics.json", "type": "text"}
            ]
        }
    },
    "Data Preprocessing": {
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
        "Reproject Raster": {
            "script": "reproject_raster.py",
            "inputs": [
                {"label": "Input Raster File", "placeholder": "e.g., input.tif", "type": "file"},
                {"label": "Target CRS", "placeholder": "e.g., EPSG:4326", "type": "text"},
                {"label": "Output File", "placeholder": "e.g., reprojected_output.tif", "type": "text"}
            ]
        }
    }
}


# Function to log messages
def log_message(message, log_widget):
    log_widget.configure(state="normal")
    log_widget.insert(tk.END, message + "\n")
    log_widget.configure(state="disabled")
    log_widget.yview(tk.END)


# Function to run a script
def run_script(script_name, log_widget):
    # Extract the category and script information
    category = find_category_for_script(script_name)
    script_info = SCRIPTS[category].get(script_name)

    if not script_info:
        messagebox.showerror("Error", f"Script '{script_name}' not found.")
        return

    open_input_dialog(script_name, script_info, log_widget)


# Function to find the category a script belongs to
def find_category_for_script(script_name):
    for category, scripts in SCRIPTS.items():
        if script_name in scripts:
            return category
    return None


# Function to create a custom input dialog
def open_input_dialog(script_name, script_info, log_widget):
    def submit_inputs():
        # Gather inputs from the dialog
        inputs = {field["label"]: entries[field["label"]].get() for field in script_info["inputs"]}
        if any(value.strip() == "" for value in inputs.values()):
            messagebox.showwarning("Warning", "All fields must be filled out.")
            return

        # Close the dialog and run the script
        dialog.destroy()
        run_script_with_inputs(script_info["script"], inputs, log_widget)

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
def run_script_with_inputs(script_path, inputs, log_widget):
    # Convert inputs to command-line arguments
    args = []
    for key, value in inputs.items():
        args.append(value)

    try:
        # Log the start of execution
        log_message(f"Running {script_path} with inputs: {inputs}", log_widget)

        # Run the script with inputs
        command = ["python", script_path] + args
        result = subprocess.run(command, capture_output=True, text=True)

        # Log the output and errors
        if result.stdout:
            log_message(f"Output from {script_path}:\n{result.stdout}", log_widget)
        if result.stderr:
            log_message(f"Errors from {script_path}:\n{result.stderr}", log_widget)

        messagebox.showinfo("Execution Complete",
                            f"Finished running {script_path}. Check the log for details.")
    except Exception as e:
        log_message(f"Error: Failed to run {script_path}. {str(e)}", log_widget)
        messagebox.showerror("Error",
                             f"Failed to run script '{script_path}'.\n\n{str(e)}")


# Initialize the Tkinter window
root = tk.Tk()
root.title("Geospatial Analysis Toolkit")
root.geometry("600x800")

# Add a header
header = tk.Label(root, text="Geospatial Analysis Toolkit", font=("Helvetica", 16))
header.pack(pady=10)

# Add a frame for category buttons
category_frame = tk.Frame(root)
category_frame.pack(pady=10)

# Add category buttons
for category_name in SCRIPTS.keys():
    category_btn = tk.Button(category_frame, text=category_name, command=lambda c=category_name: open_category(c),
                             width=40)
    category_btn.pack(pady=5)


# Function to display scripts for a selected category
def open_category(category_name):
    script_frame = tk.Frame(root)
    script_frame.pack(pady=10)

    for script_name in SCRIPTS[category_name].keys():
        script_btn = tk.Button(script_frame, text=script_name,
                               command=lambda s=script_name: run_script(s, log_window), width=40)
        script_btn.pack(pady=5)


# Add a logging section
log_label = tk.Label(root, text="Execution Log", font=("Helvetica", 14))
log_label.pack(pady=5)

log_window = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=70, height=20, state="disabled", bg="black",
                                       fg="white")
log_window.pack(pady=10)

# Add a quit button
quit_button = tk.Button(root, text="Quit", command=root.quit, width=40, bg="red", fg="white")
quit_button.pack(pady=10)

# Run the Tkinter main loop
root.mainloop()
