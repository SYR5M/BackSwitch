from rembg import remove
from PIL import Image
import io
from tkinter import filedialog, messagebox

def replace_background_with_image(file_path):
    try:
        # Select a new background image
        bg_path = filedialog.askopenfilename(
            title="Select Background Image",
            filetypes=[("Image Files", "*.jpg *.jpeg *.png")]
        )
        if not bg_path:
            messagebox.showwarning("No Background Selected", "Please select a background image.")
            return

        # Read the main image
        with open(file_path, "rb") as input_file:
            input_data = input_file.read()
        
        # Remove the background
        output_data = remove(input_data)
        image_no_bg = Image.open(io.BytesIO(output_data))
        
        # Read the new background image
        new_bg = Image.open(bg_path).resize(image_no_bg.size)

        # Combine the object with the new background
        result_image = Image.composite(image_no_bg, new_bg, image_no_bg)

        # Save the result
        save_path = filedialog.asksaveasfilename(
            title="Save Image with New Background",
            defaultextension=".png",
            filetypes=[("PNG Files", "*.png")]
        )
        if save_path:
            result_image.save(save_path)
            messagebox.showinfo("Success", "Image saved with new background!")
        else:
            messagebox.showwarning("Save Cancelled", "No file was saved.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
