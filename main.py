import tkinter as tk
from tkinter import filedialog, messagebox
from remove_bg import remove_background
from green_bg import make_background_green
from replace_bg import replace_background_with_image

def browse_file():
    file_path = filedialog.askopenfilename(
        title="Select Image",
        filetypes=[("Image Files", "*.jpg *.jpeg *.png")]
    )
    if not file_path:
        messagebox.showwarning("No File Selected", "Please select a file.")
        return

    # Create a new window for options
    def choose_option():
        selected_option = var.get()
        if selected_option == 1:
            remove_background(file_path)
        elif selected_option == 2:
            make_background_green(file_path)
        elif selected_option == 3:
            replace_background_with_image(file_path)
        else:
            messagebox.showwarning("No Option Selected", "Please select an option.")

    option_window = tk.Toplevel(root)
    option_window.title("BackSwitch")
    option_window.geometry("400x200")

    var = tk.IntVar()
    tk.Radiobutton(option_window, text="Remove Background", variable=var, value=1).pack(anchor="w")
    tk.Radiobutton(option_window, text="Make Background Green", variable=var, value=2).pack(anchor="w")
    tk.Radiobutton(option_window, text="Replace Background with Custom Image", variable=var, value=3).pack(anchor="w")

    tk.Button(option_window, text="Apply", command=choose_option).pack(pady=10)

# Main user interface
root = tk.Tk()
root.title("BackSwitch")

# Add the icon to the application
icon_path = "BackSwitch.ico"  # Ensure the .ico file is in the same directory as main.py
root.iconbitmap(icon_path)

# Set window size
root.geometry("400x200")

# Add a label for the program title
label_title = tk.Label(
    root, text="Welcome to BackSwitch", font=("Arial", 16, "bold")
)
label_title.pack(pady=10)

# Button to select files
btn_select = tk.Button(
    root, text="Select Image and Choose Action", command=browse_file, font=("Arial", 14), padx=10, pady=5
)
btn_select.pack(pady=20)

# Run the application
root.mainloop()
