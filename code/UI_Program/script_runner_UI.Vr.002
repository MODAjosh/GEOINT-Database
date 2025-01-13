import tkinter as tk
from tkinter import messagebox, simpledialog, scrolledtext, Toplevel, Label, Entry, Button
import subprocess

# Define the script list with specific input fields
SCRIPTS = {
    "Buffer Analysis": {
        "script": "buffer_analysis.py",
        "inputs": [
            {"label": "Input File (Shapefile)", "placeholder": "e.g., input.shp"},
            {"label": "Buffer Distance (meters)", "placeholder": "e.g., 100"},
            {"label": "Output File", "placeholder": "e.g., output.shp"}
        ]
    },
    "Calculate Distance": {
        "script": "calculate_distance.py",
        "inputs": [
            {"label": "Point A Coordinates (lat, lon)", "placeholder": "e.g., 40.7128,-74.0060"},
            {"label": "Point B Coordinates (lat, lon)", "placeholder": "e.g., 34.0522,-118.2437"}
        ]
    },
    # Add other scripts with their specific inputs here
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
