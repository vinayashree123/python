import tkinter as tk
import time

# Define the list of colors to display
colors = ["yellow", "green", "blue", "white"
    , "black"]

# Set the screen resolution and duration for each color (in seconds)
screen_width = 1920  # Adjust to your display's resolution
screen_height = 1080  # Adjust to your display's resolution
color_duration = 5  # Adjust the duration for each color

def display_color(color):
    root = tk.Tk()
    root.attributes("-fullscreen", True)
    canvas = tk.Canvas(root, width=screen_width, height=screen_height)
    canvas.create_rectangle(0, 0, screen_width, screen_height, fill=color)
    canvas.pack()

    root.update_idletasks()
    root.update()

    # Display the color for the specified duration
    time.sleep(color_duration)

    root.destroy()

if __name__ == "__main__":
    for color in colors:
        print(f"Displaying {color} for {color_duration} seconds...")
        display_color(color)
        time.sleep(1)  # Pause for 1 second between colors

    print("Display testing complete.")
