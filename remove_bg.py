from rembg import remove
from PIL import Image
import io
from tkinter import filedialog, messagebox

def remove_background(file_path):
    try:
        # Read the image as raw data
        with open(file_path, "rb") as input_file:
            input_data = input_file.read()
        
        # Remove the background
        output_data = remove(input_data)
        
        # Convert the data to an image
        output_image = Image.open(io.BytesIO(output_data))
        
        # Save the result
        save_path = filedialog.asksaveasfilename(
            title="Save Processed Image",
            defaultextension=".png",
            filetypes=[("PNG Files", "*.png")]
        )
        if save_path:
            output_image.save(save_path)
            messagebox.showinfo("Success", "Background removed and saved successfully!")
        else:
            messagebox.showwarning("Save Cancelled", "No file was saved.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
