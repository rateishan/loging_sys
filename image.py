import tkinter as tk
from PIL import Image, ImageTk

# Initialize the main window
root = tk.Tk()
root.title("Background Image Example")
root.geometry("800x600")  # Set the size of the window

# Load the image
image = Image.open("path/to/your/image.jpg")
background_image = ImageTk.PhotoImage(image)

# Create a canvas
canvas = tk.Canvas(root, width=image.width(), height=image.height())
canvas.pack(fill="both", expand=True)

# Set the background image
canvas.create_image(0, 0, image=background_image, anchor="nw")

# Add other widgets on top of the canvas
label = tk.Label(root, text="Hello, World!", font=("Helvetica", 24), bg="white")
label_window = canvas.create_window(400, 300, anchor="center", window=label)

# Run the application
root.mainloop()
