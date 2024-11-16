from rembg import remove
from PIL import Image
import io
from tkinter import filedialog, messagebox

def make_background_green(file_path):
    try:
        # Read the image
        with open(file_path, "rb") as input_file:
            input_data = input_file.read()
        
        # Remove the background
        output_data = remove(input_data)
        
        # Convert the data to an image
        image_no_bg = Image.open(io.BytesIO(output_data))
        
        # Create a green background
        green_background = Image.new("RGB", image_no_bg.size, (0, 255, 0))
        result_image = Image.composite(image_no_bg, green_background, image_no_bg)

        # Save the result
        save_path = filedialog.asksaveasfilename(
            title="Save Image with Green Background",
            defaultextension=".png",
            filetypes=[("PNG Files", "*.png")]
        )
        if save_path:
            result_image.save(save_path)
            messagebox.showinfo("Success", "Image saved with green background!")
        else:
            messagebox.showwarning("Save Cancelled", "No file was saved.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
