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

    def show_tooltip(self, _):
        x = self.widget.winfo_rootx() + 10
        y = self.widget.winfo_rooty() + 10
        self.tooltip = tk.Toplevel(self.widget)
        self.tooltip.wm_overrideredirect(True)
        self.tooltip.geometry(f"+{x}+{y}")
        label = tk.Label(self.tooltip, text=self.text, background="lightyellow", relief="solid", padx=5, pady=5)
        label.pack()

    def hide_tooltip(self, _):
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
def run_script(selected_script_name, selected_script_info):
    open_input_dialog(selected_script_name, selected_script_info)


# Function to create a custom input dialog
def open_input_dialog(selected_script_name, selected_script_info):
    def submit_inputs():
        inputs = {field["label"]: entries[field["label"]].get() for field in selected_script_info["inputs"]}
        if not validate_inputs(inputs, input_types):
            return

        log_message(log_window, f"Inputs for {selected_script_name}: {inputs}")
        run_script_with_inputs(selected_script_info["script"], inputs, log_window)

    dialog = Toplevel(root)
    dialog.title(f"Inputs for {selected_script_name}")
    dialog.geometry("600x400")
    dialog.resizable(True, True)

    entries = {}
    input_types = {}
    for idx, field in enumerate(selected_script_info["inputs"]):
        Label(dialog, text=field["label"]).grid(row=idx, column=0, pady=5, padx=5, sticky="e")
        entry = Entry(dialog, width=30)
        entry.insert(0, field["placeholder"])
        entry.grid(row=idx, column=1, pady=5, padx=5)
        entries[field["label"]] = entry
        input_types[field["label"]] = field["type"]

        if field["type"] == "file":
            browse_button = Button(dialog, text="Browse", command=lambda e=entry: browse_file(e))
            browse_button.grid(row=idx, column=2, padx=5, pady=5)

        ToolTip(entry, field["tooltip"])

    log_label = Label(dialog, text="Execution Log")
    log_label.grid(row=len(selected_script_info["inputs"]), column=0, columnspan=3, pady=10)

    log_window = scrolledtext.ScrolledText(dialog, wrap=tk.WORD, width=70, height=10, state="disabled", bg="black", fg="white")
    log_window.grid(row=len(selected_script_info["inputs"]) + 1, column=0, columnspan=3, pady=5)

    Button(dialog, text="Run Script", command=submit_inputs).grid(row=len(selected_script_info["inputs"]) + 2, columnspan=3, pady=10)


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
        "script": "./code/analysis_tools/buffer_analysis.py",
        "inputs": [
            {
                "label": "Input File",
                "placeholder": "input.shp",
                "type": "file",
                "tooltip": "Select the input shapefile."
            },
            {
                "label": "Buffer Distance",
                "placeholder": "100",
                "type": "number",
                "tooltip": "Enter buffer distance."
            },
            {
                "label": "Output File",
                "placeholder": "output.shp",
                "type": "text",
                "tooltip": "Specify the output file."
            },
        ]
    },
    "Calculate Centroid": {
        "script": "./code/analysis_tools/calculate_centroid.py",
        "inputs": [
            {
                "label": "Input File",
                "placeholder": "input.shp",
                "type": "file",
                "tooltip": "Select the input shapefile."
            },
            {
                "label": "Output File",
                "placeholder": "output_centroid.shp",
                "type": "text",
                "tooltip": "Specify the output file."
            },
        ]
    }
}


# Initialize Tkinter
root = tk.Tk()
root.title("Geospatial Analysis Toolkit")
root.geometry("600x800")

header = tk.Label(root, text="Geospatial Analysis Toolkit", font=("Helvetica", 16))
header.pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack(pady=10, fill="both", expand=True)

for script_name, script_info in SCRIPTS.items():
    btn = tk.Button(
        button_frame,
        text=script_name,
        command=lambda s=script_name: run_script(s, SCRIPTS[s]),
        width=40,
        anchor="w",
    )
    btn.pack(fill="x", padx=5, pady=5)
    ToolTip(btn, f"Click to run {script_name} analysis")

root.mainloop()
